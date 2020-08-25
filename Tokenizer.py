fhand =open("sample_code.txt","r",encoding='utf-8')

keywords = ['for', 'if', 'elif', 'else', 'print']
separator = [';','(',')','{','}']
operator = ['+','-','/','%','*','++','<','>','=']
buffer = dict()

for str in fhand:
    # Separate code to identify strings with inverted commas

    while str.find('"')>=0:
        for i in range(len(str)):
            k = str[i]
            if k == '"':
                for j in range (i+1,len(str)):
                    l = str[j]
                    k = k+l
                    if l =='"':
                        str = str.replace(k,' ',1)
                        i = j+1
                        if k in buffer.keys():
                            buffer[k]+=1
                        else:
                            buffer.update({k: 1})
                        break
            if i >= len(str):
                break

    # Separate code to identify ++ operator

    while str.find('++')>=0:
        for i in range(len(str)-1):
            k = str[i]
            if k == '+':
                l = str[i+1]
                k = k+l
                if l =='+':
                    str = str.replace(k,'  ',1)
                    i = i+1
                    if k in buffer.keys():
                        buffer[k]+=1
                    else:
                        buffer.update({k: 1})
            if i >= len(str):
                break

    words = str.split()

    # identifying special characters and replacing them with a space

    for word in words:
        for i in range(len(word)):
            k = word[i]
            if k in separator:
                word = word.replace(k,' ',1)
                if k in buffer.keys():
                    buffer[k] += 1
                else:
                    buffer.update({k: 1})
            if k in operator:
                word = word.replace(k, ' ', 1)
                if k in buffer.keys():
                    buffer[k] += 1
                else:
                    buffer.update({k: 1})
        new_words = word.split()
        for new_word in new_words:
            if new_word in buffer.keys():
                buffer[new_word] += 1
            else:
                buffer.update({new_word: 1})

print("Lexeme, Token, Count")

for key in buffer:
    if key[0] == '"':
        print('Literal,', key+',', buffer[key])
    elif key in keywords:
        print('Keyword,', key+',', buffer[key])
    elif key in operator:
        print('Operator,', key+',', buffer[key])
    elif key in separator:
        print('Separator,', key+',', buffer[key])
    else:
        try:
            new_key = int(key)
            print('Literal,', key+',', buffer[key])
        except:
            print('Identifier,', key+',', buffer[key])


