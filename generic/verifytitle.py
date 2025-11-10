
from generic import screenshot
def verify_title(driver, title):
    assert driver.title == title,screenshot(driver)
    print("verified successfully")
    