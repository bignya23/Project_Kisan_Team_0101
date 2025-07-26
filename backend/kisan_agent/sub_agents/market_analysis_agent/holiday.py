from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta
import pytz

def get_holidays_list():
    """
    Fetches all Indian public holidays from Google Calendar
    between today and today+30 days (Asia/Kolkata).
    """
    # Compute date range
    india_tz = pytz.timezone("Asia/Kolkata")
    today = datetime.now(india_tz).isoformat()
    end = (datetime.now(india_tz) + timedelta(days=30)).isoformat()

    # Authenticate with Service Account
    creds = service_account.Credentials.from_service_account_file(
        "//home//user//t0101projectkisan//backend//kisan_agent//kisan-466906-575fadd46b5c.json",
        scopes=["https://www.googleapis.com/auth/calendar.readonly"]
    )
    service = build("calendar", "v3", credentials=creds)

    # Use the public Indian holidays calendar
    calendar_id = "en.indian#holiday@group.v.calendar.google.com"

    events = service.events().list(
        calendarId=calendar_id,
        timeMin=today,
        timeMax=end,
        singleEvents=True,
        orderBy="startTime"
    ).execute().get("items", [])

    # Format the output
    holidays = []
    for ev in events:
        date = ev["start"].get("date") or ev["start"].get("dateTime")
        holidays.append({
            "name": ev.get("summary"),
            "date": date
        })

    return {"holidays": holidays}


if __name__ == "__main__":
    print(get_holidays_list())