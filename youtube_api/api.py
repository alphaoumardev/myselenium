import time

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# api_key = "AIzaSyA7l-gbXF7MSg3R8szRrJNckQnyWBbGaGg"
api_key = "AIzaSyD5LYvlu9-q3UzNiOF7wA4RgiKNbvuvXPA"
try:

    youtube = build('youtube', 'v3', developerKey=api_key, )

    request = youtube.channels().list(part="statistics", forUsername="@FCCHKFCC", )
    response = request.execute()

    print("res")
    print(response)
except HttpError as error:
    if error.resp.status in [403, 500, 503]:
        time.sleep(3)
        # response = request.execute()

    else:
        raise
