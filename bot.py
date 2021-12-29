# imports
import time
import json
import names
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Bot Class
class Bot():
  # This method setups driver
  def setup(self):
    # Service definition to work on all OS(ms,linux)
    s = Service("C:/Users/User/Desktop/aocop/geckodriver.exe")
    self.driver = webdriver.Firefox(service=s)
  
  # This method kills the driver
  def teardown(self):
    self.driver.quit()
  
  # This method makes the bots implementation
  def test(self):
    # variables
    json_file = "C:/Users/User/Desktop/aocop/adventofcyber3.json"
    room = "adventofcyber3"
      
    # infinite loop
    while (True):
        # get and set random user agent from user-agents.txt
        agent = random.choice(open("user-agents.txt","r").readline() )
        header_with_agent = {
            "User-Agent":agent
        }
        
        # setup browser
        self.setup()
        
        # unique random usernames
        name = names.get_full_name()
        name = name.lower()
        name = name.replace(" ", "") + str(random.randint(10000,100000))
        
        email = names.get_full_name()
        email = email.lower()
        email = email.replace(" ", "") + str(random.randint(10000,100000))
        
        password = names.get_full_name()
        password = email.replace(" ", "") + str(random.randint(10000,100000))
        
        # open the website, fill the text field, and register
        self.driver.get("https://tryhackme.com")
        self.driver.find_element(By.XPATH, "/html/body/div[3]/section/div/div[1]/div[1]/button")
        self.driver.find_element(By.CSS_SELECTOR, ".short-signup > .btn").click()
        self.driver.find_element(By.ID, "signup-username").click()
        self.driver.find_element(By.ID, "signup-username").send_keys( name)
        self.driver.find_element(By.ID, "signup-email").click()
        self.driver.find_element(By.ID, "signup-email").send_keys( email + "@gmail.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys( password)
        time.sleep(1)
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
        # Wait for the recaptcha to be resolved.
        time.sleep(25)
        self.driver.switch_to.default_content()
        # end the registration process.
        self.driver.find_element(By.XPATH, "//*[@id='passSubmitBtn']").click()
        time.sleep(1)
        # get the cookie and close the tab
        cookie = self.driver.get_cookies()
        self.driver.close()
        
        # create new session for requests
        s = requests.Session()
        
        # save unique username and password in a google form
        formUrl = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfUP9zCVH4D9fHIpGanaMyqOpHXG4vT3aPcqJq_zmB1GkZrzA/formResponse"
        entry = "entry.571824264=" + name + "&entry.2107058782=" + password
        requests.post(formUrl, params = entry)
        
        # for loop for creating cookie obj to session
        for rn in range(0,len(cookie)):
            cookie_obj = requests.cookies.create_cookie(domain=cookie[rn]['domain'],name=cookie[rn]['name'],value=cookie[rn]['value'])
            s.cookies.set_cookie(cookie_obj)
        
        # get csrf
        get_cookie = s.get('https://tryhackme.com/room/' + room, headers=header_with_agent)
        source = BeautifulSoup(get_cookie.content,"html.parser")
        csrf_token = source.find("input",attrs={"name":"_csrf"})
        
        # set csrf
        header_with_csrf = {
            "User-Agent":agent,
            "csrf-token": csrf_token['value']
        }
        
        # load json file of answers
        data = json.load(open(json_file, encoding="utf8"))
        dict_json=json.loads( json.dumps(data))
        data_length = len(dict_json['data'])
        
        # loop for tasks
        for data_index in range(0, data_length):
            taks_length = len(dict_json['data'][data_index]['tasksInfo'])
            # loop for answers
            for task_index in range(0, taks_length):
                taskNo = dict_json['data'][data_index]['taskNo']
                questionNo = dict_json['data'][data_index]['tasksInfo'][task_index]['questionNo']
                answer = dict_json['data'][data_index]['tasksInfo'][task_index]['submission']
                # get the content and fill the questions
                s.get("https://tryhackme.com/jr/" + room, headers=header_with_agent)
                response = s.post("https://tryhackme.com/api/" + room + "/answer", data={"answer":answer,"questionNo":questionNo,"taskNo":taskNo}, headers=header_with_csrf, verify=False)
                # report the response to check if it works
                print(response.text)
                # sleep to avoid being caught by cloudflare
                time.sleep(2.2)

# main test
bot = Bot()
bot.test()
bot.teardown()
