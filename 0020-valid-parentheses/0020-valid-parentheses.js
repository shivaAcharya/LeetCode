/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const openToCloseMap = new Map([
        ['(', ')'],
        ['{', '}'],
        ['[', ']']
    ]);
    
    var stack = [];
    
    for (let para of s){
        if (openToCloseMap.has(para)){
            stack.push(openToCloseMap.get(para));
        } else if((stack.length == 0) || (stack.pop() != para)){
            return false;
        }
    }
    
    return stack.length == 0;
    
};