from utilities.json_related import clean_and_load_json


class LLMOutputProcessor:
    @staticmethod
    def process_response(response, config):
        """
        Processes the LLM's response based on the provided configuration.

        Parameters:
        - response (str): The raw response from the LLM.
        - config (dict): The configuration object used for the LLM interaction.

        Returns:
        - The processed response from the LLM, which may be a JSON object or raw text, depending on the 'outputFormat'.
        """
        if LLMOutputProcessor._should_process_as_json(config):
            return LLMOutputProcessor._process_json_response(response)
        else:
            return response

    @staticmethod
    def _should_process_as_json(config):
        """
        Determines if the response should be processed as JSON based on the 'outputFormat' field in the config.
        Specifically checks if 'outputFormat' is a JSON object.

        Parameters:
        - config (dict): The configuration object used for the LLM interaction.

        Returns:
        - bool: True if the 'outputFormat' is a JSON object, False otherwise.
        """
        output_format = config.get("desiredOutput", {}).get("outputFormat", {})
        return isinstance(output_format, dict) and bool(output_format)

    @staticmethod
    def _process_json_response(response):
        """
        Cleans and processes the JSON response from the LLM.
        """
        response = clean_and_load_json(response)
        if response:  # Ensure response is not empty
            return response
        else:
            return {}
