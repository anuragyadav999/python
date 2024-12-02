a="krishna; institue's of 420 technology"
v=['a','e','i','o','u']
c=['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
co,vo=0,0
for i in a:
    for j in v:
        if i==j:
            vo+=1
    for k in c:
        if i==k:
            co+=1
print("Number of vowel in the string is ",vo)
print("Number of consonent in above string is ",co)