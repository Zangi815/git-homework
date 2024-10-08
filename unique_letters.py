def unique(word):

    unique = set()
    for i in word:
        if i in unique:
            return False
        unique.add(i)
    return True


print(unique("nigger"))  
print(unique("zangi"))  