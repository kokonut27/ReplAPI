import requests, os, json
# from bs4 import BeautifulSoup


'''
  response = requests.get(f"https://replit.com/@{owner}/", headers = {"User-Agent": "Mozilla/2.0"})
  soup = BeautifulSoup(response.text, 'html.parser')

  cont = response.json()
  print(cont)
'''


def replit_user():
  try:
    owner = os.environ['REPL_OWNER']
    return owner
  except:
    exit("ERROR: No such replit account exists!")
    #in this case, you will probably never have this error, because you will be able to view it, but just in case.

def replit_cycles(name = None):
  if name == None:
    print("ERROR: You didn't fill out the name parameter!")
  else:
    try:
      apilink = 'https://replit-user-api.pyer.repl.co/get?user=' + name#lots of thanks to @pyer
      api = requests.get(apilink)
      data = eval(api.text)
      sun = data['cycles']
      return sun
    except:
      print("ERROR: Cannot find " + name + "'s cycles.")

def replit_langs(name = None):
  if name == None:
    print("ERROR: You didn't fill out the name parameter!")
  else:
    try:
      apilink = 'thttps://replit-user-api.pyer.repl.co/get?user=' + name#lots of thanks to @pyer
      api = requests.get(apilink)
      data = eval(api.text)
      sun = data['langs']
      return sun
    except:
      print("ERROR: Cannot find " + name + "'s posts")

def replit_name(name = None):
  if name == None:
    print("ERROR: You didn't fill out the name parameter!")
  else:
    try:
      apilink = 'https://replit-user-api.pyer.repl.co/get?user=' + name#lots of thanks to @pyer
      api = requests.get(apilink)
      data = eval(api.text)
      sun = data['name']
      return sun
    except:
      print("ERROR: Cannot find " + name + "'s name!")

def replit_bio(name = None):
  if name == None:
    print("ERROR: You didn't fill out the name parameter!")
  else:
    try:
      apilink = 'https://replit-user-api.pyer.repl.co/get?user=' + name#lots of thanks to @pyer
      api = requests.get(apilink)
      data = eval(api.text)
      sun = data['bio']
      return sun
    except:
      print("ERROR: Cannot find " + name + "'s bio!")

def version():
  print("VERSION: 0.0.1")


#make loading thing next version

'''
l = replit_bio("darkdarcool")
print(f"My bio is {l}")
l = replit_cycles("darkdarcool")
print(f"I have {l} cycles!")
l = replit_name("darkdarcool")
print(f"My nickname is {l}")
'''