import configuration.load_configuration
from databases.mongo_db.connection_manager import MongoDBConnectionManager

# Initialize the connection manager
mongo_db_connection_manager = MongoDBConnectionManager()

# Get a connection to a specific database
db1 = mongo_db_connection_manager.get_database("k2")
print(db1)
collection1 = db1["test"]
collection1.insert_one({"name":"test"})
