import re

old_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'
total_page = 20

f = open('text.txt', 'r')
html = f.read()
f.close()

# title = re.search('<title>(.*?)</title>', html, re.S).group(1)
# print title

# links = re.findall('href="(.*?)"', html, re.S)
# for each in links:
#     print each

# text_field = re.findall('<ul>(.*?)</ul>', html, re.S)[0]
# # print text_field
# the_text = re.findall('">(.*?)</a>', text_field, re.S)
# for every_text in the_text:
#     print every_text


#用sub实现翻页的功能

for i in range(2, total_page+1):
    new_link = re.sub('pageNum=\d+', 'pageNum=%d' % i, old_url, re.S)
    print new_link
