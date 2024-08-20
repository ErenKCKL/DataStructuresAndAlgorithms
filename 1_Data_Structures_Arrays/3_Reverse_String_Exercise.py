# A string is given. We have to print the reversed string.
# For example, the string is "Hi how are you?"
# The output should be "?ouy era woh iH"

def reverse_string(string):
    new_string = []
    for i in range(len(string) -1, -1, -1):
        new_string.append(string[i])
    return ''.join(new_string)

string = "Hi how are you?"
print(reverse_string(string))

