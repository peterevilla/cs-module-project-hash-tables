cache = {}
def no_dups(s):
    # Your code here
    n = []
    for word in s.split():
        if word in cache:
            pass
        else:
            n.append(word)
            cache[word] = word
    new_string = " ".join(n)

    return new_string




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))