# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
    s_counter = {}
    t_counter = {}
    
    s.chars.each do |c|
        if s_counter.key?(c)
            s_counter[c] += 1
        else
            s_counter[c] = 1
        end
    end
    
    t.chars.each do |c|
        if t_counter.key?(c)
            t_counter[c] += 1
        else
            t_counter[c] = 1
        end
    end
    s_counter == t_counter
end