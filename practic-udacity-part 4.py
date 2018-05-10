

'''''
# take brake programe
import time
import webbrowser

def take_brake(period=30 , loop=3):
    period= input("please enter the period you need to take brake default is 30 minut : ")
    loop =input("please enter how many time do yo take brake default is 3 : ")
    i=0
    while i<loop:
        print time.ctime()
        time.sleep(period*60)
        webbrowser.open("https://www.youtube.com/watch?v=XN5p4EWnOEk")
        i+=1

take_brake()

# secret messge

import os
w=['0','1','2','3','4','5','6','7','8','9']
new_file_name=[]
file=os.listdir("E:\Full-Stack Track - One Million Arab Coders\prank")
os.chdir("E:\Full-Stack Track - One Million Arab Coders\prank")
for word in file:
    new_word=word.translate(None,"0123456789")
    os.renames(word,new_word)



#turtel draw
import random
import turtle
window=turtle.Screen()
window.bgcolor("green")

amr=turtle.Turtle()
amr.speed(20)
i=0
clore=["red","blue","green","white",'pink','yellow']
while i<36 :
    amr.circle(100)
    amr.left(10)

    i+=1
    amr.fillcolor(clore[random.randint(0,5)])
    amr.fill(1)
window.exitonclick()
'''''

text=open("E:\Full-Stack Track - One Million Arab Coders\movie_quotes\movie_quotes.txt",'r')
content =text.read()
text.close()


import urllib
def profainty_check(text):
    out=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    if out.read()=="false" :
        print " your text is clear "
    else :
        print " profainty found you should check your code "

profainty_check(content)


/'/////mv'







