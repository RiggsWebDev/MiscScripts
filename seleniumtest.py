from selenium import webdriver

option = webdriver.ChromeOptions()
#option.add_argument("-incognito")

browser = webdriver.Chrome(executable_path='C:/chromedriver', options=option)

browser.get("https://docs.google.com/forms/d/e/1FAIpQLSeKcCrTVTHiN2Sgy1inCjFhFl8xhudOWNjdj8ZjsNoUZ1W5lA/viewform")

textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

radiobuttons[-4].click()

textboxes[0].send_keys("Riggs")
textboxes[1].send_keys("Hunter")

radiobuttons[11].click()


#checkboxes[1].click()
#checkboxes[3].click()

#submitbutton[0].click()

#browser.close()