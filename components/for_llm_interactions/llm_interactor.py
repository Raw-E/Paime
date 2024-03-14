from .llm_output_generator import LLMOutputGenerator
from .llm_output_processor import LLMOutputProcessor


class LLMInteractor:
    """
    A class to interact with a Large Language Model (LLM) by using a provided configuration
    to generate and process outputs.
    """

    def __init__(self):
        self.llm_output_generator = LLMOutputGenerator()
        self.llm_outpt_processor = LLMOutputProcessor()

    def interact(self, config):
        """
        Uses the LLM to generate and process output based on the provided configuration.

        :param config: The configuration for the LLM.
        :return: Processed output from the LLM.
        """
        raw_response = self.llm_output_generator.generate_output(config)
        processed_response = self.llm_outpt_processor.process_response(raw_response, config)
        return processed_response
