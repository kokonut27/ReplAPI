# REPLAPI Module
#### _**(Version 0.0.4)**_
##### Made by @JBYT27 and @darkdarcool
![favicon](https://user-images.githubusercontent.com/66882633/112184565-b7a0dd80-8bd5-11eb-938a-4451d3207091.png)
--- 
## About the module:
As you may have seen on our previous module, this is the next version (or next-next. or the next-next-next. lol). We have added some new commands to the module. We have also made the speed faster for a lot of them.*(Check out the installation header below for how to get started with the module.)*

--- 

## Installation:

|Manage          |Command                                         |
|:----------------|:-----------------------------------------------|
|**pip**          | `$ pip install REPLAPI`                          |
|**poetry**       | `$ python -m poetry add REPLAPI`                 |
|**Repl.it**      | Search `REPLAPI` in the package tab and add it |

--- 
## What's new!

Well, for a lot of things in the module, including faster speeds for Avatars, Languages, Cycles, Full Names, and Bios!! We have also stopped using non-replit(external) json files for things that require it. Now we use replit json files. And we have made it so the module does not import a ton of modules whenever you run it!(by improving the modules directions!). If we are dumb and it doesen't work, please wait to use the module, or use version 0.0.3. 

## How to use the module

We have improved a bunch of the modules! Here is a small example using **`ALL`** of them!

- `replit_langs("username")`
``` python
import REPLAPI as repl
my_favorite_lang = repl.replit_langs("myusername")
print("My favorite languages are " + my_favorite_lang[0] + ", " + my_favorite_lang[1] + ", " + my_favorite_lang[2] + "!")
```

- `replit_cycles("username")`
``` python
import REPLAPI as repl
mycycles = repl.replit_cycles("myusername")
print("I have " + mycycles + " cycles!")
```

- `replit_avatar("username")`
``` python
import REPLAPI as replit
myprofilepic = repl.replit_avatar("myusername")
print("My profile image is in here: " + my)
```

- `replit_bio("username")`
``` python
import REPLAPI as replit
mybio = repl.replit_bio("myusername")
print("my bio on my replit profile is:\n" + mybio)
```

- `replit_name("username")`
``` python
import REPLAPI as replit
myfullname = repl.replit_name("myusername")
print("My full name is " + myfullname)
```
- `replit_comment("username)`
``` python
import REPLAPI as replit
mycomment = repl.replit_comment("myusername")
print("The top comment on my replit profile is " + mycomment + "!")
```
If you do `replit_comments("myusername")` you will get a long list of your comments on your replit profile until the load more button.

- `replit_post("username")`
``` python
import REPLAPI as repl
mypost = repl.replit_post("myusername")
print("The top post on my replit profile is " + mypost + "!")
```
The same thing goes for posts, if you do `replit_posts("username")`, it will return all of the posts on your replit profile until the load more button!

✨ Special(experimental) Function! ✨

The special function is `replit_langs("username")`. It returns the user's most recently used coding languages in a list! It works like this:
``` python
import REPLAPI as repl
myfavs = replit_langs("myusername")
print("My most used coding languages are: " + myfavs[0] + ", " + myfavs[1] + ", and " + myfavs[2] + "!")
```
This function is experimental, we are just playing around with it and need **YOUR** feedback and issues!

--- 

## Credits:
- [@RayhanADev](https://replit.com/@RayhanADev) ( for giving use the idea and helping us along the way! )
- [@IcynHackz](https://replit.com/@IcynHackz) ( for giving us a faster way of accesing data! )
- [@MarcusWeinberger](https://replit.com/@MarcusWeinberger) ( for helping us for the overall quality of the module! )
- Everyone that has left a pull request and issue on our [git repo](https://github.com/JBYT27/REPLAPI) ( thanks you guy's so much! )

--- 
# Contributing

If you wanna contribute, we will **not** invite you to the repl of this moudle(it's private), a we will **not** invite you to the github repo. If you wish to contribute, please leave and issure or a pull request on the github repo [here](https://github.com/JBYT27/REPLAPI). We will always(jk) try our best to read them! If you wish to complain(lol), leave it in the disscusion on the repo. 

# Closing

So yea, that's the module! We worked hard on it, and we love your guy's contributions! Feel free to use the package whenever, and for anything.

KTHXBAI!!! (lolcode reference)