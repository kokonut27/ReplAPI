import requests, os, json
from bs4 import BeautifulSoup
import string
import re

import aiohttp
import asyncio


'''
  response = requests.get(f"https://replit.com/@{owner}/", headers = {"User-Agent": "Mozilla/2.0"})
  soup = BeautifulSoup(response.text, 'html.parser')

  cont = response.json()
  print(cont)
'''

class User():
  def __init__(self, user):
    self.name = user

  def replit_user():
      try:
        owner = os.environ['REPL_OWNER']
        return owner
      except:
        exit("ERROR: No such replit account exists!")
        #in this case, you will probably never have this error, because you will be able to view it, but just in case.

  def replit_cycles(self):
      name = self.name
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

  def replit_langs(self):
      name = self.name
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

  def replit_name(self):
      name = self.name
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

  def replit_bio(self):
      name = self.name
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

  def replit_post(self):#latest post
      name = self.name
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
    
  def replit_posts(self):#all posts
      name = self.name
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
    
  def replit_comment(self):
      name = self.name
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
    
  def replit_comments(self):
      name = self.name
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

  def replit_avatar(name=None):
    if name is None:
      exit('ERROR: You didnt fill out the name parameter!')
    else:
      try:
        req = requests.get('https://replit.com/@'+name)
        soup = BeautifulSoup(req.content, 'html.parser')
        element =  soup.find(class_='jsx-2410840271 profile-icon profile-icon-xl')['style']
        url =  re.findall('(\(.+?)\)', element)
        return url[0][2:-1]

      except Exception as e:
        print(e)
        exit('ERROR: Could not find specified person\'s name.')
        

class AsyncUser():
	def __init__(self, name):
		self.name = name
		self.sess = aiohttp.ClientSession()
		self.apilink = 'https://replit-user-api.pyer.repl.co/get?user=' + name#lots of thanks to @pyer
		if self.name == '':
			raise EnvironmentError('You didnt fill out the "name" parameter')
	async def replit_cycles(self):
		try:
			async with self.sess.get(self.apilink) as resp:
				data = eval(resp.text)
				cycles = data['cycles']
				return await cycles
		except Exception:
			exit('ERROR: Cannot find name', 1)
		
	async def replit_langs(self):

	
  

class info(): 
  def version():
    print("VERSION: 0.0.2")#we're heading onto next version!

  def owners():
    print("OWNERS:\nMain Owner: JBYT27\nSide Owne`r(weird sidekick): darkdarcool\n The best one: LAMAQDAHODWALA")

if __name__ == '__main__':
	print(replit_avatar('LAMAQDAHODWALA'))
