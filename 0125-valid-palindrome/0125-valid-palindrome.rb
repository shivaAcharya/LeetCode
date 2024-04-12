# @param {String} s
# @return {Boolean}
def is_palindrome(s)
    l = 0
    r = s.length - 1
    
    while l < r
        if not s[l].match?(/[a-zA-Z0-9]/)
            l += 1
        elsif not s[r].match?(/[a-zA-Z0-9]/)
            r -= 1
        elsif s[l].downcase != s[r].downcase
            return false
        else
            l += 1
            r -= 1
        end
    end
    true
end