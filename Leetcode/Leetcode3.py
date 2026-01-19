def reverseVowels(str1):
    result=''
    vowels=('I', 'e', 'u', 'A','o')
    used = set()
    for x in range(len(str1)):
        if str1[x].lower() in [v.lower() for v in vowels]:
            for item in range(len(str1)-1,-1,-1):
                if str1[item].lower() in [v.lower() for v in vowels] and str1[item] not in used :
                    result+=str1[item]
                    used.add(str1[item])
                    break
                    
                
        else :        
            result+=str1[x]
    return result
        


print(reverseVowels('IceCreAm'))