from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# ✅ Path to your ChromeDriver
CHROME_DRIVER_PATH = "/path/to/chromedriver"  # Replace this

# ✅ Setup Selenium
service = Service(CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # run without opening browser
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=service, options=options)

try:
    # ✅ Open the WPI page
    url = "https://esankhyiki.mospi.gov.in/macroindicators?product=wpi"
    driver.get(url)

    print("🔄 Loading page...")
    time.sleep(5)  # wait for JS to load table

    # ✅ Parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find the table (you may need to inspect and adjust class/id)
    table = soup.find("table")
    if table:
        print("✅ Extracted Table:")
        for row in table.find_all("tr"):
            cells = [cell.text.strip() for cell in row.find_all(["td", "th"])]
            if cells:
                print(cells)
    else:
        print("❌ No table found. Check if page loads properly or change selector.")

finally:
    driver.quit()
