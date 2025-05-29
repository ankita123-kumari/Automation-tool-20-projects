from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Define Google Form URL
form_url = "https://forms.gle/YOUR_FORM_ID"  # Replace with your Google Form URL

# Set up WebDriver
driver = webdriver.Chrome()
driver.get(form_url)
time.sleep(2)  # Wait for form to load

# Autofill the form fields (modify according to your form structure)
fields = driver.find_elements(By.XPATH, "//input[@type='text']")

# Example: Filling out fields automatically
form_answers = ["Ankita Kumari", "ankita@example.com", "Python Developer"]
for i in range(len(fields)):
    fields[i].send_keys(form_answers[i])

# Submit form
submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
submit_button.click()

time.sleep(2)
driver.quit()
print("Google Form submitted successfully!")