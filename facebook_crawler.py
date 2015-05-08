import time
import urllib2
from urllib2 import urlopen
import datetime


website = 'https://www.facebook.com/micromaxinfo/photos/a.135353393141505.25202.120735417936636/960349747308528/?type=1&theater'

topSplit = 'body\":{\"text\":\"'
bSplit = '\",\"ranges\":'


sourceCode = urllib2.urlopen(website).read()

for i in range(1,50):

 sourceCodeSplit = sourceCode.split(topSplit)[i].split(bSplit)[0]
 print i
 print sourceCodeSplit











