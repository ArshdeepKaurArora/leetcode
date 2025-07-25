class Solution(object):
    def twoSum(self, nums, target):
        diff_dict = {}
        for i in range(len(nums)):
            complement = int(target) - int(nums[i])
            if complement in diff_dict:
                return [diff_dict[complement], i]
            diff_dict[nums[i]] = i
        return None

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    result = sol.twoSum(nums, target)
    print(result)

