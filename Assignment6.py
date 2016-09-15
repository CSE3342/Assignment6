#Preston Tighe
#Assignment6
#9-15-16
#3342 Programming Languages

import re

a_good = ['A2', 'A77', 'AB2_7', 'B99999a']
a_bad = ['9A', '_A', '**Z']
b_good = ['A', 'B22+3*A/3', '-2+A+344/A99']
b_bad = ['A+', 'B+22V']


def a_search(input_string):
    test = re.match('[A-Za-z]\w*', input_string)
    return test is not None


def b_search(input_string):
    test = re.match('^(-)*(\d+|[A-Za-z]\w*)(\s*[/+\-*]\s*(-)*(\d+|[A-Za-z]\w*))*$', input_string)
    return test is not None


for test_string in a_good:
    print(test_string + ": " + str(a_search(test_string)))
print("")
for test_string in a_bad:
    print(test_string + ": " + str(a_search(test_string)))
print("")
for test_string in b_good:
    print(test_string + ": " + str(b_search(test_string)))
print("")
for test_string in b_bad:
    print(test_string + ": " + str(b_search(test_string)))


