import requests, os, json, repltalk, asyncio, getpass, sys
from bs4 import BeautifulSoup


class info(): 
  def version():
    print("VERSION: 0.0.6")

  def owners():
    print("OWNERS:\nMain Owner: JBYT27\nSide Owner(weird sidekick): darkdarcool")


class assets():
  async def replit_avatar_get(name = None):
    if (name == None):
      exit("ERROR: Please fill out the name parameter!")
    else:
      try:
        client = repltalk.Client()
        user = await client.get_user(name)
        return user.avatar
      except:
        exit(f"ERROR: Cannot load {name}'s avatar!") 
  async def replit_cycle_get(name = None):
    if (name == None):
      exit("ERROR: Please fill out the name parameter!")
    else:
      try:
        client = repltalk.Client()
        user = await client.get_user(name)
        return user.cycles
      except:
        exit(f"ERROR: Cannot load {name}'s cycles!")
  async def replit_name_get(name = None):
    if (name == None):
      exit("ERROR: Please fill out the name parameter!")
    else:
      try:
        client = repltalk.Client()
        user = await client.get_user(name)
        return user.full_name
      except:
        exit(f"ERROR: Cannot load {name}'s name!")
  async def replit_bio_get(name = None):
    if (name == None):
      exit("ERROR: Please fill out the name parameter!")
    else:
      try:
        client = repltalk.Client()
        user = await client.get_user(name)
        return user.bio
      except:
        exit(f"ERROR: Cannot load {name}'s bio!")
  async def replit_leaderboard_get():
      #try:
        client = repltalk.Client()
        leaderboard = await client.get_leaderboard(limit=10)
        return leaderboard#, sep="\n"
      #except:
       # exit(f"ERROR: Cannot load leaderboard!")

def replit_user():
    try:
      owner = os.environ['REPL_OWNER']
      return owner
    except:
      exit("ERROR: No such replit account exists!")
def replit_avatar(name = None):
  if (name == None):
    exit("Please fill out the name parameter!")
  else:
    try:
      e = asyncio.run(assets.replit_avatar_get(f"{name}"))
      return e
    except:
      exit(f"ERROR: Cannot find {name}'s avatar!")
def replit_bio(name = None):
  if (name == None):
    exit("Please fill out the name parameter!")
  else:
    try:
      e = asyncio.run(assets.replit_bio_get(f"{name}"))
      return e
    except:
      exit(f"ERROR: Cannot find {name}'s bio!")
def replit_name(name = None):
  if (name == None):
    exit("Please fill out the name parameter!")
  else:
    try:
      e = asyncio.run(assets.replit_name_get(f"{name}"))
      return e
    except:
      exit(f"ERROR: Cannot find {name}'s name!")

def replit_cycles(name = None):
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      try:
        e = requests.get('https://repldata.ch1ck3n.repl.co/cycles/' + name).text
        return e
      except:
        exit("ERROR: Cannot find " + name + "'s cycles!")
def replit_langs(name = None, extra = None):
    sun = 0
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      if (extra == None):
        pass
      else:
        if (extra == "all"):
          sun = 1
      try:
        link = requests.get('https://replit.com/data/profiles/' +name )
        data = link.json()
        #print(data)
        els = list(data.items())
        all = els[-1]
        if ("hacker" in all):
          all = els[-2]
        if ("isTeam" in all):
          all = els[-1]
        all = list(all)
        stuff = all[1]
        stuff = str(stuff)
        stuff = stuff.replace("'", "")
        stuff = stuff.replace("[", "")
        stuff = stuff.replace("]", "")
        stuff = stuff.replace(" ", "")
        li = list(stuff.split(","))
        if (sun == 1):
          sun = 2
          return li, sun
        return (li)
      except:
        exit("ERROR: Cannot find " + name + "'s langs!")

#start working here
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
        exit("ERROR: Cannot find "+ name+"'s hottest post!")
  
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
        
      except:
        exit("ERROR: Cannot find "+ name+"'s posts!")

def replit_posts_len(name = None):#NEW FUNCTION
  if name == None:
    exit("ERROR: You didn't fill out the name parameter!")
  else:
    try:
      post = requests.get("https://replit.com/@"+ name +"?tab=posts")#name
      soup = BeautifulSoup(post.content, 'html.parser')
      html1 = soup.find_all("div", {"class":"jsx-2329710370 board-post-list-item-post-title"})#.get_text()
      num = 0
      for i in html1:
        num+=1
      return str(num)

    except:
      exit("ERROR: Cannot find "+name+"'s post length!")
  
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
        exit("ERROR: Cannot find "+ name+"'s hottest comment!") 
  
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

def replit_comments_len(name = None):#NEW FUNCTION
  if name == None:
    exit("ERROR: You didn't fill out the name parameter!")
  else:
    try:
      post = requests.get("https://replit.com/@" + name + "?tab=comments")
      soup = BeautifulSoup(post.content, 'html.parser')
      num=0
      for data in soup.find_all("p"):
        num+=1
      return str(num)
    except:
      exit("ERROR: Cannot find "+name+"'s comments length!")

class talk():
  def all_posts():#all posts, prob will not work lol 
  # dumb idea, will break
    pass
  
  def top_post():# top post 
  # this one is okey
    pass
  
  def top_posts():# few of the top posts
  # this ones aight
    pass

  def new_post():# newest post
  # this ones dumb but okey
    pass
  
  def new_posts():# newest posts
  # dumb but okey
    pass

  def leaderboard():# leaderboard info, idk yet
  # idk whut this one is
    try:
      e = asyncio.run(assets.replit_leaderboard_get())
      e = str(e)
      e = e.replace('<', '')
      e = e.replace('>', '')
      e = e.replace('[', '')
      e = e.replace(']', '')
      e = list(e.split(', '))
      # e = '\n'.join(e)
      return e
    except:
      exit("ERROR: Cannot load leaderboard!")

repltalk = talk.leaderboard()
os.system("clear")
for i in range(10):
  print(repltalk[i])
