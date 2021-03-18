import requests, os, json
from bs4 import BeautifulSoup



  response = requests.get(f"https://replit.com/@{owner}/", headers = {"User-Agent": "Mozilla/2.0"})
  soup = BeautifulSoup(response.text, 'html.parser')

  cont = response.json()
  print(cont)


def replit_user():
  try:
    owner = os.environ['REPL_OWNER']
    return owner
  except:
    exit("ERROR: No such replit account exists!")
    #in this case, you will probably never have this error, because you will be able to view it, but just in case.

def version():