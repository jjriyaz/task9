import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
paths = r"C:\Users\DELL\Desktop\New folder\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the URL
driver.get("https://www.saucedemo.com/")

# Locate the username and password fields and login button and Enter credentials and log in
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")
time.sleep(2)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")
time.sleep(2)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Wait for the page to load
time.sleep(5)

# Fetch the title and current URL of the webpage
page_title = driver.title
current_url = driver.current_url

# Extract the entire contents of the webpage
page_source = driver.page_source

# Save the extracted content to a text file
with open(r"C:\Users\DELL\Desktop\New folder\selenium task\Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(f"Page Title: {page_title}\n")
    file.write(f"Current URL: {current_url}\n\n")
    file.write("Page Source:\n")
    file.write(page_source)
print(f"Page Title: {page_title}")
print(f"Current URL: {current_url}")