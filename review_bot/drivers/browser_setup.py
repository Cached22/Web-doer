from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from review_bot.config.settings import HEADLESS_BROWSER, PROXY_DETAILS

def initialize_webdriver():
    # Set up Chrome options
    chrome_options = Options()
    if HEADLESS_BROWSER:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")  # This make Chromium reachable
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Add proxy settings if provided
    if PROXY_DETAILS:
        chrome_options.add_argument(f'--proxy-server={PROXY_DETAILS}')

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    return driver
