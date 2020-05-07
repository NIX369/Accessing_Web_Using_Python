import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_499385.html')
for line in fhand:
    print(line.decode().strip())