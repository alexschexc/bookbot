import functools


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    newText = text.lower()
    myDict = {}

    def reducer(counts, char):
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
        return counts
    myDict = functools.reduce(reducer, newText, myDict)
    return myDict

def report(myDict):
    newList = [{"char": char, "num": count} for char, count in myDict.items()]
    outList = sorted(newList, key=lambda item: item["num"], reverse=True)
    return outList
