var lengthOfLongestSubstring = function(string) {
    let initial_index = 0;
    let maxLength = 0;
    const charIndex = {};
    for (let i = 0; i < string.length; i++) {
        const current_char = string[i];
        if (current_char in charIndex && charIndex[current_char] >= initial_index) {
            initial_index = charIndex[current_char] + 1;
        }
        charIndex[current_char] = i;
        maxLength = Math.max(maxLength, i - initial_index + 1)
    }
    return maxLength
}

const result = lengthOfLongestSubstring("aaaaa");
console.log(result)