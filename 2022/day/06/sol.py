chars = list(open('2022/day/6/input').read())[:-1]

for i in range(13, len(chars)):
    print(i, len(set(chars[i-13:i+1])) == 14)

