from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


#1.PS E:\__pycache__> python ex13.py 12 34
Traceback (most recent call last):
  File "ex13.py", line 3, in <module>
    script, first, second, third = argv
ValueError: need more than 3 values to unpack
--輸入的字串數量必須大於3個才能使用這個package

#2.
##more
#from sys import argv
#script, tobey, jane, jenny, demi = argv
#print "The script is called:", ex13.py
#print "Your first variable is:", demi
#print "Your second variable is:", jane
#print "Your third variable is:", jenny 
#print "Your fourth variable is:", abby
#

##less
#from sys import argv
#scripy, tobey, jane= argv
#print "The script is called:", ex13.py
#print "Your first variable is:", jane
#print "Your second variable is:", jenny 
#
#

#3.
#

