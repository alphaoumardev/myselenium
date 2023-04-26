from googleapiclient.discovery import build

api_key = "AIzaSyD5LYvlu9-q3UzNiOF7wA4RgiKNbvuvXPA"
try:

    youtube = build('youtube', 'v3', developerKey=api_key, )

    request = youtube.channels().list(part="statistics", forUsername="FCCHKFCC", )
    response = request.execute()

    print("res")
    print(response)
except:
    print("Something went wrong")
    # response = request.execute()
