import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 1 opening browser
driver = webdriver.Firefox()
# 2 going to url
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# 10 sec total element loaded in 3 sec.. proceed for next
# Enter UserName
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, "username")))
driver.find_element(By.NAME, "username").send_keys("Admin")
# Enter Password
driver.find_element(By.NAME, "password").send_keys("admin123")
# Click on login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
# Click on menu button
driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
# Click on logout button
driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()


# parallel run
# reports
# Data driven
# hardcode value
# grouping \ selection test cases
# multiple time write same type of code
# time consuming





