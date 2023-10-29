import difflib
#str1 = difflib.get_close_matches('ruža', ['ruže', 'ruži', 'ružo', 'boris'])
#print(str1)

a = 'ruži'
b = 'ruža'

seq = difflib.SequenceMatcher(None,a,b)
d = seq.ratio()*100
print(d)