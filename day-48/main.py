from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.python.org/")
events_list = browser.find_elements_by_css_selector(".event-widget li")
events = {}

for n in range(len(events_list)):
    pieces = events_list[n].text.split("\n")
    events[n] = {"time": pieces[0], "name": pieces[1]}
print(events)