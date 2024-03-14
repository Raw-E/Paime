def read_file_contents(file_path):
    """
    Reads the contents of a file and returns it.

    Parameters:
    - file_path (str): The path to the file to be read.

    Returns:
    - str: The contents of the file.

    Raises:
    - FileNotFoundError: If the file does not exist.
    - PermissionError: If the program lacks necessary permissions to read the file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except PermissionError:
        raise PermissionError(f"Permission denied to read the file {file_path}.")
