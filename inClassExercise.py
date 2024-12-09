def main():
    """
    This program calls the arraySum() function three times with three different arrays, A, B, and C.
    """

    def arraySum(A, start, end):
        """
        Calculates the sum of elements in the array A within indices start and end.

        Parameters:
        A (list): The array to search.
        start (int): The starting index of the array.
        end (int): The ending index of the array.

        Returns:
        total_sum (int): The sum of all elements of the array.
        total_count (int): The total number of summations performed.
        """

        print("Input array: ", A[start:end+1])

        # Return the element in an array of size one.
        if (start == end):
            print("Returned value:", A[start])
            return A[start], 0
        
        # Recur the appropriate partition.
        else:
            mid = (start + end) // 2

            left_sum, left_count = arraySum(A, start, mid)
            right_sum, right_count = arraySum(A, mid+1, end)
            
            # Calculate the total sum and number of summations performed.
            total_sum = left_sum + right_sum
            total_count = left_count + right_count + 1

            print(f"Returning {left_sum} + {right_sum} =", total_sum)
            print("Number of sums executed:", total_count)
            return total_sum, total_count
    
    A = [38, 21, 39, 60, -1, 10, 81, 23]
    B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
    C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]

    print(f"(Final sum, number of sums) = {arraySum(A, 0, len(A) - 1)} \n")
    print(f"(Final sum, number of sums) = {arraySum(B, 0, len(B) - 1)} \n")
    print(f"(Final sum, number of sums) = {arraySum(C, 0, len(C) - 1)} \n")





    def merge(left, right):
        print(f"Input arrays: {left} and {right}")
        result, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if (left[i] <= right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        print(f"Sorted output array: {result}")
        return result
    
    def mergsort(A):
        print(f"Input array: {A}")
        if len(A) <= 1:
            print(f"Output array: {A}")
            return A
        else: 
            mid = len(A) // 2
            left = mergsort(A[:mid])
            right = mergsort(A[mid:])
            return merge(left, right)

    A = [38, 21, 39, 60, -1, 10, 81, 23]
    B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
    C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]

    print(mergsort(A))
    print(mergsort(B))
    print(mergsort(C))
# =============================================================

main()