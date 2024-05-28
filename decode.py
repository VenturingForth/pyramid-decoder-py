def decode(message_file):
    f = open(message_file, "r")
    file = f.read().split("\n")
    dictionary = {}
    for num_word_pair in file:
        dictionary[num_word_pair.split()[0]] = num_word_pair.split()[1]
    step = 0
    increment = 1
    message = ""
    while step < len(dictionary):
        step += increment
        increment = increment + 1
        message += dictionary[f"{step}"] + " "
    return message

print(decode("message.txt"))