from instagrapi import Client
from .tools import write_to_file
from .login import Login


class Customer():
   def __init__(self, username, password):
      self.cl = Login(username, password)



   # def daily_stats(self):
   #    context = {}
   #    self.cl.news_inbox_v1()
   #    account_info = cl.last_json
   #    return account_info

# data = Customer("larzrandana", "1Wasatch!")
# Customer("larzrandana", "1Wasatch!")
# write_to_file("news_inbox_v1", data)
   