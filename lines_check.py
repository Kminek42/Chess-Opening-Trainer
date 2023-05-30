import gameplay_variables

file = open(gameplay_variables.filename).readlines()
print(file)

doubled_lines = []


def equal(str1, str2):
    matching = True
    if len(str1) <= len(str2):
        for char in range(0, len(str1) - 2):
            if str1[char] != str2[char]:
                matching = False
    else:
        matching = False
    return matching


lines_to_remove = []

for string1 in file:
    for string2 in file:
        if string1 != string2:
            if equal(string1, string2):
                lines_to_remove.append(string1)
                print(string1, 'is in', string2)


print(lines_to_remove)

for i in lines_to_remove:
    if i not in doubled_lines:
        doubled_lines.append(i)

print(doubled_lines)

for line in doubled_lines:
    file.remove(line)

print('final file:', file)

new_file = open(gameplay_variables.filename, 'w')
for line in file:
    new_file.write(line)
