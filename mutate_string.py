def mutate_string(string,position,character):
    l=list(string)
    l[position]=character
    str1=''.join(l)
    return str1

if __name__== '__main__':
    s=input("Enter string: ")
    i, c=input("Enter position and char: ").split()
    new_str=mutate_string(s,int(i),c)
    print(new_str)