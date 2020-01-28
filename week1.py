def alphabet_position(sentence):
    ans = ''
    for letter in sentence:
        if letter.isalpha() == True:
            if letter.isupper() == True:
                letter = letter.lower()
                ans += str(ord(letter)-96)
                ans += ' '
            else:
                ans += str(ord(letter)-96)
                ans += ' '       
    return ans.strip()

