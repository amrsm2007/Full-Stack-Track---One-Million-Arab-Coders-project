import webbrowser
import time

print (" the programe started at",time.ctime())
loop=3
i=0

while i <loop :
    time.sleep(60*60*1)
    webbrowser.open("https://www.youtube.com/watch?v=XN5p4EWnOEk")
    i+=1
