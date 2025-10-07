A, B, C, X = map(int, input().split())

if X < A:
  print(1)
elif X > B:
  print(0)
else:
  answer = C * (X - A) / (B - A)
  print(answer)