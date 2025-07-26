from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.crop_disease_agent import main_agent_1
from .sub_agents.government_scheme_agent import main_agent_3
from .sub_agents.market_analysis_agent import main_agent_2

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
    ),
    instruction=prompt.FARMER_COORDINATOR_PROMPT,
    
    tools=[
        AgentTool(agent=main_agent_1),
        AgentTool(agent=main_agent_2),
        AgentTool(agent=main_agent_3),
    ],
)

root_agent = kisan_agent