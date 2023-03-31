import sys


def check_pw(pw):
    aeiou = ['a','e','i','o','u']
    flag1 = False
    for p in pw:
        if p in aeiou:
            flag1 = True
            break
    if not flag1:
        return False

    for i in range((len(pw)-2)):
        if (pw[i] in aeiou and pw[i+1] in aeiou and pw[i+2] in aeiou) or (pw[i] not in aeiou and pw[i+1] not in aeiou and pw[i+2] not in aeiou) :
            return False

    for i in range((len(pw)-1)):
        if pw[i] == pw[i+1] and pw[i] not in ['e','o']:
            return False

    return True


while True:
    inputs = sys.stdin.readline().rstrip()
    if inputs == 'end':
        break
    else:
        if check_pw(inputs):
            print(f'<{inputs}> is acceptable.')
        else:
            print(f'<{inputs}> is not acceptable.')