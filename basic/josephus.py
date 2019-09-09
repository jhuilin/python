def josephus():
    person = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if person[index]:
            number += 1
            if number == 9:
                person[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for i,p in enumerate(person):
        print(i+1 if p else ',', end=' ')


if __name__ == "__main__":
    josephus()