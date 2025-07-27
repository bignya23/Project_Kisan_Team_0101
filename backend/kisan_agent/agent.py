from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from . import prompt
from .sub_agents.crop_disease_agent import main_agent_1
from .sub_agents.government_scheme_agent import main_agent_3
from .sub_agents.market_analysis_agent import main_agent_2
from .voice.stt import speech_to_text_hindi
from .voice.tts import text_to_speech_male_hindi

MODEL = "gemini-2.5-pro"

kisan_agent = LlmAgent(
    name="kisan",
    model=MODEL,
    description=(
        "analyzing agricultural challenges provided by farmers, "
        "providing comprehensive farming advice, coordinating specialized sub-agents "
        "for crop disease detection with remedies, market price analysis, "
        "and government schemes navigation, integrating multi-agent responses "
        "into unified agricultural solutions, and accessing web resources "
        "to acquire current agricultural knowledge and market intelligence"
        "Run the text_to_speech_male_hindi tool only when is_audio = True is written at the end of the output and then output the said text in the final response."
    ),
    instruction=prompt.FARMER_COORDINATOR_PROMPT,
    
    tools=[
        AgentTool(agent=main_agent_1),
        AgentTool(agent=main_agent_2),
        AgentTool(agent=main_agent_3),
        text_to_speech_male_hindi,
    ],
)

root_agent = kisan_agent

