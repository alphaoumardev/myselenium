from googleapiclient.discovery import build

api_key = "AIzaSyA7l-gbXF7MSg3R8szRrJNckQnyWBbGaGg"
try:

    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.channels().list(part="statistics", forUsername="coreyms")
    response = request.execute()

    print("res")
    print(response)
except Exception as e:
    print(e)

