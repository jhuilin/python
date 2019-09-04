def isOneBitCharacter(bits: List[int]) -> bool:
    pos = 0
    while pos < len(bits) - 1:
        pos = pos + 2 if bits[pos] == 1 else pos + 1
    return pos == len(bits) - 1