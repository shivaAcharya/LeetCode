# @param {Integer[]} nums
# @return {Integer[]}
=begin
nums = [1, 2, 3, 4]
left = [1, 1, 2, 6]
right = [24, 12, 4, 1]
res = [24, 12, 8, 6]
=end
def product_except_self(nums)
    l = nums.length
    res = [1] * l
    
    (1...l).each do |i|
        res[i] = res[i - 1] * nums[i - 1]
    end
    
    right_prod = 1
    (l - 2).downto(0) do |i|
        right_prod *= nums[i + 1]
        res[i] *= right_prod
    end
    res
end