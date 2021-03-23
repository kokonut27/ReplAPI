# REPLAPI Module
<img style="float: right;" src="https://user-images.githubusercontent.com/66882633/112184565-b7a0dd80-8bd5-11eb-938a-4451d3207091.png"></img>

            


##### Inspired by @RayhanADev and made in python
##### Made by @JBYT27(@JBloves27) & @darkdarcool
###### ~~Note the lots of pings lol~~

--- 

## About the Module

REPLAPI is a module that crawls the internet retrieving your(and anyone elses) replit data! 

It is currently very slow, and will most likely cause a lot of lag to a game, your computer, or replit(and anything really). So because of this, it is still in beta, but we are trying to improve the speed and we hope it will be lightning fast(or at least not take 10 seconds) for the end of the project! Now, lets talk about how to actually install this this module.

---

## Installation & Usage

### Installation
To install this module, search `REPLAPI` in the package tab in a python repl, or do `pip install REPLAPI` in the shell. 

After doing so, your REPLAPI module will be installed on your repl, and you can start using it!

### Usage

After installing this module, you can finally use it!

Lets start with something basic, like accessing cycles. To do this, use this code:

``` python
import REPLAPI as repl
my_cycles = repl.replit_cycles("UsernameOfUserOnReplit")
print("Cycles: " + my_cycles)
```

This will return the number of cycles of the user that you put in the quotes.

You can do this for any user on replit.

While the lag for this is pretty annoying, we recommend putting a loading animation over it.

This is a full list of all of the things you can do:
- `replit_langs("username here")` \[This returns your most used langs]


- `replit_post("username here")` \[This returns the first replit post on your profile list]


- `replit_posts("username here")` \[This returns all of the replit posts on your profile until the load more button]


- `replit_bio("username here")` \[This returns the users bio]

- `replit_comment("username here")` \[This returns the first comment on your replit profile]

- `replit_comments("username here")` \[This returns all of the replit comments on your profie until the load more button]

- `replit_user()` \[This just returns the owner of the repl's username, this has no parameter]

- `replit_name("username here")` \[This returns the nickname of the username]

--- 

## Closing

So this is the `REPLAPI module`! We hope you guys enjoy using this module. Please do give suggestions, as we are *always* (jk) available with them! If there are any bugs, also let us know with them! Another thing I should point out is that this is in `python`, so ~~obviously~~ this is only available in python. 

# KTHXBAI!!!!!!!!

Special thanks to @RayhanADev for inspiring and helping with this project!
###### sry for pings lol

[This is the docs link](https://ReplAPI-Docs.darkdarcool.repl.co)
