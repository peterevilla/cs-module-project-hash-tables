def word_count(s):
    # Your code here
    cache = {}
    splitted = []
    for n in s.split():
        splitted.append(n.lower())

    for i in splitted:
        if i in cache:
            cache[i] += 1
        else:
            cache[i] = 1
    
    return cache




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))