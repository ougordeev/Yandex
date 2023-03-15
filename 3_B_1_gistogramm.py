import io
import sys
sys.stdin = io.StringIO('Twas brillig, and the slithy toves\nDid gyre and gimble in the wabe;\nAll mimsy were the borogoves,\nAnd the mome raths outgrabe.')

import sys

str1 = sys.stdin.read()

char_dict = {}
max_value = 0
for char in str1:
    if char not in {' ', '\n'}:
        current_value = char_dict.setdefault(char, 0)+1
        char_dict[char] += 1
        if current_value > max_value:
            max_value = current_value

keys_list  = sorted(char_dict.keys()).copy()
if not keys_list:
    sys.exit()

last_key = keys_list[-1]
while max_value > 0:
    for key in keys_list:
        if key in char_dict.keys():
            if char_dict[key] == max_value:
                print('#', end='')
                char_dict[key] -=1
                # if char_dict[key] == 0:
                #     del char_dict[key]
            else:
                print(' ', end='')
        else:
            print(' ', end='')
        if key == last_key:
            print()
    max_value -= 1
print (''.join(keys_list))
