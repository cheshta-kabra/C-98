f=open('test.txt','r')
""" print(f.read()) """
fileLine = f.readlines()
for line in fileLine:
    print (line)
introStr='I am 15 years old , I am 10th class student'
words = introStr.split(",")
print(words)
name1=input('enter your name')
def greet(name):
    print('Hello',name)
greet(name1)