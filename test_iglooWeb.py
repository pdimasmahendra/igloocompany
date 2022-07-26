from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Object
organization_form = 'inputCompanyIDLogin'
email_form = 'inputUsernameLogin'
password_form = 'inputPasswordLogin'
login_btn = 'loginButton'
qainterview_lb = '//*[@id="sideBarCustomMenu"]/div[3]/div[3]/div[1]'
owner_lb = '//*[@id="sideBarCustomMenu"]/div[3]/div[3]/div[2]'
dept_sidebar = '//*[@id="sideBarCustomMenu"]/div[5]/div[3]'
addDept_btn = 'buttonAddDepartmentList'
deptName_form = 'inputNameCreateDepartment'
next_btn = 'buttonNext1CreateDepartment'
skip_btn = 'buttonNext2CreateDepartment'
save_btn = 'buttonSaveCreateDepartment'
deptName_tb = '//*[@id="departmentListActive"]/div[2]/table/tbody/tr[1]/td[1]/p'
numbermng_tb = '//*[@id="departmentListActive"]/div[2]/table/tbody/tr[3]/td[3]'
status_lb = '//*[@id="departmentListActive"]/div[2]/table/tbody/tr[3]/td[4]'
editDept_btn = 'buttonEditDepartmentPage'
editName_form = 'inputNameEditDepartment'
saveEdit_btn = 'buttonSaveEditDepartment'
deptName_lb = '//*[@id="titleHeaderStickyDepartmentPageContent"]/div/div[2]/div[1]/div'


# Variable
baseUrl = 'http://igloohome-offline-dashboard-dev.s3-website-ap-southeast-1.amazonaws.com/login'
organization = 'qainterview'
email = 'igloohomebali.lockuser@gmail.com'
password = 'igloohome'
deptname = 'Test 7'
deptname_ed = 'Test Tujuh'
numbermng = '1'
status = 'Active'


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(baseUrl)
    driver.maximize_window()
    yield driver
    driver.quit()

# User should be able to login to iglooworks dashboard
def test_login(driver):
    driver.implicitly_wait(time_to_wait=30)
    driver.find_element(By.ID, organization_form).send_keys(organization)
    driver.find_element(By.ID, email_form).send_keys(email)
    driver.find_element(By.ID, password_form).send_keys(password)
    driver.find_element(By.ID, login_btn).click()
    time.sleep(10)
    
    # Check Dashboard Page after Login Success
    element = driver.find_element(By.XPATH, qainterview_lb)
    assert element.text == 'QA interview'
    element = driver.find_element(By.XPATH, owner_lb)
    assert element.text == 'Owner'
    
# User should be able to Add Department on iglooworks dashboard
def test_ManageDepartement(driver):
    driver.implicitly_wait(time_to_wait=30)
    driver.find_element(By.ID, organization_form).send_keys(organization)
    driver.find_element(By.ID, email_form).send_keys(email)
    driver.find_element(By.ID, password_form).send_keys(password)
    driver.find_element(By.ID, login_btn).click()
    time.sleep(10)
    driver.find_element(By.XPATH, dept_sidebar).click()
    time.sleep(2)
    driver.find_element(By.ID, addDept_btn).click()
    driver.find_element(By.ID, deptName_form).send_keys(deptname)
    driver.find_element(By.ID, next_btn).click()
    driver.find_element(By.ID, skip_btn).click()
    driver.find_element(By.ID, save_btn).click()
    time.sleep(5)
    
     # Check Table after add Departement
    element = driver.find_element(By.XPATH, deptName_tb)
    assert element.text == deptname
    element = driver.find_element(By.XPATH, numbermng_tb)
    assert element.text == numbermng
    element = driver.find_element(By.XPATH, status_lb)
    assert element.text == status
    
    # Edit Departement
    driver.find_element(By.XPATH, deptName_tb).click()
    driver.find_element(By.ID, editDept_btn).click()
    driver.find_element(By.ID, editName_form).clear()
    driver.find_element(By.ID, editName_form).send_keys(deptname_ed)
    driver.find_element(By.ID, saveEdit_btn).click()
    time.sleep(5)
    
    # Check Table after edit Departement
    element = driver.find_element(By.XPATH, deptName_lb)
    assert element.text == deptname_ed
    
    
    
    
    
    
    
    
    
                    

        
        
