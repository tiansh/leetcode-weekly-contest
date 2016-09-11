// https://leetcode.com/contest/3/problems/utf-8-validation/

bool validUtf8(int* data, int dataSize) {
  int rem = 0;
  for (int i = 0; i < dataSize; i++, data++) {
    if (rem != 0 && (*data & 0x80) == 0) return false;
    else if (rem != 0 && (*data & 0x40) != 0) return false;
    else if (rem != 0) rem--;
    else if ((*data & 0x80) == 0) continue;
    else if ((*data & 0x40) == 0) return false;
    else if ((*data & 0x20) == 0) rem = 1;
    else if ((*data & 0x10) == 0) rem = 2;
    else if ((*data & 0x08) == 0) rem = 3;
    else if ((*data & 0x04) == 0) rem = 4;
    else if ((*data & 0x02) == 0) rem = 5;
    else if ((*data & 0x01) == 0) rem = 6;
    else return false;
  }
  return rem == 0;
}
