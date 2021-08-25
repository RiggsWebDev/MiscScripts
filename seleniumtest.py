#script is now 100% working and can be completely automated - highly recommend setting up with something like Window's task scheduler and using the headless otion
#if you want this to be 100% hands off automated. Personally I'm still testing some ideas and won't be running that setup just yet. 
#
#
#It should however be extremely easy to change some of these values to fit any Google form that needs to be filled out daily for example. 
#
#Instructions on how to do that coming soon. 
#

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

# click on submit button ---- The top one works, just remove the comments to run it. Not sure why the second variant that I was attempting to use first didn't work. 
"""

This actually works

submit = browser.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
submit.click()

"""



############################################################################
# Do not use this one! It does not work, I've left it in to trouble shoot! #
############################################################################
"""

#submitbutton[0].click()

for some reason I can't actually get the above to work. It's the correct class. I'm going to have to really dig into inspect element to find out what's happening here. 
It is nice to have schedled in task manager even without this though, as the form is popped up and filled in automatically, just waiting on my clicking of the submit button. 

"""
#browser.close()
