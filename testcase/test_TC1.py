from POM.loginpage import LoginPage
from generic.verifytitle import verify_title
from generic.verifyurl import verify_url
from time import sleep
from generic import XLUtils
import  pytest
path =r'C:\Users\Dell\PycharmProjects\Hybrid_Framework\excel_files\locators.xlsx'
data = XLUtils.read_data(path, "data")

@pytest.mark.parametrize("un,pwd",data.items())
def test_TC1(setup,un,pwd):
    driver = setup
    #verify_title(driver,"OrangeHRM")
    verify_url(driver,"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_obj = LoginPage(driver)
    login_obj.username_textfield(un)
    login_obj.password_textfield(pwd)
    login_obj.login_button()
    sleep(10)
    #verify_title(driver, "OrangeHRM")
    verify_url(driver,"https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

