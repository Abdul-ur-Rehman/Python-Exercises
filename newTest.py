import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

#obj = Service(r"C:\Users\sg\Downloads\edgedriver_win64\msedgedriver.exe")
#driver1 = webdriver.Edge(service = obj)
#driver1.get("https://lightnines.com")

driver = webdriver.Chrome()
driver.get("https://lightnines.com")


driver.maximize_window()
print(driver.title)
print(driver.browser)
#driver1.maximize_window()

#time.sleep()
