participant = ['Apeach', 'Ryan', 'Muzi', 'Choonsik', 'Neo', 'Tube']
completion = ['Ryan', 'Muzi', 'Neo', 'Choonsik']
unfinished = []

for i in participant:
    if i not in completion:
        unfinished.append(i)