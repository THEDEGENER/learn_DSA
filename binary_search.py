from random import randint

def binary_search(nums: list[int], target: int) -> int:
    # define the left and right pointers as index 0 and index -1 
    # and its none inclusive because we are using a while loop

    print(f"{target}")

    l = 0
    r = len(nums) - 1

    # these pointers will become closer and closer with each iteration so they cant go passed
    # each other because we would have either found the target or not
    while l <= r:
        # mid is defined by getting the length of the list as it chnages through the iteration
        # to constantly get the middle point, this works even tho the division is going to the nearest
        # whole number by rounding down if the target isnt equal to it then it shouldnt be included anyway
        mid = (l + r) // 2

        if target == nums[mid]:
            return nums[mid]

        if target < nums[mid]:
            # we ignore the right hand side by making the right pointer equal to mid minus 1 because it wasnt equal to mid anyway
            r = mid - 1
        
        if target > nums[mid]:
            # we ignore the left hand side by changing l to be mid plus 1 because it didnt equal the mid index anyway
            l = mid + 1
    
    return -1
        
if __name__ == "__main__":
    nums = [randint(0, 200) for _ in range(0, 200)]
    arr = sorted(nums)
    target = binary_search(arr, randint(0, 200))

    if target != -1:
        print(f"number was found {target}")
    else:
        print('number wasnt found')

