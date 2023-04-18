/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let idx1 = 0; 
    let idx2 = 0;
    let stringBuilder = [];
    const L1 = word1.length; L2 = word2.length;
    
    while (idx1 < L1 & idx2 < L2){
        stringBuilder.push(word1[idx1]);
        stringBuilder.push(word2[idx2]);
        idx1 += 1;
        idx2 += 1;
    }
    
    if (idx1 < L1){
        return stringBuilder.join('') + word1.slice(idx1);
    }
    return stringBuilder.join('') + word2.slice(idx2);
};