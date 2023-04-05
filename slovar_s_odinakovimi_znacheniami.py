amount = int(input())
child, food, slovar = [], [], {}

for i in range(amount):
	kid = input().split()
	child.append(kid[0])
	food.append(kid[1])

for i in range(len(child)):
	slovar[child[i]] = food[i]

which_food = input()

l = []
for value in slovar:
	if slovar.get(value) == which_food:
		l.append(value)

l=sorted(l)

if l! = []:
	for i in l:
		print(i)
else:
	print('Это блюдо никто не выбрал')




