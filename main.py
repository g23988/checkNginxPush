import httplib, threading, urllib, urllib2, time
from collections import Counter
from time import sleep


host = "192.168.25.135"
global id, messageIndex, messageText
id = "978"
messageIndex="test"
messageText="ok"
delayCheckSec = 1

class hostThread (threading.Thread):
    def __init__(self,threadID, name, host):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.host = host
    def run(self):
        response = urllib2.urlopen("http://"+self.host+"/sub/"+id)
        html = response.read()
        if html==messageIndex+"="+messageText:
            print "true"
        else:
            print "false"


targetpath = "/"
def get_html_code(host,path=targetpath):

        try:
                data = urllib.urlencode({"test":"ok"})
                response = urllib2.urlopen("http://"+host+"/pub?id="+id,data)
                html = response.read()
                return html;
        except StandardError:
                return None

thread1 = hostThread(1,"thread1",host)
thread1.start()
sleep(delayCheckSec)
get_html_code(host)

