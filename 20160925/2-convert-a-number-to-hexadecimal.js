/**
 * @param {number} num
 * @return {string}
 */
var toHex = function(num) {
    if (num == 0) return '0';
    num = num >>> 0;
    var output = '';
    while (num) {
        output = '0123456789abcdef'[num & 15] + output;
        num = num >>> 4;
    }
    return output;
};

