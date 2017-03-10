myfile_formar = open('C:\Users\lianr\Desktop\my.txt').read().lower()
myfile = myfile_formar.replace(',',' ').replace('.',' ')
#print myfile
mybox = myfile.split()
print len(mybox)
ansfile_1 = open('C:\Users\lianr\Desktop\what.txt').read().lower()
ansfile = ansfile_1.replace(',',' ').replace(':',' ').replace('.',' ')
ansbox = ansfile.split()
print len(ansbox)
for i in range(len(ansbox)):
    if mybox[i] != ansbox[i]:
        if mybox[i] != ansbox[i]:
            try:
                for x in range(1,3):
                    if mybox[i-x][0] == ansbox[i][0] : 
                        if mybox[i-x] != ansbox[i]:
                            print 1,mybox[i-x],ansbox[i]
                    elif mybox[i+x][0] == ansbox[i][0]:
                        if mybox[i+x] !=ansbox[i]:
                            print 2,mybox[i+x],ansbox[i]
                    else:
                        raise ValueError
            except ValueError:
                print 3,mybox[i],ansbox[i]
