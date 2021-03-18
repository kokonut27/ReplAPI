# a module, so i dont need os and time module like i usually do - edit, nvm, i do need os module, but for smth else
import requests, os
from bs4 import BeautifulSoup


while True:
  try:
    owner = os.environ['REPL_OWNER']
    response = requests.get(f"https://replit.com/@{owner}/", headers = {"User-Agent": "Mozilla/2.0"})

    soup = BeautifulSoup(response.text, 'html.parser')

    
  except:
    exit("Error: There is no such replit account")
    #in this case, you will probably never have this error, because you will be able to view it, but just in case ;)