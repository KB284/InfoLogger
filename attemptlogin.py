import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

driver = webdriver.Chrome()
driver.get('https://www.google.com')

driver.fullscreen_window()

username = os.getenv("Email_Login")
password = os.getenv("PASSWORD")

def search():
    searchbar = driver.find_element(By.NAME, 'q')
    searchbar.send_keys("hackerone")
    searchbar.send_keys(Keys.ENTER)

    search_results = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a/h3')
    search_results.click()

    time.sleep(5)

def login_button():
    login_tab = driver.find_element(By.XPATH, '//*[@id="block-hackerone-topbar"]/ul/li[1]')
    login_tab.click()

    time.sleep(5)

def login_info():
    info = driver.find_element(By.XPATH,
                               '//*[@id="sign_in_email"]')
    info.send_keys(username)
    time.sleep(2)

    passInfo = driver.find_element(By.XPATH, '//*[@id="sign_in_password"]')
    passInfo.send_keys(password)
    time.sleep(2)

    infoLogin = driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div/div/form/div/div/div/div[2]/div/div/div[4]/button')
    infoLogin.click()
    time.sleep(2)

    # Define the expected condition to wait for (e.g., the presence of an element on the next page)
    expected_condition = EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[1]/div/div'))

    # Set the maximum time to wait for the condition to be met
    timeout = 10  # Timeout in seconds

    # Wait for the condition to be met
    wait = WebDriverWait(driver, timeout)
    element = wait.until(expected_condition)

    element.is_displayed()
    time.sleep(5)

def available_bountys():
    # Define the expected condition to wait for (e.g., the presence of the bounty elements)
    expected_condition = EC.presence_of_all_elements_located((By.CLASS_NAME, "relative"))

    # Set the maximum time to wait for the condition to be met
    timeout = 10  # Timeout in seconds

    # Wait for the condition to be met
    wait = WebDriverWait(driver, timeout)
    wait.until(expected_condition)

    # Extract the bounty data
    bounties = driver.find_elements(By.CLASS_NAME, "flex gap-xs")
    print("Number of bounties found:", len(bounties))

    # Process and print the bounty details
    for bounty in bounties:
        title = bounty.find_element(By.CLASS_NAME, "w-0 grow truncate").text
        bounty_type = bounty. find_element(By.TAG_NAME, 'strong')
        reward = bounty.find_element(By.CLASS_NAME, "spec-amount-in-currency").text
        print("Title: ", title)
        print("Bounty: ", bounty_type)
        print("Reward: ", reward)
        print("---------------")

        time.sleep(3)

        print(bounty)

        return bounty


search()
login_button()
login_info()
available_bountys()
