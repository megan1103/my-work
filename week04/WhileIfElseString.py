#Two examples of seeing if a word exists in another list
# The first option is complicated 

a = ['foo', 'bar', 'baz', 'corge']
s = 'corge'

#i = 0
#while i < len(a):
#     if a[i] == s:
#         # Processing for item found
#         break
#     #print(s, 'found in list.') 
#     i += 1
#else:
#     # Processing for item not found
#     print(s, 'not found in list.')

if s in a:
     print(s, 'found in list.')
else:
     print(s, 'not found in list.')