def main():
    cards = list(map(int, input().split()))
    assert len(cards) == 5

    from collections import Counter
    count = Counter(cards)
    if sorted(count.values()) == [2, 3]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()