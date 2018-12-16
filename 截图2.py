from PIL import Image
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.hongkunjinfu.com/')
driver.save_screenshot('金服.png')
left = driver.find_element_by_xpath("html/body/div[2]/div[2]/div/ul/li[1]/a").location['x']
top = driver.find_element_by_xpath("html/body/div[2]/div[1]/div[1]/div/ul[1]/li[3]/a").location['y']
right = driver.find_element_by_xpath("html/body/div[2]/div[2]/div/ul/li[6]/a").location['x'] + driver.find_element_by_xpath("html/body/div[2]/div[2]/div/ul/li[6]/a").size['width']
bottom = driver.find_element_by_xpath(".//*[@id='___szfw_logo___']").location['y'] + driver.find_element_by_xpath(".//*[@id='___szfw_logo___']").size['height']
im = Image.open('金服.png')
im = im.crop((left, top, right, bottom))
im.save('金服1.png')

