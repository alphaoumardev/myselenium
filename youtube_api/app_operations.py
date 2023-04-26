# df = pd.read_excel('bookid.xlsx',)
# channel_ids = df['IDS'].tolist()
# with open('channel_ids.txt', 'w') as f:
#     for channel_id in channel_ids:
#         f.write(channel_id + '\n')
# print(channel_ids)
with open('ids.txt', 'r') as f:
    count = 0
    # for li in f:
    #     count += 1
    # print(count)
    username = f.read().splitlines()
    ids = [line.strip() for line in f]
    print(username)

# To remove the duplicate elements
# with open('category.txt', 'r') as file:
#     data = file.readlines()
#
# data = list(set(data))
#
# with open('category.txt', 'w') as file:
#     file.writelines(data)

# To remove the whitespace and replace it with + for YouTube search
# with open('category1.txt') as f:
#     lines = f.readlines()
# # Remove empty lines
#     lines = [line.strip() for line in lines if line.strip()]
#     with open('category1.txt', 'w') as file:
#         for line in lines:
#             file.writelines(line.replace(' ', '+') + '\n')
# print(lines)
