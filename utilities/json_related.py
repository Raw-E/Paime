import json
import re


def is_valid_json(obj):
    """
    Checks if the object can be serialized to a JSON string.

    Parameters:
    - obj (any): The object to check.

    Returns:
    - bool: True if the object can be serialized to JSON, False otherwise.
    """
    try:
        json.dumps(obj)
        return True
    except (TypeError, OverflowError):
        return False


def clean_and_load_json(response):
    """
    Cleans the response and loads it into a JSON object.

    Args:
        response (str): The raw response string from the language model.

    Returns:
        dict or None: The loaded JSON object if successful, None otherwise.
    """
    try:
        # Assuming the response is always a valid JSON string encapsulated in some extra text.
        json_str = re.search(r"{.*}", response, flags=re.DOTALL).group()
        return json.loads(json_str)
    except (json.JSONDecodeError, AttributeError) as e:
        print(f"Failed to process the response: {e}")
        return None
