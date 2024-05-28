export function merge_sort(l: number[]): number[] {
  if (l.length === 0) return l.slice();
  if (l.length === 1) return l.slice();
  const mid = Math.floor(l.length / 2);
  const left = l.slice(0, mid);
  const right = l.slice(mid);
  const left_sorted = merge_sort(left);
  const right_sorted = merge_sort(right);
  return merge(left_sorted, right_sorted);
}

export function merge(l1: number[], l2: number[]) {
  let i1 = 0;
  let i2 = 0;
  let result: number[] = [];
  while (i1 < l1.length && i2 < l2.length) {
    if (l1[i1] < l2[i2]) {
      result.push(l1[i1]);
      i1++;
    } else {
      result.push(l2[i2]);
      i2++;
    }
  }
  let l1_leftover = l1.slice(i1);
  let l2_leftover = l2.slice(i2);
  result.push(...l1_leftover);
  result.push(...l2_leftover);
  return result;
}
