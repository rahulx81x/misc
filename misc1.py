
length = int(input())
string = list(map(int,(input().split())))
string.sort()
done=[]
for i in range(length):
    if string[i] not in done:
        if string[i] > i+1:
            print(-1)
        elif string[i] == i+1:
            pass
        else:
            for j in range(i,length+1):
                if j not in string:
                    string[i] = j
                    done.append(j)
                    break
print(len(done))
print(string)
