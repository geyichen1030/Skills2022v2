def unique_count(array):
    return len(set(array))

if __name__ == '__main__':
    array1 = [2,3,3,2]
    array2 = [1, 1, 1, 2]
    array3 = [1, 2, 3]
    print(unique_count(array1))
    print(unique_count(array2))
    print(unique_count(array3))