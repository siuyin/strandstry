import logging
from strands import Agent
from strands.models.ollama import OllamaModel

# Enables Strands debug log level
logging.getLogger("strands").setLevel(logging.DEBUG)

# Sets the logging format and streams logs to stderr
logging.basicConfig(
        format="%(levelname)s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler()]
        )

llm = OllamaModel(
        host="http://localhost:11434",
        model_id="gemma3:1b",
        )
agent = Agent(model=llm)

res = agent("Hello!")

print("------------ agent result print ----")
print(res.stop_reason)
print(res.metrics)
print(res.state)
print(res.message)
