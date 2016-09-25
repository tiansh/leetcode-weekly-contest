/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function (people) {
  var sorted = people.sort(function (x, y) {
    if (x[1] != y[1]) return x[1] - y[1];
    return x[0] - y[0];
  }), l = sorted.length;
  var output = [], i, j;
  for (i = 0; i < l; i++) {
    var current = sorted[i], before = current[1];
    for (j = 0; j < i; j++) {
      if (output[j][0] >= current[0]) {
        if (!before--) break;
      }
    }
    output.splice(j, 0, current);
  }
  return output;
};

