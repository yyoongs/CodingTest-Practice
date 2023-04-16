number = "1233210120321"

idx = 0
count = 0
temp = ""

while idx < len(number):
    print(count,temp,idx)
    count += 1
    temp += number[idx]
    if number[idx] == '0':
        idx+=1
        continue
    elif idx == len(number)-1:
        count += 1
        break
    elif number[idx+1] == str(int(number[idx])+1):
        temp += str(int(number[idx])+1)
        idx += 2
        continue
    else:
        count+=1
        idx += 1

print(temp)
print(count)