from selenium import webdriver

driver = webdriver.Chrome()

url = 'http://www.baidu.com'

driver.get(url)

text = driver.find_element_by_id('wrapper').text

print(text)