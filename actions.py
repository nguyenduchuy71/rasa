# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted
from selenium import webdriver

class action_get_luong(Action):
    def name(self):
        return 'action_get_luong'
    def run(self,dispatcher, tracker, domain):
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        driver=webdriver.Chrome(executable_path='./drivers/chromedriver',options=op)
        driver.get('https://vncoder.vn/tin-tuc/chia-se/tim-hieu-muc-luong-vi-tri-khoa-hoc-may-tinh')
        x=driver.find_elements_by_css_selector('.bk-lesson-content >p')
        imgs = driver.find_elements_by_css_selector('.bk-lesson-content >p> img')
        img=imgs[0]
        src = img.get_attribute('src')
        dispatcher.utter_message(x[11].text)
        dispatcher.utter_message(image=str(src))
        return []

class action_unclear(Action):
    def name(self):
        return 'action_unclear'
    def run(self,dispatcher, tracker, domain):
        dispatcher.utter_message('Mình không hiểu ý của bạn là gì? Vui lòng nhập lại')
        return []