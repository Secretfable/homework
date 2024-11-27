my_dict = {"Masha":1998, "Oleg":2007, "Stepan":2000}
print(my_dict)
print(my_dict.get("Masha", "There isn't such person"))
print(my_dict.get("Natasha", "There isn't such person"))
my_dict.update({"Nikita":2001, "Olga":1987})
print(my_dict.pop("Oleg"))
print(my_dict.items())
my_set = {1,1,2,2,66,66,7,True,True,"hi","hi","hi"}
print(my_set)
my_set.add((5,6))
my_set.add(5)
my_set.discard(7)
print(my_set)