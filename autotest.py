from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\my_files\codes\sessies\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("file:///C:/my_files/codes/sessies/main.html")
print(driver.find_element(by=By.ID, value="menu").text)
