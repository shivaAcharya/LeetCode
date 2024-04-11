# @param {Integer[]} nums
# @return {Integer}
=begin

nums = [3, 4, 5, 1, 2]
        l     m      r
compare with right element
    if m > r:
        move l to m + 1
    else
        move r to m
[1, 2]

[2, 1]
=end
def find_min(nums)
    l = 0
    r = nums.length - 1
    
    while l < r do
    
        mid = (l + r) / 2
        
        if nums[mid] > nums[r]
            l = mid + 1
        else
            r = mid
        end
    end
    nums[l]
    
end