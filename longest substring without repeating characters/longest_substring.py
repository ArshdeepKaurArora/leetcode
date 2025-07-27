class Solution(object):
    def lengthOfLongestSubstring(self, s):
        initial_index = 0
        char_index = {}
        max_length = 0
        for i in range(len(s)):
            current_char = s[i]
            if current_char in char_index and char_index[current_char] >= initial_index:
                initial_index = char_index[current_char] + 1
            char_index[current_char] = i
            max_length = max(max_length, i - initial_index + 1)
        return max_length

if __name__ == "__main__":
    sol = Solution()
    result = sol.lengthOfLongestSubstring("aaaaaab")
    print(result)