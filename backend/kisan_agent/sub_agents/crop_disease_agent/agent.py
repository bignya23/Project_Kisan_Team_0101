import os
from PIL import Image
import google.genai as genai
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import FunctionTool, google_search
from dotenv import load_dotenv
import os
from .prompt import CROP_ANALYSIS_PROMPT

load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_AUTH_CREDENTIALS")


disease_agent = LlmAgent(
    name="crop_disease_agent",
    model="gemini-2.5-pro",
    description="Identifies plant diseases from an image.",
    instruction=(
        "You are an agricultural assistant. "
        "Only return the disease name and also the name of the plant in short, e.g., 'Powdery Mildew'."
    ),
    output_key="disease_name"
)

remedies_agent = LlmAgent(
    name="remedies_agent",
    model="gemini-2.5-pro",
    description="Suggests remedies for a given plant disease.",
    instruction=(
        CROP_ANALYSIS_PROMPT
    ),
    tools=[google_search],
    output_key="remedies"
)

# Main Sequential Agent
main_agent_1 = SequentialAgent(
    name="final_crop_disease_assistant",
    sub_agents=[disease_agent, remedies_agent],
    description=(
        "This assistant takes a plant image, detects the disease, "
        "and then suggests effective remedies."
    )
)







