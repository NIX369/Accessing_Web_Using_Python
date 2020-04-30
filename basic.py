#Finding sum of all integer values in a file of text

import re
file = open('train.txt')
y=[]
lst=[]
for line in file:
    x =  re.findall('[0-9]+', line)
    y.append(x)
# the list y has all the integer values from txt file but in string format
for i in y:
    for j in i:
        lst.append(int(j))              # Converting it into int
print(lst)
sum=0
for i in lst:
    sum = sum+i                         # Adding all values in the new integer list
print(len(lst))
print(sum)