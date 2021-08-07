n = int(input())  # no. of monsters
e = int(input())  # initial exp
p = []     # power points of monsters
b = []     # bonus exp after defeating monster
# for victory exp >= power
for i in range(n):
    p.append(int(input()))
for j in range(n):
    b.append(int(input()))
p_b = sorted(zip(p, b))
power = []
bonus = []
for i in range(n):
    power.append(p_b[i][0])
    bonus.append(p_b[i][1])
kill_count = 0

for k in range(len(power)):
    if e >= power[k]:
        kill_count += 1
        e += bonus[k]

print(kill_count)
