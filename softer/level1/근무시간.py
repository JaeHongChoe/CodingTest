import sys

total =0

for _ in range(5):
    inn, out = input().split()

    inn_h, inn_m = map(int,inn.split(":"))
    out_h, out_m = map(int,out.split(":"))

    def num2(inn_h, inn_m,out_h, out_m):
        total_h = (out_h - inn_h) * 60
        total_m = out_m - inn_m

        total_t = total_h + total_m
        return total_t

    total += num2(inn_h, inn_m,out_h, out_m)

print(total)
