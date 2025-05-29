import pyautogui
import pandas as pd
import time

# Load data from CSV file
data = pd.read_csv("data.csv")  # Replace with your actual file

# Delay to switch to the target application
time.sleep(5)  # Gives you time to open the form

for index, row in data.iterrows():
    pyautogui.write(str(row["Name"]))  # Type Name
    pyautogui.press("tab")  # Move to next field
    pyautogui.write(str(row["Email"]))  # Type Email
    pyautogui.press("tab")
    pyautogui.write(str(row["Phone"]))  # Type Phone
    pyautogui.press("enter")  # Submit form
    time.sleep(2)  # Wait before next entry

print("Data entry completed successfully!")