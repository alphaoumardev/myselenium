import csv

from googleapiclient.discovery import build

api_key = ''
youtube = build('youtube', 'v3', developerKey=api_key)

next_page_token = None
channels = []
while len(channels) < 5000:
    request = youtube.channels().list(
        part='snippet,statistics',
        # chart='mostSubscribed',
        maxResults=50,
        pageToken=next_page_token
    )
    response = request.execute()
    channels += response['items']
    next_page_token = response.get('nextPageToken')
    if not next_page_token:
        break

with open('channels.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Views', 'Latest Video Links', 'Subscribers', 'Description', 'Links'])
    for channel in channels:
        channel_name = channel['snippet']['title']
        channel_views = channel['statistics']['viewCount']
        channel_subscribers = channel['statistics']['subscriberCount']
        channel_description = channel['snippet']['description']
        channel_link = f"https://www.youtube.com/channel/{channel['id']}"
        video_request = youtube.search().list(
            part='id',
            channelId=channel['id'],
            maxResults=3,
            order='date'
        )
        video_response = video_request.execute()
        video_links = [f"https://www.youtube.com/watch?v={video['id']['videoId']}" for video in video_response['items']]
        writer.writerow([channel_name, channel_views, video_links, channel_subscribers, channel_description, channel_link])
