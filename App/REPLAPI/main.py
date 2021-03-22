import requests, os, json
from bs4 import BeautifulSoup


'''
  response = requests.get(f"https://replit.com/@{owner}/", headers = {"User-Agent": "Mozilla/2.0"})
  soup = BeautifulSoup(response.text, 'html.parser')

  cont = response.json()
  print(cont)
'''


class replapi():
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

  def replit_posts(name = None):
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      try:
        post = requests.get("https://replit/@"+name+"?tab=posts")
        soup = BeautifulSoup(post.content, 'html.parser')
        html1 = soup.find("div", {"class":"jsx-2329710370 board-post-list-item-post-title"})
        html2 = str(html1)
        a = html1.replace('<div class="jsx-2329710370 board-post-list-item-post-title">','')
        b = a.replace('</div>','')
        return b
      except:
        exit("ERROR: Cannot find "+ name+"'s latest post!")
  
  def replit_comments(name = None):
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      try:
        post = requests.get("https://replit/@"+name+"?tab=comments")
        soup = BeautifulSoup(post.content, 'html.parser')
        html1 = soup.find("div", {"class":"rendered-markdown jsx-4279741890"})
        try:
          a = html1.find('a')
          b = a.get('href')
         except:
          exit("ERROR: Linking is not working!")
        
        html2 = str(html1)
        r = html2.replace('<div class="rendered-markdown jsx-4279741890"><p>',
                          '')
        try:
          x = r.replace('<span class="jsx-589677836 user-hover-card user-hover-card-inline">'
                            '<a href="'+oop1+'">','')
        except:
          exit("ERROR: Span linking not working!")
        
        s = x.replace('</a></span>','')
        abc = s.replace('</p></div>','')
        return abc
      
      except:
        exit("ERROR: Cannot find "+ name+"'s latest comment!") 

  def version():
    print("VERSION: 0.0.2")#we're heading onto next version!

  def owners():
    print("OWNERS:\nMain Owner: JBYT27\nSide Owner(weird sidekick): darkdarcool")#added another function lol



#how to make loading?
# idk
