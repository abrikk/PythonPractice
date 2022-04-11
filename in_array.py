def in_array(array1, array2):
    list_of_words = []
    for a in array1:
        for b in array2:
            if a in b and a not in list_of_words:
                list_of_words.append(a)
    return sorted(list_of_words)


print(in_array(['live', 'arp', 'strong'], ["lively", "alive", "harp", "sharp", "armstrong"]))
print(in_array(["tarp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))
