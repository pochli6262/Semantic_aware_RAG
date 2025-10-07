import sys

input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

def main():
    N = int(input())
    l = []
    for i in range(N):
        a, b = map(int, input().split())
        l.append((-a, i + 1))  # Fixed line here
    l.sort()
    for i in range(N):
        print(l[i][1], end=' ')
    print()

if __name__ == '__main__':
    main()