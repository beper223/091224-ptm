"""
================================== Задача 1 ================================
Приходит текст из 5 строк.
Задача:
 - строка не должна начинаться с пробелов, допустима только табуляция (отступ).
 - сделать так, чтобы все предложения начинались с большой буквы;
 - не было подряд несколько пробелов и знаков пунктуации;
Не забывайте, что точка не всегда значит конец предложения! Например, и т.д. и т.п.
"""
text_str = """    \thello,,,, world.    how are you???    
    \t I'm fine, thank   you.     
\tI am fine too!!!     
Do you know what means "и т.д. и т.п."?
   \t   I'm fine. Thank you   for your question!           """


# =============== РЕЗУЛЬТАТ ==================
# 	Hello, world. How are you?
# 	I'm fine, thank you.
# 	I am fine too!
# Do you know what means "и т.д. и т.п."
# 	I'm fine. Thank you for your question!

# решение задачи
UNIQ_MARK = "!№;%:?"
PUNCTUATION_MARKS_AND_SPACE = " ,.:;!?"

lines = text_str.split('\n')
new_text = ''
i = 0
while i < len(lines):
    string = lines[i]
    # - строка не должна начинаться с пробелов, допустима только табуляция (отступ).
    # - сделать так, чтобы все предложения начинались с большой буквы;
    # - не было подряд несколько пробелов и знаков пунктуации;
    # - Не забывайте, что точка не всегда значит конец предложения! Например, и т.д. и т.п.

    string = string.replace('"и т.д. и т.п."', UNIQ_MARK)
    string = string.split('\t')

    n = 0
    while n < len(string):
        result = []
        prev_char = ''
        m = 0
        while m < len(string[n]):
            char = string[n][m]
            if char in PUNCTUATION_MARKS_AND_SPACE:
                if prev_char != char:
                    result.append(char)
            else:
                result.append(char)
            prev_char = char
            m += 1
        string[n] = ''.join(result)
        string[n] = string[n].strip()
        sentences = string[n].split('. ')
        l = 0
        while l < len(sentences):
            sentences[l] = sentences[l].capitalize()
            l += 1
        string[n] = '. '.join(sentences)
        n += 1
    string = "\t".join(string)
    string = string.replace(UNIQ_MARK, '"и т.д. и т.п."')
    new_text += string + '\n'
    i += 1

print(new_text)