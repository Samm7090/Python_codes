def reverse_string(s):
    return ' '.join(s.split()[::-1])

if __name__=="__main__":
    s=input("Enter the sentence: ")

    print(reverse_string(s))
