# txt = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

txt = open('2025/day/02/input.txt').read()

ranges = [tuple(map(int,v.split('-'))) for v in txt.split(',')]

print(ranges)


sum_ = 0

invalids = set()

for start, stop in ranges:
    print(f'{start}-{stop}')
    for i in range(start, stop+1):
        s = str(i)
        for len_ in range(1, len(s) // 2 + 1):
            repeat = len(s) // len_
            if repeat * len_ == len(s):
                r = s[:len_] * repeat
                if s == r:
                    if int(r) not in invalids:
                        invalids.add(int(r))
                        print('    ', r)

print(sum(invalids))
