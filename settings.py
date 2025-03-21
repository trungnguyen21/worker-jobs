from dotenv import load_dotenv
import os

load_dotenv()

# Account Info
USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASSWORD = os.environ.get("USER_PASSWORD")

# Say you want an appointment no later than Mar 14, 2024
# Please strictly follow the YYYY-MM-DD format
EARLIEST_ACCEPTABLE_DATE = "2025-03-23"
LATEST_ACCEPTABLE_DATE = "2025-12-31"

# The following is only required for the Gmail notification feature
# Gmail login info
GMAIL_SENDER_NAME = os.environ.get("GMAIL_SENDER_NAME")
GMAIL_EMAIL = os.environ.get("GMAIL_EMAIL")
GMAIL_APPLICATION_PWD = os.environ.get("GMAIL_APPLICATION_PWD")

# Email notification receiver info
RECEIVER_NAME = os.environ.get("RECEIVER_NAME")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")

# Override with local, for developers
# from local import *

# See the automation in action
SHOW_GUI = False  # toggle to false if you don't want to see the browser

# If you just want to see the program run WITHOUT clicking the confirm reschedule button
# For testing, also set a date really far away so the app actually tries to reschedule
TEST_MODE = False

SELENIUM_PATH = os.environ.get("SELENIUM_PATH")

# Don't change the following unless you know what you are doing
DEPLOYMENT = os.environ.get("DEPLOYMENT", False)
# CHROME_DRIVER_PATH = "/usr/local/bin/chromedriver"
CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
DETACH = True
NEW_SESSION_AFTER_FAILURES = 5
NEW_SESSION_DELAY = 60 * 15
TIMEOUT = 10
FAIL_RETRY_DELAY = 30
DATE_REQUEST_DELAY = 30
DATE_REQUEST_MAX_RETRY = 60
DATE_REQUEST_MAX_TIME = 30 * 60
LOGIN_URL = "https://ais.usvisa-info.com/en-ca/niv/users/sign_in"
# This is hardcoded to the Toronto consulate, might need to change for other consulates
AVAILABLE_DATE_REQUEST_SUFFIX = "/days/95.json?appointments[expedite]=false"
APPOINTMENT_PAGE_URL = "https://ais.usvisa-info.com/en-ca/niv/schedule/{id}/appointment"
PAYMENT_PAGE_URL = "https://ais.usvisa-info.com/en-ca/niv/schedule/{id}/payment"
REQUEST_HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
}
