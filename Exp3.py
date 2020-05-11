# Extracting Data from XML
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
#The program will prompt for a URL, read the XML data from that URL using urllib and then 
#parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

#We provide two files for this assignment. 
#One is a sample file where we give you the sum for your testing and 
#the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_499387.xml (Sum ends with 81)
#You do not need to save these files to your folder since your program will read the data directly from the URL.

#Sample data:
#<comment>
#  <name>Matthias</name>
#  <count>97</count>
#</comment>


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count=0
url = input("Enter url : ")
xml = urllib.request.urlopen(url, context=ctx).read()
stuff = ET.fromstring(xml)

lst = stuff.findall('comments/comment')
for i in lst:
    ele = i.find("count").text
    ele = int(ele)
    count = count + ele
print("Sum:", count)
