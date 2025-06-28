#-------------------------------------------------------------------------------------
# THIS IS FOR READING
#-------------------------------------------------------------------------------------
"""it is used to open a file """
'''but this method is not preferred because in this you have to explicitly close the file
 else it will cause some problems'''

f = open('demo.txt','r')

print(f.name)
print(f.mode)

f.close()

'''opening the file with context manager it will close the file automatically'''

'''if you want to read the file content then you can use read() method but this will also load the data and this isn not preferred when we have large data in the file'''
with open('demo.txt','r') as f:
    f_content = f.read()
    print(f_content)

'''this gives the content line by line in the form of list'''
with open('demo.txt','r') as f:
    f_content = f.readlines()
    print(f_content)

'''this is the most efficient way to read the file'''
with open('demo.txt','r') as f:
    for line in f:
        print(line,end="") ##this end = "" is here to print lines as in the file without a gap

'''if you want more control over the file then you can use the for loop'''
with open('demo.txt','r') as f:
    f_content = f.read(30) # this will print the first 30 characters of the file
    print(f_content,end ='')
    # we can repeat the samp ecode to get nxt 30 characters and when the file content ends, it will give empty string

'''this is the same code as above but with a loop to read whole file'''

with open('demo.txt', 'r') as f:

    size_to_read = 10
    f_content = f.read(size_to_read)
    print(f.tell())

    while len(f_content) > 0:
        print(f_content, end='*')
        f_content = f.read(size_to_read)
    f.seek(0) ##this will reset from where it starts reading

#---------------------------------------------------------------------------------
#THIS IS FOR WRITING IN THE FILE
#---------------------------------------------------------------------------------

'''we can not write in the file that is not opened in read mode'''
with open ('demo.txt','r') as f:
    f.write('hello')

'''this is code to write in the file'''
with open('demo_2.txt','w') as f:
    pass
# if the file demo_2.txt is not existing, this will create the file itself
with open('demo_2.txt','w') as f:
    f.write('python')
# if the file exists and already have something in it will overwrite the file to avoid this, open the file in appended mode i.e., 'a'

for d,r,f in os.walk('C:/Users/Vikas Dubey/Desktop/Python_basic'):
    for file in f:
        file.rename('txt','jpg')