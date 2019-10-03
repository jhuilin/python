def test(s):
    counter = 0
    current = None
    for i in range(len(s)):
        if counter == 0:
            current = s[i]
            counter = counter + 1
        elif s[i] == current:
            counter += 1
        else:
            counter -= 1
    print(str(current))

def main():
    s = 'abcbaba'
    test(s)

if __name__ == "__main__":
    main()