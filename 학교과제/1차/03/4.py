students = ['Apeach', 'Ryan', 'Muzi', 'Choonsik', 'Neo', 'Tube']

res = sorted(students)

num = ['1', '2', '3', '4', '5', '6']

name_numbers = dict(zip(num, res))

print(name_numbers)

#name_numbers = {i + 1 : res[i] for i in range(len(res))}