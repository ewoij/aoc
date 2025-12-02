txt = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

txt = open('2025/day/02/input.txt').read()

ranges = [tuple(map(int,v.split('-'))) for v in txt.split(',')]

print(ranges)


sum_ = 0

for start, stop in ranges:
    for i in range(start, stop+1):
        s = str(i)
        if len(s) % 2 == 0:
            m = len(s) // 2
            if s[:m] == s[m:]:
                print(s)
                sum_ += i

print(sum_)
