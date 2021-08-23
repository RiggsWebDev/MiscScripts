from selenium import webdriver

option = webdriver.ChromeOptions()
#option.add_argument("-incognito")

browser = webdriver.Chrome(executable_path='C:/chromedriver', options=option)

browser.get(" GENERIC DAILY RESPONSE FORM - redacted to keep specific forum anonymous")

textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

radiobuttons[-4].click()

textboxes[0].send_keys("Last Name")
textboxes[1].send_keys("First Name")

radiobuttons[11].click()


#checkboxes[1].click()
#checkboxes[3].click()

#submitbutton[0].click()

#browser.close()
