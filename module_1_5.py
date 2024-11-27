immutable_var = [0,2,4,"hello"],True,2,3,4,6,'Hy'
print(type(immutable_var))
# print(immutable_var[2])
# immutable_var[2]=3 #tuple does not support item assignment
print("Immutable tuple:",immutable_var)
mutable_list=[1,1,2,3,5]
print("Mutable list unchanged:",mutable_list)
mutable_list[0]=0
print("Mutable list changed:", mutable_list)