def merge_sort_list(a,b):
    merge_1=[]

    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            merge_1.append(a[i])
            i += 1

        else:
            merge_1.append(b[j])
            j += 1

    
    while i<len(a):
        merge_1.append(a[i])
        i += 1

    while j<len(b):
        merge_1.append(b[j])
        j += 1

    return merge_1


a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
print(merge_sort_list(a, b))
