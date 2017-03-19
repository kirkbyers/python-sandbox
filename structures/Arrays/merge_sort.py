def mergeSort(inp):
    result = []
    
    if len(inp) < 2:
        return inp
    middle = int(len(inp)/2)
    right = mergeSort(inp[:middle])
    left = mergeSort(inp[middle:])
    
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(right[0])
                right.pop(0)
            else:
                result.append(left[0])
                left.pop(0)
        elif len(right) > 0:
            for item in right:
                result.append(item)
                right.pop(0)
        else:
            for item in left:
                result.append(item)
                left.pop(0)
                
    return result
