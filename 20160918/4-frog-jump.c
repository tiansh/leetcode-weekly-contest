bool mayCross(int* stones, int stonesSize, int t) {
  if (stonesSize == 1) return true;
  int m = -1, k = -1, p = -1;
  for (int i = 1; i < stonesSize; i++) {
    if (stones[i] == stones[0] + t + 1) p = i;
    if (stones[i] == stones[0] + t ) k = i;
    if (stones[i] == stones[0] + t - 1) m = i;
    if (stones[i] > stones[0] + t + 1) break;
  }
  if (p != -1 && mayCross(stones + p, stonesSize - p, t + 1)) return true;
  if (k != -1 && mayCross(stones + k, stonesSize - k, t)) return true;
  if (m != -1 && mayCross(stones + m, stonesSize - m, t - 1)) return true;
  return false;
}

bool canCross(int* stones, int stonesSize) {
  if (stones[0] != 0 || stones[1] != 1) return false;
  return mayCross(stones + 1, stonesSize - 1, 1);
}


