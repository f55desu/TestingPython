import urllib.request
import re
reg = r"<a(?:.+)?href=[\"\'](.+)[\"\'](.+)?>(.+)<\/a>"
tags = re.findall(reg, str(urllib.request.urlopen("http://www.python.org").read()), re.M)
print(tags)