def binarySearchRecursive(arr, left, right, target):

    if right >= left:

        mid = left + (right - left) / 2

        # If element is present at the middle itself
        if arr[mid] == target:
            return mid
        
        # If element is smaller than mid, then it 
        # can only be present in left subarray
        elif arr[mid] > target:
            return binarySearch(arr, left, mid-1, target)

        # Else the element can only be present 
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, right, target)

    else:
        # Element is not in the array
        return -1

def binarySearchIterative(arr, target):

	left = 0
	right = len(arr) - 1

    while left <= right:

        mid = left + (right - left) / 2

        # If element is present at the middle, return the mid index
        if arr[mid] == target:
            return mid
        
        # If element is smaller than mid, then reduce the array size
        # by setting the right to the midpoint
        elif arr[mid] > target:
            right = mid - 1

        # Element is greater than mid, so reduce array size by 
        # setting the left to the midpoint
        else:
            left = mid + 1

    else:
        # Element is not in the array
        return -1
