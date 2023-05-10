# [BOJ] 2665
# LEVEL : G4



# 8
# 11100110
# 11
#
#
#
#
#
#

import sys

n = int(sys.stdin.readline().rstrip())

maps = []

for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    maps.append(temp)

print(maps)