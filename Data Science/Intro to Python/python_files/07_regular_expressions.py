import re # Import for regular expressions

patterns = ['term1','term2']

text = 'This is string with term1, not the other!'

for pattern in patterns:
    print('I am searching for: '+pattern)

    if re.search(pattern,text):
        print('Match Find')
    else:
        print('Match Not Find')


match = re.search('term1',text)
print(match.start())

### For Spliting terms into parts

split_term = '@'
email = 'wrt user@email.com'
split_mail = re.split(split_term,email)
print(split_mail)


#For finding all Matches
print(re.findall('match','test phrase match in middle match'))


def multi_find(patterns,phrase):
    for pat in patterns:
        print('searching for pattern {}'.format(pat))
        print(re.findall(pat,phrase))
        print('\n')


test_phrase = 'ssddd.sssd..ds.d..s.d.s.ds.dsjsjkflsjf.s.sjskfsl'
test_patterns = ['sd*']
multi_find(test_patterns,test_phrase)

test_phrase_2 = 'This is a string! But it has punctuation. How we can remove it?'
test_patterns_2 = ['[^!.?]+']
multi_find(test_patterns_2,test_phrase_2)
