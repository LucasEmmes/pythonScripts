## Cryptography Stuff, yay! ##

I took a class of cryptography in the spring of 2021,  
and when we went through some historical ciphers I thought  
to myself: these can't be all that hard to replicate in python.  
And they really weren't. Still kinda tricky.

Most of these (with the exception of visual.py)  
are meant to be used as an import, but if you want  
to run them by themselves in a console, you can.

All of these are delivered **as is**.  
This just means I have not gotten around to  
implementing good failsafes / debugging code  
yet in case something were to go wrong.

*Notes*
  - visual.py  
    This one requires you have Pillow installed.
    It takes both PNG and JPG as input  
    (possibly more, haven't checked)  
    It also doesn't have docstrings yet  
    but probably aren't needed either.
    
 - substitution.py and transposition.py  
    Take note when making alphabets for these to include **EVERY**  
    character in the plaintext. Make sure you remember to add  
    a space character, as well as differentiating between  
    upper and lower case characters.
