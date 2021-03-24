import requests, os, json
os.system("pip install beautifulsoup4")
from bs4 import BeautifulSoup
import string
import re


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
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      try:
        apilink = 'https://replit-user-api.pyer.repl.co/get?user=' + name#lots of thanks to @pyer
        api = requests.get(apilink)
        data = eval(api.text)
        sun = data['cycles']
        return sun
      except:
        exit("ERROR: Cannot find " + name + "'s cycles!")

def replit_langs(name = None):
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      try:
        apilink = 'https://replit-user-api.pyer.repl.co/get?user=' + name# the link was wrong, i switched it
        api = requests.get(apilink)
        data = eval(api.text)
        sun = data['langs']
        sun = ', '.join(sun)
        return sun
      except:
        exit("ERROR: Cannot find " + name + "'s langs!")

def replit_name(name = None):
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      try:
        apilink = 'https://replit-user-api.pyer.repl.co/get?user=' + name#lots of thanks to @pyer
        api = requests.get(apilink)
        data = eval(api.text)
        sun = data['name']
        return sun
      except:
        exit("ERROR: Cannot find " + name + "'s name!")

def replit_bio(name = None):
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      try:
        apilink = 'https://replit-user-api.pyer.repl.co/get?user=' + name#lots of thanks to @pyer
        api = requests.get(apilink)
        data = eval(api.text)
        sun = data['bio']
        return sun
      except:
        exit("ERROR: Cannot find " + name + "'s bio!")

def replit_post(name = None):#latest post
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      #user = os.environ["REPL_OWNER"]
      try:
        post = requests.get("https://replit.com/@"+ name +"?tab=posts")#name
        soup = BeautifulSoup(post.content, 'html.parser')
        html1 = soup.find("div", {"class":"jsx-2329710370 board-post-list-item-post-title"}).get_text()
        return html1
        #b = a.replace('</div>','')
        #return b
      except:
       exit("ERROR: Cannot find "+ name+"'s latest post!")
  
def replit_posts(name = None):#all posts
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      try:
        post = requests.get("https://replit.com/@"+ name +"?tab=posts")#name
        soup = BeautifulSoup(post.content, 'html.parser')
        html1 = soup.find_all("div", {"class":"jsx-2329710370 board-post-list-item-post-title"})#.get_text()
        all_text = []
        for i in html1:
          all_text.append(i.get_text())
        return '\n'.join(all_text)
        #return html1
        #b = a.replace('</div>','')
        #return b
      except:
       exit("ERROR: Cannot find "+ name+"'s posts!")
  
def replit_comment(name = None):
  if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
  else:
      try:
        post = requests.get("https://replit.com/@" + name + "?tab=comments")
        soup = BeautifulSoup(post.content, 'html.parser')
        for data in soup.find("p"):
          return (data.get_text())
          break # keep this here so it prints once
      except:
        exit("ERROR: Cannot find "+ name+"'s latest comment!") 
  
def replit_comments(name = None):
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      try:
        post = requests.get("https://replit.com/@" + name + "?tab=comments")
        soup = BeautifulSoup(post.content, 'html.parser')
        all_text = []
        for data in soup.find_all("p"):
          all_text.append(data.get_text())
        return '\n'.join(all_text)
      except:
        exit("ERROR: Cannot find "+name+"'s comments!")

def replit_profile_pic(name=None):
  if name is None:
	  exit('ERROR: You didnt fill out the name parameter!')
  else:
	  try:
		  req = requests.get('https://replit.com/@'+name)
		  soup = BeautifulSoup(req.content, 'html.parser')
		  element =  soup.find(class_='jsx-2410840271 profile-icon profile-icon-xl')['style']
		  print(element)
		  url =  re.findall('(\(.+?)\)', element)
	  except Exception as e:
		  print(e)
		  exit('ERROR: Could not find specified person\'s name.')
        
class info(): 
  def version():
    print("VERSION: 0.0.2")#we're heading onto next version!

  def owners():
    print("OWNERS:\nMain Owner: JBYT27\nSide Owner(weird sidekick): darkdarcool\n The best one: LAMAQDAHODWALA")

if __name__ == '__main__':
	print(replit_profile('LAMAQDAHODWALA'))
