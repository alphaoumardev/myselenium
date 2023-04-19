from googleapiclient.discovery import build

def main():
    api_key = "AIzaSyBdwjJNyKfgs25Suh9gfXfz7Uxw00ztc-0"

    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.channels().list(part="statistics", forUsername="coreyms")
    response = request.execute()

    print("res")
    print(response)

if __name__ == "__main__":
    main()