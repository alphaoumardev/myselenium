import csv

# To remove the duplicate elements
# with open('category.txt', 'r') as file:
#     data = file.readlines()
#
# data = list(set(data))
#
# with open('category.txt', 'w') as file:
#     file.writelines(data)

# To remove the whitespace and replace it with + for YouTube search
# with open('categories.txt') as f:
#     lines = f.readlines()
#     # Remove empty lines
#     lines = [line.strip() for line in lines if line.strip()]
#     with open('categories.txt', 'w') as file:
#         for line in lines:
#             file.writelines(line.replace(' ', '+') + '\n')
# print(lines)

# To merge two csv files
# Open the first CSV file for reading
with open('channels3.csv', 'r', encoding='utf-8') as file1:
    reader1 = csv.reader(file1)
    data1 = list(reader1)

# Open the second CSV file for reading
with open('channels4.csv', 'r', encoding='utf-8') as file2:
    reader2 = csv.reader(file2)
    data2 = list(reader2)

# Combine the data from the two files
data = data1 + data2

# Open a new CSV file for writing
with open('channels.csv', 'w', newline='') as merged_file:
    writer = csv.writer(merged_file)

    # Write the combined data to the new file
    for row in data:
        writer.writerow(row)
