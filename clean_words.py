l = []
with open('words.txt', 'r', encoding='utf-8') as buffer:
    l = (buffer.readlines())

print(l[10].split('\t')[0])

with open('new_words.txt', 'w', encoding='utf-8') as buffer:
    for l_ in l:
        new_line = l_.split('\t')[0]
        buffer.write(new_line+'\n')