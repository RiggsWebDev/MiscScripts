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
"""

#submitbutton[0].click()

for some reason I can't actually get the above to work. It's the correct class. I'm going to have to really dig into inspect element to find out what's happening here. 
It is nice to have schedled in task manager even without this though, as the form is popped up and filled in automatically, just waiting on my clicking of the submit button. 

"""
#browser.close()
