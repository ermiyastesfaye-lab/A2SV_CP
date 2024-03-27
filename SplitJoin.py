def split_and_join(line):
    line = line.split(" ")
    newLine = "-".join(line)
    return newLine


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
