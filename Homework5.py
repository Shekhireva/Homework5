immutable_var=("sweet", 1, 3, True, 'go', 5+1)
print(immutable_var)
#immutable_var[1][1]=2
#print(immutable_var)
#print(immutable_var) #error т.к. immutable_var  является кортежем, заменить его нельзя. Но до тех пор, пока не возьмешь нужные данные в скобки, сделав его списком.
mutable_list= ['sweet',0, 1, 3, True, 'go', '5+1']
mutable_list[3]=2
print(mutable_list)

