scores = [45, 12, 67, 23, 34, 9]

sorted_scores = []

for score in scores:
    if sorted_scores == []:
        sorted_scores.append(score)

    else: 
        inserted = False
        for i in range(len(sorted_scores)):
            if score < sorted_scores[i]:
                sorted_scores.insert(i, score)
                inserted = True
                break
        if not inserted:
            sorted_scores.append(score)

print(f'This is with for {sorted_scores}')


for i in range(1, len(scores)):
    key = scores[i]
    j = i - 1
    while j >= 0 and scores[j] > key:
        scores[j + 1] = scores[j]
        j -= 1
    scores[j + 1] = key

print(f'This is with while {sorted_scores}')


names = ["Zoe", "Alice", "John", "Bob", "Charlie"]
names_sorted = []
for name in names:
    if names_sorted == []:
        names_sorted.append(name)
    else:
        inserted = False
        for i in range(len(names_sorted)):
            if name < names_sorted[i]:
                names_sorted.insert(i, name)
                inserted = True
                break
        if not inserted:
            names_sorted.append(name)

print(f'This is with for {names_sorted}')


for i in range(1, (len(names))):
    key = names[i]
    j = i - 1
    while j >= 0 and names[j] > key:
        names[j + 1] = names[j]
        j -= 1
    names[j + 1] = key

print(f'This is with while {names}')

dates = ["2023-06-05", "2021-12-25", "2022-01-01", "2024-02-14"]

sorted_dates = []

for date in dates:
    if sorted_dates == []:
        sorted_dates.append(date)
    else:
        inserted = False
        for i in range(len(sorted_dates)):
            if date < sorted_dates[i]:
                sorted_dates.insert(i, date)
                inserted = True
                break
        if not inserted:
            sorted_dates.append(date)

print(f'This is with FOR {sorted_dates}')

for i in range(1, len(dates)):
    key = dates[i]
    j = i - 1 
    while j >= 0 and dates[j] > key:
        dates[j + 1] = dates[j]
        j -= 1 
    dates[j + 1] = key

print(f'This is with while {dates}')
