def find_message(s_message):
    s_answer = ''
    l_words = s_message.split()
    for s_word in l_words:
        if len(s_word) > 0:
            s_letter = s_word[0]
            if s_letter.isupper():
                s_answer += s_letter[0]
    if len(s_answer) == 0:
        s_answer = 'No message found'
    return s_answer

print('First decryption is:')
print(find_message('How are you? Eh, ok. Low or Lower? Ohhh.'))
print('Second decryption is:')
print(find_message('hello world!'))