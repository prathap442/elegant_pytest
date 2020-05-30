import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def chrome_browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    print("after the tear down of the driver")