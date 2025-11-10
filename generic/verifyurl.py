
from generic.screenshot import screenshot

def verify_url(driver,url):
    assert driver.current_url == url, screenshot(driver)
    print("verified successfully")
