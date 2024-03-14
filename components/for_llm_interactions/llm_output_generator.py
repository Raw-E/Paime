from .openai_client import OpenAIClient
from .llm_input_generator import LLMInputGenerator


class LLMOutputGenerator:
    def __init__(self):
        self.openai_client = OpenAIClient()
        self.llm_input_generator = LLMInputGenerator()

    def generate_output(self, config):
        """
        Generates output from the LLM based on a provided configuration.

        Parameters:
        - config (dict): Configuration for generating messages and handling the LLM interaction.

        Returns:
        - str: The raw response from the LLM.
        """
        messages = self.llm_input_generator.generate_messages_for_llm(config)
        response = self.openai_client.get_response_from_llm(messages)
        return response
