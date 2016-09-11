/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} query
 * @return {number[]}
 */
var calcEquation = function(equations, values, query) {
    var d = {};
    var v = [];
    var l = equations.length, i;
    for (i = 0; i < l; i++) {
        d[equations[i][0]] = d[equations[i][0]] || {};
        d[equations[i][1]] = d[equations[i][1]] || {};
        d[equations[i][0]][equations[i][1]] = values[i];
        d[equations[i][1]][equations[i][0]] = 1 / values[i];
    }
    var findAnswer = function (p, q) {
        var searched = [];
        if (!(p in d)) return -1;
        return (function find(p, q) {
            var result;
            if (d[p][q] != null) return d[p][q];
            searched.push(p);
            Object.keys(d[p]).some(function (k) {
                if (searched.indexOf(k) !== -1) return false;
                result = find(k, q);
                if (result == null) return false;
                result = d[p][k] * result;
                return true;
            });
            return result;
        }(p, q));
    };
    return query.map(function (q) {
       var answer = findAnswer(q[0], q[1]);
       if (answer == null) return -1;
       return answer;
    });
};
