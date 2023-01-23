# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

data = [12, "sadf", 4543, 9483, "aezakmi"]
print(data)
newlist = list(filter(lambda x: type(x) == int,data))
newlist2 = list(filter(lambda x: type(x) == str,data))
print(f'number: {newlist}')
print(f'string: {newlist2}')