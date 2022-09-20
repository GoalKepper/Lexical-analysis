def is_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


key_words_file = open('key_words_list.txt', 'r')
key_words_list = []
while True:
    line = key_words_file.readline()
    for word in line.split():
        key_words_list.append(word)
    if not line:
        break
key_words_file.close()

operators_file = open('operators_list.txt', 'r')
operators_list = []
while True:
    line = operators_file.readline()
    for word in line.split():
        key_words_list.append(word)
    if not line:
        break
operators_file.close()

brackets_file = open('brackets_list.txt', 'r')
brackets_list = []
while True:
    line = brackets_file.readline()
    for word in line.split():
        brackets_list.append(word)
    if not line:
        break
brackets_file.close()

separators_file = open('separators_list.txt', 'r')
separators_list = []
while True:
    line = separators_file.readline()
    for word in line.split():
        separators_list.append(word)
    if not line:
        break
separators_file.close()

is_text = False


input_code_file = open('input_code.txt', 'r')
lexical_analysis_file = open('lexical_analysis_result.txt', 'w')
input_lex = ''
cnt_lex = 1
while True:
    char = input_code_file.read(1)
    if not char:
        break

    if char == ' ' or char == '\n' or char == '\t' or char in brackets_list or input_lex == "//" or char in separators_list:
        if input_lex in key_words_list:
            lexical_analysis_file.write(str(cnt_lex) + ' #2 ' + input_lex + '\n')
            cnt_lex += 1
            input_lex = ''
        if input_lex in operators_list:
            lexical_analysis_file.write(str(cnt_lex) + ' #3 ' + input_lex + '\n')
            cnt_lex += 1
            input_lex = ''
        if input_lex == "/*":
            input_lex = ''
            while char:
                char = input_code_file.read(1)
                if char == "/" or char == "*":
                    input_lex += char
                else:
                    input_lex = ''
                if input_lex == "*/":
                    input_lex = ''
                    break
        elif input_lex == '//':
            input_lex = ''
            while char:
                char = input_code_file.read(1)
                if char == '\n':
                    input_lex = ''
                    break
        if input_lex in separators_list:
            lexical_analysis_file.write(str(cnt_lex) + ' #5 ' + input_lex + '\n')
            cnt_lex += 1
            input_lex = ''
        else:
            if input_lex != '' and input_lex[-1] in separators_list:
                input_lex = input_lex[:-1]
                char = input_lex[-1]
            if is_number(input_lex):
                lexical_analysis_file.write(str(cnt_lex) + ' #4 ' + input_lex + '\n')
                cnt_lex += 1
            elif input_lex != '':
                if is_number(input_lex[0]):
                    print('Error! Numeric literal with unexpected symbols!')
                    exit(1)
                else:
                    lexical_analysis_file.write(str(cnt_lex) + ' #1 ' + input_lex + '\n')
                    cnt_lex += 1
            input_lex = ''
            if char in separators_list:
                lexical_analysis_file.write(str(cnt_lex) + ' #5 ' + char + '\n')
                cnt_lex += 1
    else:
        input_lex += char

    if char in brackets_list:
        lexical_analysis_file.write(str(cnt_lex) + ' #6 ' + char + '\n')
        cnt_lex += 1
        if char == '"':
            input_lex = ''
            while char:
                char = input_code_file.read(1)
                if not char:
                    print('Error! Unexpected end of file!')
                    exit(1)
                if char == '"':
                    lexical_analysis_file.write(str(cnt_lex) + ' #4 ' + input_lex + '\n')
                    input_lex = ''
                    cnt_lex += 1
                    lexical_analysis_file.write(str(cnt_lex) + ' #6 ' + char + '\n')
                    cnt_lex += 1
                    break
                input_lex += char
        input_lex = ''

input_code_file.close()
lexical_analysis_file.close()
