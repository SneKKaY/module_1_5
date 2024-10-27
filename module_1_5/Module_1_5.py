Games = 'Witcher', 'Last of us', "Assassin's creed"
Rating = 5, 5, 4

immutable_var = ("Potato", 1, "Tomato", ['Witcher', 'Last of us', "Assassin's creed", 5, 5, 4], 1, 2 ,3)
print(immutable_var)
immutable_var[3][2] = 999
print(immutable_var)
#TypeError: 'tuple' object does not support item assignment. Картеж не изменяется. Но в него можно вписать список,
# который можно изменить)

mutable_list = ['L', 'O,', 'V', 'E']
mutable_list[0] = 'H'
mutable_list[1] = 'E'
mutable_list[2] = 'L'
mutable_list[3] = 'L'
print(mutable_list)
