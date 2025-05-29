import pyautogui
import time

def take_screenshot():
    """Capture and save a screenshot automatically."""
    timestamp = time.strftime("%Y%m%d_%H%M%S")  # Generate unique filename
    filename = f"screenshot_{timestamp}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Screenshot saved as {filename}")

# Example Usage
take_screenshot()