import logging
from strands import Agent
from strands_tools import calculator
from strands.models.ollama import OllamaModel

# Enables Strands debug log level
logging.getLogger("strands").setLevel(logging.DEBUG)
#logging.getLogger("strands").setLevel(logging.INFO)

# Sets the logging format and streams logs to stderr
logging.basicConfig( format="%(levelname)s | %(name)s | %(message)s", handlers=[logging.StreamHandler()])

# Initialize the agent with tools, model, and configuration
llm = OllamaModel(
        host="http://localhost:11434",
        model_id="mistral",
        )
agent = Agent(
        model=llm,
        tools=[calculator],
        system_prompt="You are a helpful assistant."
        )

# Process user input
result = agent("Calculate (25 * 48) - 2")
print(result)
