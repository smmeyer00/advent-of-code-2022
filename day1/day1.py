
with open('input.txt', 'r') as file:
    lines = file.readlines()

elfCals = [0]
curr = 0
for n in lines:
    n = n.strip()
    if n == '':
        curr += 1
        elfCals.append(0)
    else:
        elfCals[curr] = elfCals[curr] + int(n)

elfCals.sort(reverse=True)
print(f'Largest sum of calories: {elfCals[0]}')
print(f'Sum of top 3: {sum(elfCals[0:3])}')

