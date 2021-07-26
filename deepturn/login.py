import os
from instagrapi import Client
import requests
from dotenv import load_dotenv
from django.http import JsonResponse

SELF_HOST = os.getenv('SELF_HOST')

class Login():
   def __init__(self):
      self.cl = Client()

   def first_login(self, username, password):
      self.cl.login(username, password)
      self.cl.account_info()
      account_info = self.cl.last_json['user']
      account_info['password'] = password
      account_info['id'] = account_info['pk']
      cookies = self.cl.get_settings()
      cookies['account'] = str(account_info['pk'])
      account_info.update({"cookies":cookies})
      return account_info

   def login(self, username, password, cookies=None):
      if cookies != None:
         self.cl.set_settings(cookies)
         self.cl.login(username, password)
         
         # self.cl.account_info()

      # if cookies != False:
      #    print(cookies)
      # else:
      #    self.cl.login(username, password)
      #    cookies = self.cl.get_settings()
      
      
      
      # if os.path.exists(IG_CREDENTIAL_PATH):
      #    self.cl.load_settings(IG_CREDENTIAL_PATH)
      #    self.cl.login(username, password)
      # else:
      #    self.cl.login(username, password)
      #    self.cl.dump_settings(IG_CREDENTIAL_PATH)