
bookInfo={
    'title' : 'pride and prejudice',
    'pagesNo' : 345,
    'author':'jane austen',
    'genre': 'romance',
    'got adapted?' : True  
}

# print(bookInfo)
#stored as key-value pairs, doesn't allow duplicate values and it's changeable 

# print(bookInfo['author'])
# print(bookInfo.get('pagesNo'))

# print(bookInfo.keys())

# print(bookInfo.items()) #return a tuple with each key-value pair.

# bookInfo.update({"pagesNo" : 456})
# print(bookInfo.items())

bookInfo["status"]="completed"
bookInfo["rate"]="4.8/5"
# del bookInfo["genre"] or
bookInfo.pop('genre')
print(bookInfo)

