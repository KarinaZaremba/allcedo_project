from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('C:\\Users\\rem6o\\Desktop\\Python\\chromedriver\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = "https://www.google.com/"
driver.get(url)
get_url = driver.current_url
print(get_url)
