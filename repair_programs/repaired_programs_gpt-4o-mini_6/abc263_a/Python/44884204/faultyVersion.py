def main():
    from collections import Counter
    cards = list(map(int, input().split()))
    assert len(cards) == 5

    counts = Counter(cards)
    if sorted(counts.values()) == [2, 3]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()