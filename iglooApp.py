from lib2to3.pgen2 import driver
from appium import webdriver
from selenium.webdriver.common.by import By
import time

# Objt
login_btn = '//android.view.View[@content-desc="Log in"]'
email_form = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'
password_form = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText'
signin_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.widget.Button'
welcoming_text = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.TextView'


# Variable
name = 'Dimas Putra'
email = 'dmpdmpm90@gmail.com'
password = 'Qwerty123@'
welcome = 'Welcome to igloohome'


des_caps = {}

des_caps['appPackage'] = 'com.igloo.home'
des_caps['appActivity'] = 'com.igloo.home.MainActivity'
des_caps['platformName'] = 'Android'
des_caps['deviceName'] = 'vivo 1938'
des_caps['udid'] = '8DHQL77XBADIWGUG'
des_caps['unicodeKeyboard'] = 'true'
des_caps['resetKeyboard'] = 'true'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)

time.sleep(3)

driver.find_element(By.XPATH, login_btn).click()
time.sleep(3)
driver.find_element(By.XPATH, email_form).click()
driver.find_element(By.XPATH, email_form).send_keys(email)
time.sleep(3)
driver.find_element(By.XPATH, password_form).click()
driver.find_element(By.XPATH, password_form).send_keys(password)
driver.find_element(By.XPATH, signin_btn).click()
time.sleep(5)
driver.quit()

# Check dashboard after login
element = driver.find_element(By.XPATH, welcoming_text)
assert element.text == welcome


