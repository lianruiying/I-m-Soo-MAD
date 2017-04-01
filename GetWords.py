import re
fil = open('C:\Users\lianr\Desktop\y.xfdf')
fi = fil.read()
#print words
#print re.findall('<contents>(.+)</contents>',words)

for char in re.findall('<contents>(.+)</contents>',fi):
    print char


fil.close()