# df = pd.read_excel('bookid.xlsx',)
# channel_ids = df['IDS'].tolist()
# with open('channel_ids.txt', 'w') as f:
#     for channel_id in channel_ids:
#         f.write(channel_id + '\n')
# print(channel_ids)

with open('channel_ids.txt') as f:
    ids = f.read().splitlines()
print(ids)