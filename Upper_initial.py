def solve(s):
    #return s.title()
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
        s = input("Enter name: ")
        result = solve(s)

        print(result)