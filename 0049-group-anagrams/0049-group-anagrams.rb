# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
    groups = Hash.new {|hash, key| hash[key] = []}
    
    strs.each do |str|
        sorted_str = str.chars.sort.join
        groups[sorted_str].push(str)
    end
    groups.values
end