#taken from week 2, MIT algorithims class

def insertion_sort(A):
    """
    Sort list A into order, in place.

    From Cormen/Leiserson/Rivest/Stein,
    Introduction to Algorithms (second edition), page 17,
    modified to adjust for fact that Python arrays use 
    0-indexing.
    """
    for j in range(len(A)):
        key = A[j]
        # insert A[j] into sorted sequence A[0..j-1]
        i = j-1
        while i>-1 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A

def main():
    test_list = [4, 7, 9, 4, 5, 67, 234, 333, -2]
    print(test_list)
    sorted_list = insertion_sort(test_list)
    print(sorted_list)

if __name__ == "__main__":
    main()
    