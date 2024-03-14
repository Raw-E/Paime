import json
from utilities import json_related


class LLMInputGenerator:
    def __init__(self):
        pass

    def generate_messages_for_llm(self, config):
        """
        Generates messages for the language model based on a configuration object.

        Parameters:
        - config (dict): Configuration for generating messages, including:
          - desired_output (dict): A dictionary specifying the desired output.
          - context (str, optional): Additional context or information.
          - custom_messages (list, optional): List of custom message dictionaries.

        Returns:
        - list: A list of message dictionaries to be sent to the language model.
        """
        desired_output = config.get("desiredOutput", {})
        context = config.get("context", None)
        custom_messages = config.get("custom_messages", [])

        if not json_related.is_valid_json(desired_output.get("outputFormat", {})):
            raise ValueError("outputFormat must be a valid JSON object")

        messages = [
            {"role": "system", "content": "Try to create the desired output."},
            {
                "role": "system",
                "content": f"Desired output description: {desired_output.get('description', '')}",
            },
            {
                "role": "system",
                "content": f"Additional info: {context}" if context else "",
            },
            {
                "role": "system",
                "content": f"Exact output format: {json.dumps(desired_output.get('outputFormat', {}))}",
            },
        ] + custom_messages

        print("Generated messages for LLM:", messages, "\n---\n")
        return messages
