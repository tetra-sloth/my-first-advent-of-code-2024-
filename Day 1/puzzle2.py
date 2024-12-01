#both had same input
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

for i in x:

    for j in y:
        if i == j:
            ans += i

print(ans)
