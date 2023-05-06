# df = pd.read_excel('bookid.xlsx',)
# channel_ids = df['IDS'].tolist()
# with open('channel_ids.txt', 'w') as f:
#     for channel_id in channel_ids:
#         f.write(channel_id + '\n')
# print(channel_ids)

# with open('category.txt') as f:
#     username = f.read().splitlines()
# print(username)

with open('ta.csv', mode='r') as f:
    print(f.readlines())
    # username = f.read().splitlines()
    # print(username)
