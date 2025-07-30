import textwrap

def wrap(string,width):
    return '\n'.join(textwrap.wrap(string,width))

if __name__=='__main__':
    string=input("Enter your string: ")
    width=int(input("Enter the width: "))

    result=wrap(string,width)
    print(result)