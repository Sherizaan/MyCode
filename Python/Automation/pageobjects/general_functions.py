import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class GeneralFunctions():

 def __init__(self):
  pass

 def set_driver(self, driver, seconds):
  self.driver = driver
  self.wait = WebDriverWait(self.driver, int(seconds))

 def set_page_timeout(self, seconds):
  self.driver.set_page_load_timeout(int(seconds))
 
 def open_page(self, url):
  try:
   self.driver.get(url)
   return True
  except TimeoutException:
   return False

 def open_new_window(self, url, driver):
  try:
   driver.get(url)
   return True
  except TimeoutException:
   return False

 def load_page(self, compare_text):
  try:
   if self.driver.title.lower() == compare_text.lower():
    return True
   else:
    return False
  except TimeoutException:
   return False

 def load_new_window_page(self, compare_text, driver):
  try:
   if driver.title.lower() == compare_text.lower():
    return True
   else:
    return False
  except TimeoutException:
   return False

 def return_web_element(self, element_name):
  element_details = element_name.split("||")
  try:
   if element_details[0].lower() == "xpath":
    return self.driver.find_element_by_xpath(element_details[1])
   if element_details[0].lower() == "id":
    return self.driver.find_element_by_id(element_details[1])
   if element_details[0].lower() == "name":
    return self.driver.find_element_by_name(element_details[1])
   if element_details[0].lower() == "class":
    return self.driver.find_element_by_class_name(element_details[1])
   if element_details[0].lower() == "css":
    return self.driver.find_element_by_css_selector(element_details[1])
  except NoSuchElementException:
   return None

 def return_web_element_new_page(self, element_name, driver):
  element_details = element_name.split("||")
  try:
   if element_details[0].lower() == "xpath":
    return driver.find_element_by_xpath(element_details[1])
   if element_details[0].lower() == "id":
    return driver.find_element_by_id(element_details[1])
   if element_details[0].lower() == "name":
    return driver.find_element_by_name(element_details[1])
   if element_details[0].lower() == "class":
    return driver.find_element_by_class_name(element_details[1])
   if element_details[0].lower() == "css":
    return driver.find_element_by_css_selector(element_details[1])
  except NoSuchElementException:
   return None

 def enter_text(self, text, input_field):
  element_details = input_field.split("||")
  try:
   if element_details[0].lower() == "xpath":
    self.wait.until(EC.presence_of_element_located((By.XPATH, element_details[1]))).send_keys(text)
    return True
   if element_details[0].lower() == "id":
    self.wait.until(EC.presence_of_element_located((By.ID, element_details[1]))).send_keys(text)
    return True
  except TimeoutException:
   return "Timeout"
  except NoSuchElementException:
   return "No element"

 def enter_text_new_page(self, text, input_field, wait):
  element_details = input_field.split("||")
  try:
   if element_details[0].lower() == "xpath":
    wait.until(EC.presence_of_element_located((By.XPATH, element_details[1]))).send_keys(text)
    return True
   if element_details[0].lower() == "id":
    wait.until(EC.presence_of_element_located((By.ID, element_details[1]))).send_keys(text)
    return True
  except TimeoutException:
   return "Timeout"
  except NoSuchElementException:
   return "No element"

 def click_element(self, element_name):
  element_details = element_name.split("||")
  try:
   if element_details[0].lower() == "xpath":
    self.wait.until(EC.element_to_be_clickable((By.XPATH, element_details[1]))).click()
    return True
   if element_details[0].lower() == "id":
    self.wait.until(EC.element_to_be_clickable((By.ID, element_details[1]))).click()
    return True
   if element_details[0].lower() == "css_selector":
    self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_details[1]))).click()
    return True
  except TimeoutException:
   return "Timeout"
  except NoSuchElementException:
   return "No element"

 def click_element_new_page(self, element_name, wait):
  element_details = element_name.split("||")
  try:
   if element_details[0].lower() == "xpath":
    wait.until(EC.element_to_be_clickable((By.XPATH, element_details[1]))).click()
    return True
   if element_details[0].lower() == "id":
    wait.until(EC.element_to_be_clickable((By.ID, element_details[1]))).click()
    return True
   if element_details[0].lower() == "css_selector":
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_details[1]))).click()
    return True
  except TimeoutException:
   return "Timeout"
  except NoSuchElementException:
   return "No element"

 def check_if_exists(self, element_name):
  element_details = element_name.split("||")
  try:
   if element_details[0].lower() == "xpath":
    self.wait.until(EC.presence_of_element_located((By.XPATH, element_details[1])))
    return True
   if element_details[0].lower() == "id":
    self.wait.until(EC.presence_of_element_located((By.ID, element_details[1])))
    return True
  except TimeoutException:
   return "Timeout"
  except NoSuchElementException:
   return "No element"

 def check_if_exists_on_new_window_page(self, element_name, wait):
  element_details = element_name.split("||")
  try:
   if element_details[0].lower() == "xpath":
    wait.until(EC.presence_of_element_located((By.XPATH, element_details[1])))
    return True
   if element_details[0].lower() == "id":
    wait.until(EC.presence_of_element_located((By.ID, element_details[1])))
    return True
  except TimeoutException:
   return "Timeout"
  except NoSuchElementException:
   return "No element"

 def wait_until_visible(self, element_name):
  element_details = element_name.split("||")
  try:
   if element_details[0].lower() == "xpath":
    self.wait.until(EC.presence_of_element_located((By.XPATH, element_details[1])))
    return True
   if element_details[0].lower() == "id":
    self.wait.until(EC.presence_of_element_located((By.ID, element_details[1])))
    return True
  except TimeoutException:
   return "Timeout"
  except NoSuchElementException:
   return "No element"

 def wait_until_invisible(self, element_name):
  element_details = element_name.split("||")
  try:
   if element_details[0].lower() == "xpath":
    self.wait.until(EC.invisibility_of_element_located((By.XPATH, element_details[1])))
    return True
   if element_details[0].lower() == "id":
    self.wait.until(EC.invisibility_of_element_located((By.ID, element_details[1])))
    return True
  except TimeoutException:
   return "Timeout"
  except NoSuchElementException:
   return "No element"

 def email_error_log(self, text):
  if os.path.exists(os.getcwd() + "/email/email_message.txt"):
   with open(os.getcwd() + "/email/email_message.txt", "a") as message_body:
    message_body.write("\n{}".format(text))
  else:
   with open(os.getcwd() + "/email/email_message.txt", "w") as message_body:
    message_body.write(text)

 def email_e_tender_record_amount(self, category, text):
  if os.path.exists(os.getcwd() + "/email/email_e_tender_records.txt"):
   with open(os.getcwd() + "/email/email_e_tender_records.txt", "a") as message_body:
    message_body.write("\n{}: {}".format(category, text))
  else:
   with open(os.getcwd() + "/email/email_e_tender_records.txt", "w") as message_body:
    message_body.write("{}: {}".format(category, text))

 def email_sa_tender_record_amount(self, keyword, text):
  if os.path.exists(os.getcwd() + "/email/email_sa_tender_records.txt"):
   with open(os.getcwd() + "/email/email_sa_tender_records.txt", "a") as message_body:
    message_body.write("\n{}: {}".format(keyword, text))
  else:
   with open(os.getcwd() + "/email/email_sa_tender_records.txt", "w") as message_body:
    message_body.write("{}: {}".format(keyword, text))

 def return_page_object(self, page_object):
  if page_object.lower().strip() == "sa-tenders":
   return SA_TendersHomePage()
  if page_object.lower().strip() == "sa-tenders results":
   return SA_TendersResultsPage()

from pageobjects.sa_tenders_home_page import SA_TendersHomePage
from pageobjects.sa_tenders_results_page import SA_TendersResultsPage