from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/gowtham/Downloads/chromedriver/chromedriver_linux64(1)/chromedriver")
driver.get("http:www.google.com")

print(driver.title)