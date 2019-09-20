if __name__ == '__main__':
    try:
        while True:
            string = input().strip()
            chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                     'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

            new_string = ''
            new_string1 = ''
            for each in string:
                if each not in chars:
                    new_string += each
                else:
                    new_string1 += each
            print(new_string + new_string1)
    except Exception as e:
        pass
