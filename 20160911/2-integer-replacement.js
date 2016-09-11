var cache = [0, 0, 1, 2, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5, 5, 5, 4, 5, 5, 6, 5, 6, 6, 6, 5, 6, 6, 7, 6, 7, 6, 6, 5, 6, 6,
 7, 6, 7, 7, 7, 6, 7, 7, 8, 7, 8, 7, 7, 6, 7, 7, 8, 7, 8, 8, 8, 7, 8, 8, 8, 7, 8, 7, 7, 6, 7, 7, 8, 7, 8,
 8, 8, 7, 8, 8, 9, 8, 9, 8, 8, 7, 8, 8, 9, 8, 9, 9, 9, 8, 9, 9, 9, 8, 9, 8, 8, 7, 8, 8, 9, 8, 9, 9];
/**
 * @param {number} n
 * @return {number}
 */
var integerReplacement = function(n) {
    if (n < 100) return cache[n];
    switch (n % 4) {
        case 0: case 2: return integerReplacement(n / 2) + 1;
        case 1: return integerReplacement((n - 1) / 4) + 3;
        case 3: return integerReplacement((n + 1) / 4) + 3;
    }
};
