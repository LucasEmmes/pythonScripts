## Cryptography stuff, yay! ##

I took a class of cryptography in the spring of 2021,  
and when we went through some historical ciphers I thought  
it'd be educational to try to replicate them in python.

Most of these (with the exception of visual_cryptography.py)  
are meant to be used as an import, but if you want  
to run them by themselves in a console, you can.

I have not gotten around to implementing good  
failsafes / debugging code yet,  
in case something were to go wrong.

###*Notes*###
  - **visual\_cryptography.py**  
    This one requires you have Pillow installed.
    It takes both PNG and JPG as input  
    (possibly more, haven't checked).
	
	You can find some example images in the ./assets folder  
	to easily test out the code for yourself
    
 - **substitution\_ciphers.py and transposition\_ciphers.py**  
    Take note when making alphabets for these to include **EVERY**  
    character in the plaintext. Make sure you remember to add  
    a space character, as well as differentiating between  
    upper and lower case characters.
