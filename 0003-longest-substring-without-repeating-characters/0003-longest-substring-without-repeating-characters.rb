# @param {String} s
# @return {Integer}
=begin
last_seen = {
    p => 0,
    w => 2,
    k => 3,
    e => 4,
    
}
max_length = 3
l = 2
r = 4
s = "pwwkew"
          ^
=end
def length_of_longest_substring(s)
    
    last_seen = {}
    max_length = l = 0
    
    s.chars.each_with_index do |c, r|
        if last_seen.key?(c)
            l = [l, last_seen[c] + 1].max
        end
        max_length = [max_length, r - l + 1].max
        last_seen[c] = r
    end
    max_length
end