// https://leetcode.com/contest/3/problems/is-subsequence/

bool isSubsequence(char* s, char* t) {
  while (*s && *t) {
    if (*s == *t) s++;
    t++;
  }
  return !*s;
}

