class Solution {
  twoSum(nums, target) {
    let index_dict = {};
    for (let i = 0; i < nums.length; i++) {
      let complement = target - nums[i];
      if (complement in index_dict) {
        return [index_dict[complement], i];
      }
      index_dict[nums[i]] = i;
    }
    return null;
  }
}

const nums = [2, 7, 11, 15];
const target = 9;
const solution = new Solution();
const result = solution.twoSum(nums, target)
console.log(result)