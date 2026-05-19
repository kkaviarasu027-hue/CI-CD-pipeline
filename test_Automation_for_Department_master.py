import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_department_master(driver):

    wait = WebDriverWait(driver, 20)

    # ================= LOGIN =================
    driver.get("https://tranquil-truffle-2a8000.netlify.app/")

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[contains(@placeholder,'admin')]")
    )).send_keys("Kalpana@yopmail.com")

    driver.find_element(By.XPATH, "//input[@placeholder='Enter password']").send_keys("Kal@2026")

    driver.find_element(By.ID, "stayLoggedIn").click()

    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # ================= NAVIGATION =================
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@class,'cm-menu-item')]//*[name()='svg']")
    )).click()

    time.sleep(2)

    dept = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[normalize-space()='Department Master']")
    ))
    driver.execute_script("arguments[0].click();", dept)

    # ================= CREATE DEPARTMENT =================
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Create Department']")
    )).click()

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter Department Code']")
    )).send_keys("DPT001")

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter Department Name']")
    )).send_keys("Computer Science")

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter Department Number']")
    )).send_keys("101")

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@value='Active']")
    )).click()

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Save']")
    )).click()

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Yes']")
    )).click()

    time.sleep(2)

    ok = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='OK' or normalize-space()='Ok']")
    ))
    driver.execute_script("arguments[0].click();", ok)

    # ================= CLICK EDIT =================
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[8]//div[6]//div[1]//button[1]")
    )).click()

    # ================= ENTER DETAILS =================
    code = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter Department Code']")
    ))
    code.clear()
    code.send_keys("DPT003")

    name = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter Department Name']")
    ))
    name.clear()
    name.send_keys("Civil Engineering")

    number = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter Department Number']")
    ))
    number.clear()
    number.send_keys("303")

    # ================= SELECT INACTIVE =================
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@value='Inactive']")
    )).click()

    # ================= CLICK DELETE =================
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Delete']")
    )).click()

    # ================= CONFIRM YES =================
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Yes']")
    )).click()

    # ================= FINAL OK =================
    ok_btn = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='OK' or normalize-space()='Ok']")
    ))
    driver.execute_script("arguments[0].click();", ok_btn)