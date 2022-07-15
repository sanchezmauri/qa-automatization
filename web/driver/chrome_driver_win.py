from selenium import webdriver


class ChromeDriverWin:
    def test(self):
        driver = webdriver.Chrome(executable_path="C:/Users/PC/source/repos/driver/chromedriver.exe")
        driver.get("http://www.ole.com.ar")

