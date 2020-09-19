import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = ' http://py4e-data.dr-chuck.net/comments_961657.xml'
data = urllib.request.urlopen(serviceurl, context=ctx).read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
results = tree.findall('.//count')
sum = 0

for item in results:
    sum = sum + int(item.text)

print(sum)