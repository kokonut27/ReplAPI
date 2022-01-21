#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json  # thx
import random
import os
# os.system("clear") # CLEAR IT UP YO



'''
wtf is this
╭━━━━━╮
╰┃ ┣▇━▇
 ┃ ┃  ╰━▅╮
 ╰┳╯ ╰━━┳╯ memedog says this is pog
  ╰╮ ┳━━╯
 ▕▔▋ ╰╮╭━╮
╱▔╲▋╰━┻┻╮╲╱▔▔▔╲
▏  ▔▔▔▔▔▔▔  O O┃
╲╱▔╲▂▂▂▂╱▔╲▂▂▂╱
 ▏╳▕▇▇▕ ▏╳▕▇▇▕
 ╲▂╱╲▂╱ ╲▂╱╲▂╱\
'''


ROLES = """
	id
	name
	key
	tagline
"""
ORGANIZATION = """	
	id
	name
	country
	postalCode
	state
	city
	timeCreated
"""
SUBSCRIPTION = """
	id
	planId
	quantity
	timeCreated
"""
BOARD = """
	id
	name
	color
	description
"""
LANGUAGE = """
	id
	key
	displayName
	tagline
	icon
	category
"""
USER = f"""
	id
	fullName
  firstName
  lastName
	username
	image
	bio
	karma
	isHacker
	timeCreated
  isBannedFromBoards
	roles {{
					{ROLES}
				}}
	organization {{
					{ORGANIZATION}
	}}
"""
REPL = f"""
	id
	url
	title
	description
	timeCreated
	size
	imageUrl
	isPrivate
	isAlwaysOn
  user {{
					{USER}
	}}
	lang {{
					{LANGUAGE}
	}}
	origin {{
					url
	}}
"""
COMMENT = f"""
	id
	body
	timeCreated
	url
	isAnswer
	voteCount
	canVote
	hasVoted
	post {{
					id
	}}
  user {{
					{USER}
	}}
"""
REPL_COMMENT = f"""
	id
	body
	timeCreated
	
	repl {{
					{REPL}
	}}
"""
POST = f"""
	id
	title
	body
	url
	commentCount
	isHidden
	isPinned
	isLocked
	isAnnouncement
	timeCreated
	isAnswered
  isAnswerable		
	voteCount
	canVote
	hasVoted
	user {{
    {USER}
  }}
	repl {{
					{REPL}
	}}
	board {{
					{BOARD}
	}}
	answer {{
					{COMMENT}
	}}
"""

# lol id go brrrrr

# user {{
# 					{USER}  
# 	}}

url = 'https://replit.com/graphql'

# hahae = {'query': 'query UserData { userByUsername(username: "RayhanADev") { id, username, karma, bio } }'}

headers = {
    'X-Requested-With': 'RayhanADev',
    'Referrer': 'https://replit.com/graphql'
}

# res = json.loads(requests.post(url, data=hahae, headers=headers).text)
# print(res) # res.text is var
# print(res["data"]["userByUsername"]["karma"])


class UserNotFoundError(Exception):
    pass
    

class UnluckyFroggyError(Exception):# YES IT IS 
    pass
    


class JSON:
  #Put everything here.
   
  pass


class User:
    def __init__(self, username):
        body = {'query': 'query UserData { userByUsername(username: "' + username + '") { '+USER+' } }'}
        self.res = json.loads(
            requests.post(url, data=body, headers=headers).text)['data']['userByUsername']
        if self.res is None:
            raise UserNotFoundError('User not found')
        if self.res['username'] == 'UnluckyFroggy':
            raise UnluckyFroggyError('You are not allowed to put frog in here')
        self.cycles = self.res['karma']
        self.bio = self.res['bio']
        self.username = self.res['username']
        self.fullname = self.res['fullName']
        self.banned = self.res['isBannedFromBoards']
        self.image = self.res["image"]
        self.roles = self.res["roles"]
        self.hacker = self.res["isHacker"]

    def posts(self, count=10, parse=False, order="new"):#could we add an order thingy in the function so like they could change the order? so like it could be new, trending, etc. Edit: seems like i just copied the idea from RayhanADev's function from the original lmao - jb
    # done - ckn
    #okie, thanks - jb
        body = {
              'query': """query User($username: String!, $after: String!, $count: Int!, $order: String!) {
					                user: userByUsername(username: $username) {
						                posts(after: $after, order: $order, count: $count) {
							                items {
								                """+POST+"""
							                }
						                }
					                }
				                }
                """,
                "variables": json.dumps({
                  "username": self.res['username'],
                  "after": "",
                  "count": count,
                  "order": order
                })
              }
        if parse:
          return Assets.parse_json(json.loads(requests.post(url, data=body,headers=headers).text))
        else:
          return str(json.loads(requests.post(url, data=body,headers=headers).text))

    def comments(self, count=10, parse=False, order="new"):
      body = {
              'query': """query User($username: String!, $after: String!, $count: Int!, $order: String!) {
					                user: userByUsername(username: $username) {
						                comments(after: $after, order: $order, count: $count) {
							                items {
								                """+COMMENT+"""
							                }
						                }
					                }
				                }
                """,
                "variables": json.dumps({
                  "username": self.res['username'],
                  "after": "",
                  "count": count,
                  "order": order
                })
              } 
      if parse:
        return Assets.parse_json(json.loads(requests.post(url, data=body, headers=headers).text))
      else:
        return str(json.loads(requests.post(url, data=body,headers=headers).text))

    def user(self, parse=False):
      body = {
              'query': """query User($username: String!, $after: String!, $count: Int!, $order: String!) {
					                user: userByUsername(username: $username) {
						                comments(after: $after, order: $order, count: $count) {
							                items {
								                """+USER+"""
							                }
						                }
					                }
				                }
                """,
                "variables": json.dumps({
                  "username": self.res['username'],
                  "after": "",
                })
              } 
      if parse:
        return Assets.parse_json(json.loads(requests.post(url, data=body, headers=headers).text))["data"]["user"]
      else:
        return str(json.loads(requests.post(url, data=body,headers=headers).text))


class Repl:
  def __init__(self,replUrl, parse=False, user=False):
      body = {'query': """
    query ReplView($url: String!) {
					repl(url: $url) {
						  ... on Repl {
							  """+REPL+"""
						  }
					  }
				  } """, 
            'variables': json.dumps({
              "url":  replUrl
            })}
      self.res = json.loads(requests.post(url, data=body,headers=headers).text)
      if (user == True):
          self.res["data"]["repl"]["user"] = User(self.res["data"]["repl"]["user"]["username"])
      elif user == False:
        self.res["data"]["repl"] = self.res["data"]["repl"]
      if parse == True:
        self.res = json.dumps(json.loads(requests.post(url, data=body,headers=headers).text), sort_keys=True, indent=2)


  def repl_comments(self, count=10, parse=False):
    pass

class Talk:#repl talk info
  def __init__(self,):
    pass


class Assets:
  def parse_json(tjson):
    return json.dumps(tjson, sort_keys=True, indent=2) # 4 is just too much
    

print(User("JBloves27").comments(parse=True))