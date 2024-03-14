import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDBConnectionManager:
    """
    Manages MongoDB connections using MongoClient from PyMongo.
    
    Attributes:
        connections (dict): A dictionary to store MongoClient connections keyed by database names.
    """
    
    def __init__(self):
        """
        Initializes the MongoDBConnectionManager with an empty connections dictionary.
        """
        self.connections = {}

    def get_database(self, database_name: str) -> MongoClient:
        """
        Retrieves a database object for the specified database.
        
        If a connection to the database does not already exist in the `connections` dictionary,
        a new connection is created and added to the dictionary. The database object from this
        connection is then returned.
        
        Parameters:
            database_name (str): The name of the database to connect to.
        
        Returns:
            MongoClient: A database object for the specified database.
        """
        if database_name not in self.connections:
            self.connections[database_name] = self._create_connection(database_name)
        return self.connections[database_name]

    def _create_connection(self, database_name: str) -> MongoClient:
        """
        Creates a new MongoClient connection to the specified database.
        
        This method constructs a MongoDB URI using environment variables for secure access,
        then attempts to establish a connection to the database. If the connection fails,
        it raises a ConnectionFailure exception.
        
        Parameters:
            database_name (str): The name of the database to connect to.
        
        Returns:
            MongoClient: A MongoClient connection to the specified database.
        
        Raises:
            ConnectionFailure: If the connection to MongoDB cannot be established.
        """
        uri = self._construct_uri(database_name)
        try:
            client = MongoClient(uri)
            # Directly return the database object from the client
            return client[database_name]
        except ConnectionFailure as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise

    def _construct_uri(self, database_name: str) -> str:
        """
        Constructs the MongoDB URI for the specified database using environment variables.
        
        Parameters:
            database_name (str): The name of the database for which to construct the URI.
        
        Returns:
            str: The constructed MongoDB URI.
        """
        return (
            f"mongodb+srv://"
            f"{os.getenv('MONGO_DB_ATLAS_USERNAME')}:"
            f"{os.getenv('MONGO_DB_ATLAS_PASSWORD')}@"
            f"{os.getenv('MONGO_DB_ATLAS_CLUSTER_ADDRESS')}/"
            f"{database_name}?retryWrites=true&w=majority"
        )

    def close_all_connections(self):
        """
        Closes all MongoClient connections stored in the `connections` dictionary.
        
        This method iterates through all connections, closes each one, and then removes
        it from the dictionary to ensure no stale connections are left.
        """
        for db_name, connection in list(self.connections.items()):
            connection.client.close()
            del self.connections[db_name]