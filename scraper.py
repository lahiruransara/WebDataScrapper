from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# # Paths
firstNameBoxPath = '//*[@id="Times_TimesSearchDetail_Index_Div-1-FirstName"]'
lastNameBoxPath = '//*[@id="Times_TimesSearchDetail_Index_Div-1-LastName"]'
findTimesButtonPath = '//*[@id="Times_TimesSearchDetail_Index_Div-1-Search"]'
downloadButtonPath = '/html/body/div[1]/div[6]/div[12]/div[2]/div[2]/a'

# # Name Arrays
firstName = ["Bjorn","Adam"]
lastName = ["Seeliger","Chaney"]

# # Selenium Webdriver
wd = webdriver.Chrome()
wd.get('https://www.usaswimming.org/times/individual-times-search')

# # WhileLoop
i = 0

while i < len(firstName):
  # go to usa swimming and fill in the query stuff
  firstNameBox = wd.find_element_by_xpath(firstNameBoxPath)
  lastNameBox = wd.find_element_by_xpath(lastNameBoxPath)
  firstNameBox.clear()
  lastNameBox.clear()
  firstNameBox.send_keys(firstName[i])
  lastNameBox.send_keys(lastName[i])
  
  # # click find times button
  findTimesButton = wd.find_element_by_xpath(findTimesButtonPath)
  findTimesButton.click()
  time.sleep(5)  # downloadButtonPath eka waradi kiyala error enawa nm sleep time eka wadi karanna.
  
  # # click download button
  dowloadButton = wd.find_element_by_xpath(downloadButtonPath)
  dowloadButton.click()

  print("Iteration No:", i)
  i += 1

wd.close()
wd.quit()
print ('All Done!')