import json
rock_dict = {'intents': []}
tags = ''
r = ''
patterns = []
responses = []
add = False
with open('tech_with_tim_chat/rock.txt', 'r', encoding='utf-8') as f:
    line = f.readlines()
    for l in line:
        if l.isupper():
            if 'ЕХ YU ROCK ENCIKLOPEDIJA' not in l:
                patterns.append(l[:-2])
                if r!='':
                    responses.append(r)
                else:
                    r=''
        elif 'ЕХ YU ROCK ENCIKLOPEDIJA' not in l: 
            if l[:-2][-1] == '-':
                r = r + l[:-3]
            else:
                r = r + l[:-2] + ' '
    responses.append(r)

for i in range(len(patterns)):
    new_dict = {
        'tags': patterns[i],
        'patterns': [patterns[i]],
        'responses': [responses[i]],
    }
    rock_dict['intents'].append(new_dict)

with open('tech_with_tim_chat/json_rock.json', 'w', encoding='utf-8') as f:
    json.dump(rock_dict, f)
print(len(responses))
print((patterns))

print(responses[0])
print(patterns[0])