# @param {Integer[]} nums
# @return {Integer}
def max_product(nums)
    cur_min_prod = cur_max_prod = 1
    max_prod = -Float::INFINITY
    
    nums.each do |num|
        values = [num, cur_min_prod * num, cur_max_prod * num]
        cur_min_prod = values.min
        cur_max_prod = values.max
        max_prod = [max_prod, cur_max_prod].max
    end
    max_prod
end