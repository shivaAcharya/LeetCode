/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function(s) {
    let stack = [];
    
    for (c of s){
        // console.log(stack);
        if (c === '*'){
            stack.pop();
        } else {
            stack.push(c);
        }
    }
    
    return stack.join('');
};