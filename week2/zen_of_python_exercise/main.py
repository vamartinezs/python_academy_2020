import this
import codecs

new_block = "".join(map(lambda x: "*" if x.lower() in "aeiou" else x, codecs.encode(this.s, 'rot13')))

print("## Solving it with Lambda function ##")
counter = new_block.count('*')
print("{} \n\nCounter of Vowels: {}".format(new_block, new_block.count('*')))
print("===============================================================================================================")




print("##  Try to solve it with Regex ##")

import re
new_re_block = re.sub("a|e|i|o|u|A|E|I|O|U", "*", codecs.encode(this.s, 'rot13'))
print("===============================================================================================================")
print("{} \n\nCounter of Vowels: {}".format(new_re_block,new_re_block.count('*')))