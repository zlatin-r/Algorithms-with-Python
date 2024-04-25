def find_all_solutions(index, t, w_by_idx, w_counts, used_words):
    if index >= len(t):
        print(" ".join(used_words))
        return

    if index not in w_by_idx:
        return

    for w in w_by_idx[index]:
        if w_counts[w] == 0:
            continue

        used_words.append(w)
        w_counts[w] -= 1

        find_all_solutions(index + len(w), t, w_by_idx, w_counts, used_words)

        used_words.pop()
        w_counts[w] += 1


words = input().split(", ")
target = input()

words_by_idx = {}
words_counts = {}

for word in words:
    if word in words_counts:
        words_counts[word] += 1
        continue

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

find_all_solutions(0, target, words_by_idx, words_counts, [])
