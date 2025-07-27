
from datetime import datetime
from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LlmAgent
from google.adk.tools import google_search
from .holiday import get_holidays_list
from .weather import weather_tool
from .mandi import fetch_mandi_data
from .wholesale_price_index import wpi_tool
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_AUTH_CREDENTIALS")


def holiday_tool():
    """Returns holidays for the current month using Google Calendar API."""
    return get_holidays_list()

def mandi_tool(state: str = "Uttar Pradesh"):
    """Returns mandi price data for a given state."""
    return fetch_mandi_data(state)


news_agent = LlmAgent(
    name="news_agent",
    model="gemini-2.5-flash",
    description="Provides market news and sentiment for a location or commodity.",
    instruction="Use google_search to find latest market news & sentiment. Return a concise summary.",
    tools=[google_search],
    output_key="news_data"
)

weather_agent = LlmAgent(
    name="weather_agent",
    model="gemini-2.5-flash",
    description="Provides the 10-day weather forecast for a specific location.",
    instruction="Summarize temperature, rain chances, and extreme weather using weather_tool.",
    tools=[weather_tool],
    output_key="weather_data"
)

holiday_agent = LlmAgent(
    name="holiday_agent",
    model="gemini-2.5-flash",
    description="Fetches upcoming holidays and festivals that may affect demand.",
    instruction="Use the holiday_tool to list upcoming major holidays or festivals in the region.",
    tools=[holiday_tool],
    output_key="holiday_data"
)

mandi_agent = LlmAgent(
    name="mandi_agent",
    model="gemini-2.5-flash",
    description="Fetches mandi price data for the given state.",
    instruction="Use mandi_tool to get latest mandi price data. Return as is.",
    tools=[mandi_tool],
    output_key="mandi_data"
)

wpi_agent = LlmAgent(
    name="wpi_agent",
    model="gemini-2.5-flash",
    description="Fetches WPI trend for the requested commodity.",
    instruction="Use wpi_tool to get the latest WPI and basic trend (Uptrend/Downtrend).",
    tools=[wpi_tool],
    output_key="wpi_data"
)

gatherer = ParallelAgent(
    name="InfoGatherer",
    sub_agents=[news_agent, weather_agent, holiday_agent, mandi_agent, wpi_agent]
)

market_agent = LlmAgent(
    name="market_combined_agent",
    model="gemini-2.5-pro",
    description="Combines all data (news, weather, holidays, mandi prices, WPI) into a single actionable insight.",
    instruction=(
        "You are a combined assistant. "
        "This is the : "
        "NEWS : {news_data} "
        "Holidays : {holiday_data} "
        "Mandi Prices : {mandi_data} "
        "WPI Trends : {wpi_data} "
        "Weather : {weather_data} "
        "Finally, combine all the information into a comprehensive response to analyze market trends.\n"
        "Step 1: Compare WPI trends and mandi prices to estimate price movement (Uptrend / Downtrend).\n"
        "Step 2: Factor in holidays, festivals, and weather to predict demand shifts.\n"
        "Step 3: Provide a simple, actionable recommendation to farmers — "
        "Should they SELL now, HOLD, or WAIT? Clearly justify based on data (WPI, mandi, weather, and news).\n"
        "Step 4: End with 2-3 short bullet points summarizing key reasons for the prediction."
    ),
    output_key="final_market_analysis"
)

main_agent_2 = SequentialAgent(
    name="seq_agent",
    sub_agents=[gatherer, market_agent]
)
