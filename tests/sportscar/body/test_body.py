
class CarBodyTests:
    def test_function_for_body_test(self,chrome_browser):
        driver = chrome_browser.Chrome(ChromeDriverManager().install())
        driver.get('https://www.google.com')
        assert True
