def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    for i in range(len(arr)):
        left_to_right += arr[i][i]
    line = 0
    for i in range(-1, -len(arr)-1, -1):
        right_to_left += arr[line][i]
        line += 1
    return abs(left_to_right - right_to_left)
    # Write your code here

print(diagonalDifference([[1,2,3],[4,5,6],[9,8,9]]))