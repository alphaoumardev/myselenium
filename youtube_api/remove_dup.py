# To remove the duplicate elements
# with open('category.txt', 'r') as file:
#     data = file.readlines()
#
# data = list(set(data))
#
# with open('category.txt', 'w') as file:
#     file.writelines(data)

# To remove the whitespace and replace it with + for YouTube search
with open('categories.txt') as f:
    lines = f.readlines()
    # Remove empty lines
    lines = [line.strip() for line in lines if line.strip()]
    with open('category1.txt', 'w') as file:
        for line in lines:
            file.writelines(line.replace('+', '%20') + '\n')
print(lines)
