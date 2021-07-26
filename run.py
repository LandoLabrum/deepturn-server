from deepturn.subscriptions import subscriptions

subscriptions = subscriptions()
for sub in subscriptions['customers']:
   print(sub['instagram'])