from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Click link
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
linkElem.click()

# Enter text
browser.get('htttps://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('notmyrealemail@fake.com')
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('12345')
passwordElem.submit()

# Scroll with keys
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')         # General web page
htmlElem.send_keys(Keys.END)        # scrolls to bottom
htmlElem.send_keys(Keys.HOME)       # scrolls to top

# Elements that use the CSS class 
browser.find_element_by_class_name(name)
browser.find_elements_by_class_name(name)  
# Elements that match the CSS selector
browser.find_element_by_css_selector(selector)
browser.find_elements_by_css_selector(selector)
# Elements with a matching id attri-bute value
browser.find_element_by_id(id)
browser.find_elements_by_id(id)
# <a> elements that completely match the text provided
browser.find_element_by_link_text(text)
browser.find_elements_by_link_text(text)
# <a> elements that contain the text provided
browser.find_element_by_partial_link_text(text)
browser.find_elements_by_partial_link_text(text)
# Elements with a matching name attribute value
browser.find_element_by_name(name)
browser.find_elements_by_name(name)
# Elements with a matching tag name (case insensitive; an <a> element is matched by 'a' and 'A' )
browser.find_element_by_tag_name(name)
browser.find_elements_by_tag_name(name)
# Browser Buttons
browser.back()
browser.forward()
browser.refresh()
browser.quit() 