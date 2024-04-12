# @param {String} s
# @return {Boolean}
def is_valid(s)
    brackets = {
        '(' => ')',
        '{' => '}',
        '[' => ']',
    }
    
    stack = []
    
    s.chars.each do |c|
        if brackets.key?(c)
            stack.push(brackets[c])
        elsif stack and stack.pop != c
            return false
        end
    end
    stack.empty?
end