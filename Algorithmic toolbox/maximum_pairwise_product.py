import heapq

# Only works with positive numbers
'''def max_pairwise_product(nums):
    if len(nums) < 2:
        return "There are no pairs."
    
    top_two = heapq.nlargest(2, nums)
    return top_two[0] * top_two[1]'''


# Brute force approach - check every possible pair. 
# Time complexity: O(n^2)
# Aux space: O(1)
'''def max_pairwise_product(nums):
    n = len(nums)

    if n < 2:
        return
    if n == 2:
        return nums
    
    # Initialize the first pair
    a = nums[0]
    b = nums[1]

    for i in range(0, n):
        for j in range(i + 1, n):
            if nums[i] * nums[j] > a * b:
                a = nums[i]
                b = nums[j]
    
    return f"{a}, {b}"'''

# Positive numbers, algorithm from scratch
'''def max_pairwise_product(nums):
    n = len(nums)

    if n < 2: return
    if n == 2: return nums 

    index1 = -1
    for i in range(0, n):
        if index1 == -1 or nums[i] > nums[index1]:
            index1 = i 

    index2 = -1
    for j in range(0, n):
        if j == index1: continue
        if index2 == -1 or nums[j] > nums[index2]:
            index2 = j

    return f"{nums[index1]}, {nums[index2]}"'''


# Sort the list, compare product of two first and last numbers
# Returns positive if the products are equal
# Time complexity: O(nlog(n))
# Aux space: O(1)
'''def max_pairwise_product(nums):
    n = len(nums)

    if n < 2: return 
    if n == 2: return nums

    nums.sort()

    product_neg = nums[0] * nums[1]
    product_pos = nums[n - 1] * nums[n - 2]

    if product_neg > product_pos:
        return f"{nums[0]}, {nums[1]}" 
    return f"{nums[n - 1]}, {nums[n - 2]}"'''


# Find two largest positive numbers and two largest negative numbers
# Compare the products 
# Returns positive when the products are equal
# Time complexity: O(n)
# Aux space: O(1)
def max_pairwise_product(nums):
    n = len(nums)

    if n < 2: return
    if n == 2: return nums

    # Initialize maximum and second minimum
    posa = 0
    posb = 0

    # Initialize minimum and second minimum
    nega = 0
    negb = 0

    # Traverse given array
    for i in range(n):
        # Update positive maximum numbers
        if nums[i] > posa:
            posb = posa
            posa = nums[i]
        elif nums[i] > posb:
            posb = nums[i]

        # Update minimum and second minimum if needed
        if nums[i] < 0 and abs(nums[i]) > abs(nega):
            negb = nega
            nega = nums[i]
        elif nums[i] < 0 and abs(nums[i]) > abs(negb):
            negb = nums[i]

    if nega * negb > posa * posb:
        return f"{nega}, {negb}"
    return f"{posa}, {posb}"  


if __name__ == '__main__':
    numbers = [10, -20, 2, 5, 6, 9, -20, 20, 20] 
    print(f"Maximum pairwise product: {max_pairwise_product(numbers)}")