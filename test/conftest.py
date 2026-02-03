import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="module")
def shared_driver():
    appium_server_url = "http://localhost:4723"
    capabilities = {
        "platformName": "Android",            
        "platformVersion": "14.0",            
        "deviceName": "Pixel 9 Pro API 35",        
        "browserName": "Chrome",              
        "automationName": "UiAutomator2",     
        "udid": "emulator-5554"
    }
    options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(command_executor=appium_server_url, options=options)
    
    yield driver 
    driver.quit()