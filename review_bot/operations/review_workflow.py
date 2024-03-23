from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from review_bot.config.settings import WEBSITE_URLS
from review_bot.database.account_manager import get_unused_account, mark_account_as_used
from review_bot.drivers.browser_setup import initialize_webdriver
from review_bot.utils.captcha_handling import detect_captcha, solve_captcha
from review_bot.utils.content_generator import generate_review_content
from review_bot.utils.proxy_rotation import rotate_proxy

class ReviewWorkflow:
    def __init__(self, driver):
        self.driver = driver

    def login_to_email(self, account):
        # Assuming the email login page has fields with IDs 'login_email_input' and 'login_password_input'
        self.driver.get("http://email.login.page")
        email_input = self.driver.find_element(By.ID, "login_email_input")
        password_input = self.driver.find_element(By.ID, "login_password_input")
        email_input.send_keys(account['email'])
        password_input.send_keys(account['password'])
        password_input.submit()
        # Wait for login to complete
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "inbox"))
        )

    def navigate_to_website(self, url):
        self.driver.get(url)
        # Wait for the navigation to complete
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def post_review(self, content):
        # Assuming the review page has a textarea with ID 'review_textarea'
        review_textarea = self.driver.find_element(By.ID, "review_textarea")
        review_textarea.send_keys(content)
        # Assuming the review page has a submit button with ID 'submit_review_button'
        submit_review_button = self.driver.find_element(By.ID, "submit_review_button")
        submit_review_button.click()
        # Wait for the review to be posted
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "review_confirmation"))
        )

    def logout(self):
        # Assuming there's a logout button with ID 'logout_button'
        logout_button = self.driver.find_element(By.ID, "logout_button")
        logout_button.click()

def execute_review_workflow():
    driver = initialize_webdriver()
    workflow = ReviewWorkflow(driver)

    for url in WEBSITE_URLS:
        account = get_unused_account()
        if account:
            workflow.login_to_email(account)
            workflow.navigate_to_website(url)
            content = generate_review_content()
            workflow.post_review(content)
            if detect_captcha(driver.page_source):
                captcha_element = driver.find_element(By.ID, "captcha_image")
                solve_captcha(captcha_element)
            workflow.logout()
            mark_account_as_used(account)
            rotate_proxy()

    driver.quit()

if __name__ == "__main__":
    execute_review_workflow()