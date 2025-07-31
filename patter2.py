import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    width = 4 * size - 3
    lines = []

    for i in range(size):
        # Get letters from current down to 'a' and back up
        chars = alphabet[size - 1:i:-1] + alphabet[i:size]
        line = '-'.join(chars).center(width, '-')
        lines.append(line)

    # Combine top (reversed) + bottom
    print('\n'.join(lines[::-1] + lines[1:]))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)