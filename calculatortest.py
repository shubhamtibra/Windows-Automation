#******************************************************************************
#
# Copyright (c) 2016 Microsoft Corporation. All rights reserved.
#
# This code is licensed under the MIT License (MIT).
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#******************************************************************************



from appium import webdriver
import time
import json

#set up appium
desired_caps = {}
# desired_caps["app"] = "C:\Users\I558624\AppData\Local\Microsoft\Teams\Update.exe"
# desired_caps["appArguments"] = '--processStart "Teams.exe"'
# desired_caps["appWorkingDir"] = "C:\Users\I558624\AppData\Local\Microsoft\Teams"
desired_caps["app"] = "Root"
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723',
    desired_capabilities= desired_caps)

start = driver.find_element_by_name("Start")
start.click()
time.sleep(1)
# teams = driver.find_elements_by_name("Microsoft Teams")
# start.click()
# time.sleep(1)

# for i in range(len(teams)):
#     try:
#         start = driver.find_element_by_name("Start")
#         start.click()
#         time.sleep(1)
#         team = driver.find_elements_by_name("Microsoft Teams")[i]
#         team.click()
#         start.click()
#         time.sleep(1)
#     except Exception as e:
#         print (e)
#         pass

# start = driver.find_elements(by="xpath", value="/Pane/Pane[1]/Button[1]")
# start.click()
# time.sleep(1)
# team = driver.find_elements_by_name("Microsoft Teams")[1]
# team.click()
team = driver.find_element_by_accessibility_id("W~com.squirrel.Teams.Teams")
team.click()
time.sleep(4)
profile = driver.find_element_by_accessibility_id("personDropdown")
profile.click()
status = driver.find_element_by_accessibility_id("settings-dropdown-update-status-button")
status.click()
oof = driver.find_element_by_accessibility_id("-1875434576")
oof.click()


# ar = driver.find_elements_by_name("Turn on automatic replies")[0]
# ar.click()
# save = driver.find_elements_by_name("Save")[0]
# save.click()
res = driver.find_elements(by="xpath", value="//*")
ans = [[o.text, o.tag_name] for o in res]
with open('team.json', 'w') as f:
    json.dump(ans, f)

# # displaytext = driver.find_element_by_accessibility_id("CalculatorResults").text
# # displaytext = displaytext.strip("Display is " )
# # displaytext = displaytext.rstrip(' ')
# # displaytext = displaytext.lstrip(' ')
# # return displaytext



# # elementsList = driver.find_elements(by="xpath", value="//*")
# # driver.find_element_by_name("Clear").click()
# # driver.find_element_by_name("Seven").click()
# # assertEqual(getresults(),"7")
# # driver.find_element_by_name("Clear").click()


# # driver.find_element_by_name("One").click()
# # driver.find_element_by_name("Plus").click()
# # driver.find_element_by_name("Seven").click()
# # driver.find_element_by_name("Equals").click()
# # assertEqual(getresults(),"8")

# driver.quit()

