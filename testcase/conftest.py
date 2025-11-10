from selenium.webdriver import Chrome,ChromeOptions
import pytest
opts = ChromeOptions()
opts.add_experimental_option("detach", True)

url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

@pytest.fixture
def setup():
    driver = Chrome(opts)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
