def word_count(s):
    # Your code here
    dictionary = {}
    special_chars = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    string2 = ''.join(c.lower() for c in s if not c in special_chars)
    
    for word in string2.split():
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    
    return dictionary




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))