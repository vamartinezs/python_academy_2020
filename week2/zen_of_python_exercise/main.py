import this
import codecs

new_block = "".join(map(lambda x: "*" if x.lower() in "aeiou" else x, codecs.encode(this.s, 'rot13')))
counter = new_block.count('*')

print("===============================================================================================================")
print(new_block)
print("vowels counter ", counter)
