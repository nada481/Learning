# => list: 

names = ['nada','sara','abeer','lana']

result_of_course =["CMPS303","B+",3.5,True]

result_of_course.insert(4,"Spring2024")
result_of_course.append("repeated course")

# if 'nada' in names:
#     for x in names:
#         newList.append(x)
newList = [x for x in names if "sara" in names] #invalid syntax because x is needed in the begining 

info=[n for n in result_of_course if n != "repeated course" ] #accept all elements but repeated course. 
data=[n.upper() for n in result_of_course if isinstance(n,str) ] #accept all elements but repeated course. 


print(data)



# ==> change a value/s:
# names[1]='mansoor'
# result_of_course [:2]=["CMPS351","C+"]
# print(result_of_course[:6])
# print(names[:6])

# check if exist:
# if "B" in result_of_course:
#     print("yes")
# else:
#     print("nope")


##      ==> for print:
# for x in result_of_course:
#     print(x)
# for i in range(len(result_of_course)):
#     print(result_of_course[i])
#[print(x) for x in result_of_course]



#printing part :
#print(result_of_course[0:3]) #starting from the same point but the diff is print 3-1 so from index 0 til 2. 
#print(type(result_of_course))
#print(result_of_course[-1])


# ==> reminder!:
# insert needs a specific place/ index but append not. 
# del result_of_course remove the whole list
