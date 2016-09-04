// https://leetcode.com/contest/3/problems/decode-string/

var f = function (s) {
  return s.replace(/(\d+)\[([^\]\[]*)\]/g, function (_, n, t) { return t.repeat(n); });
};

/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    t = f(s);
    while (t != s) {
        s = f(t);
        t = f(s);
    }
    return t;
};

