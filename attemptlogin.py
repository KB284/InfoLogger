import os
import time
from dotenv import load_dotenv
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

load_dotenv()

## Example Proxy
PROXY = "207.188.73.155:80"

## Set Chrome Options
options = uc.ChromeOptions()
options.add_argument(f'--proxy-server={PROXY}')

driver = uc.Chrome(options= options)
driver.get('https://www.google.com')

driver.maximize_window()
time.sleep(5)

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

    verify = driver.find_element(By.XPATH, '//*[@id="challenge-stage"]/div/label/input')
    verify.click()

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


    time.sleep(5)


def available_bountys():
    # Create a Chrome WebDriver with headless option
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the HackerOne Opportunities page
    driver.get("https://hackerone.com/opportunities/all")

    # Wait for the JavaScript to dynamically load the content
    wait = WebDriverWait(driver, 10)
    #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".program-table__row")))

    # Create a Beautiful Soup object from the page source
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find the bounty elements and extract the information
    bounties = soup.select(".program-table__row")

    for bounty in bounties:
        company_name = bounty.select_one(".program-table__name").text.strip()
        bounty_amount = bounty.select_one(".program-table__reward").text.strip()
        bounty_type = bounty.select_one(".program-table__type").text.strip()

        print("Company Name:", company_name)
        print("Bounty Amount:", bounty_amount)
        print("Bounty Type:", bounty_type)
        print("----------------")


search()
login_button()
login_info()
available_bountys()
