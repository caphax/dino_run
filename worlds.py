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
        out_vowels = {'u': 0, 'o': 0, 'e': 0, 'a': 0, 'i': 0, 'y': 0, 'q': 0}
        out_consonants = {'h': 0, 'd': 0, 'l': 0, 'r': 0, 'g': 0, 'n': 0, 'b': 0, 'c': 0,
                   'k': 0, 'f': 0, 't': 0, 'm': 0, 'p': 0, 's': 0, 'v': 0, 'z': 0, 'w': 0, 'x': 0,
                   'j': 0}


        for i in read_out:
            out_first_letter[i[:1]] += 1
            for j in i:
                if j in out_vowels:
                    out_vowels[j] += 1
                else:
                    out_consonants[j] += 1
                if j in out_num:
                    out_num[j] += 1

        print('сколько букв:', out_num)
        print('самая частая первая буква:', max(out_first_letter, key=lambda x: out_first_letter[x]))
        print('гласные:', out_vowels)
        print('согласные:', out_consonants)
    # 15920, 370105



for i in range(1):
   main()
time_0 = time.time()
print("--- %s seconds ---" % ((time.time() - time_0) / 10))



