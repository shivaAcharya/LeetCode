/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    
    max_candy = Math.max(...candies)
    const res = []
    //console.log(max_candy);
    for (candy of candies){
        if (candy + extraCandies >= max_candy){
            res.push(true);
        }
        else {
            res.push(false);
        }
    }
    
    return res;
    
};