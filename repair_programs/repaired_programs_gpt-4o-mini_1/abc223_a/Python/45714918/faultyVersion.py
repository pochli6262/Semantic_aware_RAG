try:
    x = int(input())
    print('Yes' if x % 100 == 0 else 'No')
except ValueError:
    print('Invalid input, please enter an integer.')