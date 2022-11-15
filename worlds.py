import time


def main():

    with open("all_worlds.txt") as text:
        read = text.read().split('\n')

    with open("5_len_worlds.txt", 'w') as out:
        read.sort(key=lambda x: len(x))

        for i in read:
            if len(i) == 5:
                out.write(i + "\n")
    with open("5_len_worlds.txt", 'r') as out:
        read_out = out.read().split()
        out_num = {'a': 0, 'h': 0, 'e': 0, 'd': 0, 'l': 0, 'i': 0, 'r': 0, 'g': 0, 'o': 0, 'n': 0, 'b': 0, 'c': 0, 'k': 0, 'f': 0, 't': 0, 'm': 0, 'p': 0, 's': 0, 'u': 0, 'v': 0, 'z': 0, 'y': 0, 'w': 0, 'x': 0, 'j': 0, 'q': 0}
        out_first_letter = {'a': 0, 'h': 0, 'e': 0, 'd': 0, 'l': 0, 'i': 0, 'r': 0, 'g': 0, 'o': 0, 'n': 0, 'b': 0, 'c': 0,
                   'k': 0, 'f': 0, 't': 0, 'm': 0, 'p': 0, 's': 0, 'u': 0, 'v': 0, 'z': 0, 'y': 0, 'w': 0, 'x': 0,
                   'j': 0, 'q': 0}
        out_vowels = {}



        for i in read_out:
            out_first_letter[i[:1]] += 1
            for j in i:
                if j in out_num:
                    out_num[j] += 1

        print(out_num)
        print(max(out_first_letter))

    # 15920, 370105



for i in range(1):
   main()
time_0 = time.time()
print("--- %s seconds ---" % ((time.time() - time_0) / 10))



