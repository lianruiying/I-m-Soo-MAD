
def fileW():
    filename = raw_input('File Name: ')
    address = r'C:\Users\lianr\Desktop\\' + filename
    return address

myfile_formar = open('C:\Users\lianr\Desktop\my.txt').read().lower()
myfile = myfile_formar.replace(',',' ').replace('.',' ')
mybox = myfile.split()
print len(mybox)
ansfile_1 = open('C:\Users\lianr\Desktop\what.txt').read().lower()
ansfile = ansfile_1.replace(',',' ').replace(':',' ').replace('.',' ')
ansbox = ansfile.split()
print len(ansbox)

def GetWords(inputbox):
    box = []
    for words in inputbox :
        if words not in box:
            box.append(words)
    return box

mynewbox = GetWords(mybox)
ansnewbox = GetWords(ansbox)

copybox = mynewbox[:]
for word in mynewbox:
    if word in ansnewbox:
        del copybox[copybox.index(word)]
        del ansnewbox[ansnewbox.index(word)]



def recurPrint(box1,box2):
    box1.sort()
    box2.sort()
   # print copybox
    #print ansnewbox
    for i in range(len(box1)):
        try:
            print box1[i],box2[i]
        except IndexError:
            print ' '

        
recurPrint(copybox,ansnewbox)


#   This is not so good not doing comments , right?      But .........   :p
