from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from .search_datastore import search_sample
from .prompt import SCHEMAS_PROMPT


schemes_agent = LlmAgent(
    model="gemini-2.5-pro",
    name="government_schemes_navigator",
    description=("Navigate government agricultural schemes using both local datastore and live Google search to provide comprehensive, up-to-date information about subsidies, eligibility, and application processes."),
    instruction=("Fetch all the info related to the query using search sample"),
    tools=[search_sample],
    output_key="schemes"
)

eligibility_agent = LlmAgent(
    model="gemini-2.5-pro",
    name="eligibility_navigator",
    description=("Navigate government agricultural schemes using both local datastore and live Google search to provide comprehensive, up-to-date information about subsidies, eligibility, and application processes."),
    instruction=("Fetch all the eligibility criteria related to this info {schemes}"),
    tools=[google_search],
    output_key="eligibility"
)


main_agent_3 = SequentialAgent(
    name="final_crop_disease_assistant",
    sub_agents=[schemes_agent, eligibility_agent],
    description=(
        SCHEMAS_PROMPT
    )
)





