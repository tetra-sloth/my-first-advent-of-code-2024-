f = open("puzzle1_input.txt", "r")

l = f.readlines()

x = []
y = []

ans = 0

cl = [n.replace('\n', '') for n in l]

for i in cl:
    left, right = i.split()
    x.append(int(left))
    y.append(int(right))

x.sort()
y.sort()

for i in range(0, len(x)):

    if int(x[i]) > int(y[i]):
        ans += int(x[i]) - int(y[i])
    else:
        ans += int(y[i]) - int(x[i])

print(ans)