import os
import stripe
import requests
import time
from dotenv import load_dotenv
load_dotenv()

HEROKU_HOST = os.getenv('HEROKU_HOST')

def subscriptions():
   """
   returns JSON {'subscription','ig_id','username','password'} 
   """
   stripe.api_key = os.getenv('STRIPE_PUBLIC_KEY')
   customers = requests.get(HEROKU_HOST+"/middleware/current").json()
   context = {
      "timestamp": int(time.time()),
      "customers": []
      }
   for customer in customers:
      stripe_id = customer['stripe_id']
      if stripe_id != None:
         stripe_customer = stripe.Customer.retrieve(stripe_id)
         subscriptions = stripe_customer.subscriptions.data
         if subscriptions != []:
               for sub in stripe_customer.subscriptions.data:
                  context['customers'].append(
                     {
                        'subscription': sub.id,
                        'instagram': customer['instagram'],
                        'username': customer['username'],
                     }
                  )
   return context