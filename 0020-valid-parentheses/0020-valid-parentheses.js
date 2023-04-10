/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const map = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    };
    let stack = [];
    
    for (para of s){
        if (para in map){
            stack.push(map[para]);
        } else if (stack.length == 0 || stack.pop() != para){
            return false;
        }
        
    }
    
    return stack.length == 0;
};