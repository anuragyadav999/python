a="Anurag Yadav"
num=['0','1','2','3','4','5','6','7','9']
c=0
for i in a:
    for j in num:
        if i==j:
            print("Alphanumeric")
            c+=1
if c==0:
    print("It is not alphanumeric")