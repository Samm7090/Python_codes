def an_anagram(str1,str2):
    return sorted(str1)==sorted(str2)


print(an_anagram("Hello","World"))
print(an_anagram("silent","listen"))