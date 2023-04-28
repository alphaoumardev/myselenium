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
#
# import csv
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
#
# # Set up YouTube API credentials and service
# API_KEY = 'YOUR_API_KEY'
# YOUTUBE_API_SERVICE_NAME = 'youtube'
# YOUTUBE_API_VERSION = 'v3'
# youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
#
# # Open the input CSV file and create the output CSV file
# with open('input.csv', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
#     # Set up CSV readers and writers
#     input_reader = csv.reader(input_file)
#     output_writer = csv.writer(output_file)
#
#     # Write the header row to the output file
#     output_writer.writerow(['id', 'username', 'title', 'description'])
#
#     # Iterate over the input rows
#     for i, (id, username) in enumerate(input_reader):
#         try:
#             # Call the YouTube API to retrieve channel data by ID
#             response = youtube.channels().list(
#                 part='snippet',
#                 id=id
#             ).execute()
#
#             # Extract the relevant data from the API response
#             title = response['items'][0]['snippet']['title']
#             description = response['items'][0]['snippet']['description']
#
#             # Write the data to the output CSV file
#             output_writer.writerow([id, username, title, description])
#
#         except HttpError as error:
#             # Handle any errors that occur during the API call
#             print(f'An error occurred while searching for channel with ID {id}: {error}')
#
#         except IndexError:
#             # Handle the case where the API response does not contain any items
#             print(f'No channel found with ID {id}')
#
#         else:
#             # Print a message indicating that the channel data was successfully retrieved and stored
#             print(f'Channel data retrieved and stored for channel with ID {id} and username {username}')
