def lomuto(A, left, right):
    p = A[right]
    i = left
    count = 0
    for j in range(left, right):
        # print(A)
        if A[j] > p:
            # print("switching", A[i], A[j])
            A[i], A[j] = A[j], A[i]
            i += 1
            count += 1
    # print("NOW switching", A[i], A[right])
    A[i], A[right] = A[right], A[i]
    count += 1
    # print("COUNT" , count)
    return i, count

def quicksort(A, left, right, calls):
    if (left < right):
        calls += 1
        mid, swaps = lomuto(A, left, right)

        leftSwaps, calls  = quicksort(A, left, mid-1, calls)
        rightSwaps, calls = quicksort(A, mid+1, right, calls)

        totalSwaps = leftSwaps + rightSwaps + swaps
        return totalSwaps, calls
    return 0, calls

A = [38, 21, 39, 60, -1, 10, 81, 23]
B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]

print(f"A: (Number of swaps, number of recursive calls) = {quicksort(A, 0, len(A)-1, 0)}")
print("A =", A)
print(f"B: (Number of swaps, number of recursive calls) = {quicksort(B, 0, len(B)-1, 0)}")
print("B =", B)
print(f"C: (Number of swaps, number of recursive calls) = {quicksort(C, 0, len(C)-1, 0)}")
print("C =", C)