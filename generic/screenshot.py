
from datetime import datetime

def screenshot(driver):
    d = datetime.now().strftime("%d-%m-%Y %H-%M=%S")
    path = r'C:\Users\Dell\PycharmProjects\Hybrid_Framework\screenshots'
    driver.save_screenshot(f"{path}/{d}.png")
    print("screenshot saved successfully...")
