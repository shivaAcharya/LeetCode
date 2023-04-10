/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const openToCloseMap = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    };
    
    var stack = [];
    
    for (let para of s){
        if (para in openToCloseMap){
            stack.push(openToCloseMap[para]);
        } else if((stack.length == 0) || (stack.pop() != para)){
            return false;
        }
    }
    
    return stack.length == 0;
    
};