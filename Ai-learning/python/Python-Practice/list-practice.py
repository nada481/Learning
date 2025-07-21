
import math as math

#Create a list of the first 10 even numbers:
evenNum=[]
for x in range(-1,1000,1): #start stop steps
    if x %2==0:
        evenNum.append(x)

#Reverse a list without using the reverse() method.


def reverseList(list):
    for y in evenNum:
     evenNum.sort(reverse=True)
    return list

def sum(list):
    sum=0
    for i in list:
        sum+=i

    return sum 


#print(sum(evenNum))

listOfno= [1, 3, 5, 3, 3, 9, 3]

j=0
count =0
while (j < len(listOfno)):
    if listOfno[j] ==3 :
        count+=1
    j+=1


# print(f'{count}, is the number of repeated 3s')


#Replace all negative numbers in a list with 0.

numbers=[3,4,11,234,-1,-34442,23,100,43,50,12]
for i in range(len(numbers)): 
    if numbers[i] <0:
        numbers[i] = 0
    

#print(numbers)

# Given a list of numbers, create a new list with only the squares of the odd numbers:

# create a new list --> loop through the old list and do comparsion if the index i in exList is an odd number then append the element^2 to the new list

Oddnumbers=[]

for i in range(len(numbers)):
    if numbers[i] % 2==1:
        Oddnumbers.append(math.pow(numbers[i],2))
    
#print(Oddnumbers)

# Write a list comprehension to filter out all words shorter than 4 letters from a list of strings.
# steps: 1) create a string list, 2) loop over the list #) condition if len(names[i] <=4 then pop() else continue)

names=['Arrow','Gravity','cow','bird','Olivia','noah','james','Elijah','Sophia']

names = [name for name in names[:] if len(name) > 4]

# for name in names[:]: # copy it
#     if len(name) <=4:
#         names.remove(name)


#print(names)
# --> comprehension part:


EvenNumbers=[math.pow(no,2) for no in numbers if no %2==0 ]
print(EvenNumbers)


#Count how many strings in a list start with a vowel.
# 1) create a count variable, 2) loop over the list, 3) if names[i] contains (a,e,i,o) then count+=1 
vowels = 'aeiouAEIOU'
total=0
words = ['apple', 'asa', 'orange', 'umbrella', 'grape', 'Egg', 'iguana']



count = 0
for word in words:
    if word and word[0] in vowels: #word[0] refers to the first letter in the string. 
        count += 1

print(count)

