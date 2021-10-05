def palindrome(word, index):
    if index == len(word) // 2:
        return f'{word} is a palindrome'
    right_index = (-index)
    if index == 0:
        right_index = -1
    else:
        right_index += (-1)
    if word[index] == word[right_index]:
        return palindrome(word, index + 1)

    else:
        return f'{word} is not a palindrome'







print(palindrome('abcba', 0))
print(palindrome('peter', 0))
