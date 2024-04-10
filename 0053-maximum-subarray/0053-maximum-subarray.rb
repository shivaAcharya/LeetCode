# @param {Integer[]} nums
# @return {Integer}
=begin
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_so_far = -inf
for num in nums
    max_so_far = max(max_so_far + num, num)
return max_so_far
=end
def max_sub_array(nums)
    max_so_far = -Float::INFINITY
    cur_sum = -Float::INFINITY
    nums.each do |num|
        cur_sum += num
        if cur_sum < num
            cur_sum = num
        end
        max_so_far = [max_so_far, cur_sum].max
    end
    max_so_far    
end