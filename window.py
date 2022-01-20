
from appium import webdriver
import time
import json

#set up appium
desired_caps = {}
desired_caps["appTopLevelWindow"] = "0x20534"
teams = webdriver.Remote(
    command_executor='http://127.0.0.1:4723',
    desired_capabilities= desired_caps)

# start = teams.find_element_by_name("Start")
# start.click()
# time.sleep(1)
# teams = driver.find_elements_by_name("Microsoft Teams")
# start.click()
# time.sleep(1)
child = teams.find_element_by_accessibility_id("2030974912")
profile = child.find_element_by_accessibility_id("personDropdown")
profile.focus()
status = child.find_element_by_accessibility_id("settings-dropdown-update-status-button")
status.click()



# ar = driver.find_elements_by_name("Turn on automatic replies")[0]
# ar.click()
# save = driver.find_elements_by_name("Save")[0]
# save.click()
res = teams.find_elements(by="xpath", value="//*")
ans = [[o.text, o.tag_name] for o in res]
with open('team.json', 'w') as f:
    json.dump(ans, f)

