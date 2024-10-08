def letter_count(letters):
    count_dict = {}
    for i in letters:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict


print(letter_count("hello"))  
