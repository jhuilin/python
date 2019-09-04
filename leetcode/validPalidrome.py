
def isPalindrome(s) -> bool:
    cleanList = [c for c in s.lower() if c.isalnum()]
    return cleanList == cleanList[::-1]

def main():
    a = "A man, a plan, a canal: Panama"
    print(isPalindrome(a))

if __name__ == '__main__':
    main()