import urllib

file = "E:\Full-Stack Track - One Million Arab Coders\movie_quotes\movie_quotes.txt"
def red_text(file_location):
    text=open(file_location)
    content_text=text.read()
   # print (content_text)
    check_profanity(content_text)
    text.close()

def check_profanity(text):
    check = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output=check.read()
    if "false" in output:
        print "this document has no curse words"
    elif "true" in output:
        print "Profainty Alert"
    else:
        print"this document couldent checked properly !"
    check.close()

red_text(file)