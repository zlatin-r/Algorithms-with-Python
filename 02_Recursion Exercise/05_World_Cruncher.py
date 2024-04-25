words = input().split(", ")
target = input()

words_by_idx = {}
words_counts = {}

for word in words:
    if word in words_counts:
        words_counts[word] += 1
    else:
        words_counts[word] = 1

    try:
        idx = 0
        while True:
            idx = target.index(word, idx)

            if idx not in words_by_idx:
                words_by_idx[idx] = []
            words_by_idx[idx].append(word)
            idx += len(word)
    except ValueError:
        pass


def find_all_solutions(index, w_by_idx, w_counts, used_words):
    if index not in w_by_idx:
        return

    for w in w_by_idx[index]:
        used_words.add(w)
        w_counts[w] -= 1

        find_all_solutions(index + len(w), w_by_idx, w_counts, used_words)

        used_words.pop(w)
        w_counts[w] += 1


find_all_solutions(0, words_by_idx, words_counts, [])
