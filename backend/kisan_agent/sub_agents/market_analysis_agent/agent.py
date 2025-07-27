from datetime import datetime
from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LlmAgent
from google.adk.tools import google_search
from .holiday import get_holidays_list
from .weather import weather_tool
# from .mandi import fetch_mandi_data
from dotenv import load_dotenv
import os


load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_AUTH_CREDENTIALS")

def holiday_tool():
    """
    Returns holidays for the current month using Google Calendar API.
    """
    return get_holidays_list()


def mandi_tool(state: str = "Uttar Pradesh"):
    """
    Returns mandi price data for a given state.
    """
    # return fetch_mandi_data(state)
    return """Papaya (Papaya): ₹2750 - ₹2880 (Modal: ₹2810) | Market: Badayoun, District: Badaun
Tomato (Deshi): ₹2830 - ₹3000 (Modal: ₹2895) | Market: Badayoun, District: Badaun
Wheat (Dara): ₹2450 - ₹2490 (Modal: ₹2470) | Market: Dataganj, District: Badaun
Apple (Delicious): ₹12850 - ₹13200 (Modal: ₹13000) | Market: Wazirganj, District: Badaun
Cabbage (Cabbage): ₹1350 - ₹1425 (Modal: ₹1400) | Market: Wazirganj, District: Badaun
Green Chilli (Green Chilly): ₹4025 - ₹4100 (Modal: ₹4060) | Market: Wazirganj, District: Badaun
Onion (Red): ₹1425 - ₹1475 (Modal: ₹1440) | Market: Wazirganj, District: Badaun
Onion (Red): ₹1300 - ₹1340 (Modal: ₹1315) | Market: Wazirganj, District: Badaun
Papaya (Papaya): ₹2750 - ₹2825 (Modal: ₹2800) | Market: Wazirganj, District: Badaun
"""

news_agent = LlmAgent(
    name="news_agent",
    model="gemini-2.5-flash",
    description="Provides market news and sentiment for a location or commodity.",
    instruction="You are a search specialist. Use the google_search tool to find relevant news and market reports. Return a summary of key findings.",
    tools=[google_search],
    output_key="news_data"
)

weather_agent = LlmAgent(
    name="weather_agent",
    model="gemini-2.5-flash",
    description="Provides the 10-day weather forecast for a specific location.",
    instruction=(
        "You are a weather assistant. When given a location, "
        "use the 'weather_tool' to get the 10-day forecast. "
        "Summarize temperature, rain chances, and extreme weather if any."
    ),
    tools=[google_search],
    output_key="weather_data"
)


analysis_agent = LlmAgent(
    name="analysis_agent",
    model="gemini-2.5-flash",
    description=(
        "Analyzes holidays and local news to anticipate upcoming demand, such as festival or wedding seasons. "
        "Also provides mandi price data for a given state."
    ),
    instruction=(
        "You are a professional market analysis assistant. "
        "When the user asks for the price of an item, use the tools to get price and holiday information. Also use the googleSearch to get the prices of the specific region."
        "Return price information first, followed by relevant holiday/mandi analysis."
    ),
    tools=[holiday_tool, mandi_tool, google_search],
    output_key="final_data"
)


gatherer = ParallelAgent(
    name="InfoGatherer",
    sub_agents=[analysis_agent, news_agent, weather_agent]
)


main_final_agent = LlmAgent(
    name="market_final_agent",
    model="gemini-2.5-pro",
    instruction=(
        "You are a combined assistant. This is the : NEWS : {news_data} Mandi and holildays : {final_data}, Weather : {weather_data}"
        "Finally, combine all the information into a comprehensive response to  analyze trends, and provide a simple, actionable summary to guide selling decisions like upcoming trends of the prices and the reasons for it."
    ),
)

main_agent_2 = SequentialAgent(
    name="seq_agent",
    sub_agents=[gatherer, main_final_agent]
)
