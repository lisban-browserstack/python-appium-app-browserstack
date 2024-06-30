from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
options = UiAutomator2Options().load_capabilities({
    # Specify device and os_version for testing
    "platformName" : "android",
    "platformVersion" : "9.0",
    "deviceName" : "Google Pixel 3"

    # Add your caps here
})

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

# Test case for the BrowserStack sample Android app.
# If you have uploaded your app, update the test case here.
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="12")
el1.click()
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="filter-btn")
el2.click()
el3 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Samsung\")")
el3.click()
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"High to Low\")")
el4.click()
driver.execute_script('mobile: pressKey', {"keycode": 4})
el5 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Add to cart\")")
el5.click()
el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"\")")
el6.click()
el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"CHECKOUT\")")
el7.click()
el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Accepted usernames are\")")
el8.click()
el9 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"demouser\")")
el9.click()
el10 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Password for all users\")")
el10.click()
el11 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"testingisfun99\")")
el11.click()
el12 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Sign in\")")
el12.click()
el13 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="firstNameInput")
el13.send_keys("lisban")
el14 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="lastNameInput")
el14.click()
el14.send_keys("gonsalves")
el15 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="addressInput")
el15.click()
el15.send_keys("mumbai")
el16 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="stateInput")
el16.click()
el16.send_keys("maharashtra")
driver.execute_script('mobile: pressKey', {"keycode": 4})
el17 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="postalCodeInput")
el17.click()
el17.send_keys("401206")
driver.execute_script('mobile: pressKey', {"keycode": 4})
el18 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"SUBMIT\")")
el18.click()
el19 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"SUBMIT\")")
el19.click()
# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
