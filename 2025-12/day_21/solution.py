def solve(nums):
    new_arr = []
    
    if len(nums) == 1:
        return [0]
    
    total_product = 1
    for num in nums:
        total_product *= num

    for i in range(len(nums)):
        if nums[i] == 0:
            local_product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                local_product *= nums[j]
            new_arr.append(local_product)
        else:
            new_arr.append(total_product / nums[i])
    return new_arr


def solve_no_division(nums):
    res = [1 for _ in range(len(nums))]
    
    prod_left = 1
    for i in range(len(nums)):
        res[i] = prod_left
        prod_left *= nums[i]
        
    prod_right = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= prod_right
        prod_right *= nums[i]
    return res

        
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    res = solve_no_division(nums)
    print(res)
    assert res == [120, 60, 40, 30, 24]