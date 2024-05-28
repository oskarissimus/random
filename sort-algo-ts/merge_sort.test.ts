import { merge, merge_sort } from "./merge_sort";
import { test, expect, it } from "@jest/globals";

it.each([
  [[1], [2], [1, 2]],
  [[1], [2, 3], [1, 2, 3]],
  [[2], [1, 3], [1, 2, 3]],
  [[3], [1, 2], [1, 2, 3]],
])(
  "merges %p and %p expecting %p",
  (l1: number[], l2: number[], expected: number[]) => {
    expect(merge(l1, l2)).toEqual(expected);
    expect(merge(l2, l1)).toEqual(expected);
  }
);

it.each([
  [[1], [1]],
  [
    [1, 2],
    [1, 2],
  ],
  [
    [2, 1],
    [1, 2],
  ],
  [
    [1, 2, 3],
    [1, 2, 3],
  ],
  [
    [1, 3, 2],
    [1, 2, 3],
  ],
  [
    [2, 1, 3],
    [1, 2, 3],
  ],
  [
    [2, 3, 1],
    [1, 2, 3],
  ],
  [
    [3, 1, 2],
    [1, 2, 3],
  ],
  [
    [3, 2, 1],
    [1, 2, 3],
  ],
])("sorts %p expecting %p", (l: number[], expected: number[]) => {
  expect(merge_sort(l)).toEqual(expected);
});
