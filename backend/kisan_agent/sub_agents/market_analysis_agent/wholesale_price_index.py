import pandas as pd

def wpi_tool(item_name: str):
    """
    Reads the local WPI CSV file and returns the latest WPI index 
    and a basic prediction (Uptrend / Downtrend).
    """
    try:
        df = pd.read_csv("/home/user/t0101projectkisan/backend/kisan_agent/sub_agents/market_analysis_agent/wholesale_price_index.csv")
        filtered = df[df["Item Name"].str.contains(item_name, case=False, na=False)]
        if filtered.empty:
            return f"No WPI data found for {item_name}."

        filtered = filtered.copy()  # avoid SettingWithCopyWarning
        filtered.loc[:, "YearMonth"] = pd.to_datetime(
            filtered["Year"].astype(str) + "-" + filtered["Month"],
            format="%Y-%B"
        )

        filtered = filtered.sort_values("YearMonth")

        latest = filtered.iloc[-1]
        latest_value = latest["IndexValue"]

        if len(filtered) >= 2:
            prev_value = filtered.iloc[-2]["IndexValue"]
            trend = "Uptrend" if latest_value > prev_value else "Downtrend"
        else:
            trend = "Insufficient data for trend"

        return f"WPI for {item_name} ({latest['Month']} {latest['Year']}): {latest_value} | Trend: {trend}"

    except Exception as e:
        return f"Error reading WPI data: {str(e)}"


if __name__ == "__main__":
    print(wpi_tool("Wheat"))
    print(wpi_tool("Rajma"))
    print(wpi_tool("Almonds"))
