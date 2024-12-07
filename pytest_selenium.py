import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Test for logging into Google
@pytest.fixture(scope="module")
def browser():
    # Set up the WebDriver
    driver = webdriver.Chrome()  # You can replace with your WebDriver if needed
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_google_login(browser):
    # Open the Google login page
    browser.get("https://accounts.google.com/")

    # Enter email
    email_input = browser.find_element(By.ID, "identifierId")
    email_input.send_keys("your_email@gmail.com")  # Replace with your email
    email_input.send_keys(Keys.RETURN)

    # Wait for password field to appear
    time.sleep(2)

    # Enter password
    password_input = browser.find_element(By.NAME, "password")
    password_input.send_keys("your_password")  # Replace with your password
    password_input.send_keys(Keys.RETURN)

    # Wait for a while to ensure login has completed
    time.sleep(5)

    # Verify login by checking if the Google account page loads
    assert "Google Account" in browser.title, "Login failed!"


if __name__ == "__main__":
    pytest.main(["-v", "-s"])
