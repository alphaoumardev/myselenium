# Importing the tiktok Python SDK
import sys

# Import JSON for export of data
import pandas as pd
from TikTokApi import TikTokApi as tiktok


# Conver processing code to function
def process_results(data):
    nested_values = ['video', 'author', 'music', 'stats', 'authorStats', 'challenges', 'duetInfo', 'textExtra',
                     'stickersOnItem']
    skip_values = ['challenges', 'duetInfo', 'textExtra', 'stickersOnItem']

    flattened_data = {}
    for idx, value in enumerate(data):
        flattened_data[idx] = {}
        for prop_idx, prop_value in value.items():
            if prop_idx in nested_values:
                if prop_idx in skip_values:
                    pass
                else:
                    # Loop through each nested property
                    for nested_idx, nested_value in prop_value.items():
                        flattened_data[idx][prop_idx + '_' + nested_idx] = nested_value
            # If it's not nested, add it back to the flattened dictionary
            else:
                flattened_data[idx][prop_idx] = prop_value

    return flattened_data


def get_data(hashtag):
    # Get cookie data
    verifyFp = "verify_kx2ee558_BH6fvQVi_cXHF_4lfK_Bimg_hH0lYMCV6Vm6"
    # Setup instance
    api = tiktok.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)
    # Get data by hashtag
    trending = api.by_hashtag(hashtag)
    # Process data
    # Convert the preprocessed data to a dataframe
    df = pd.DataFrame.from_dict(trending, orient='index')
    df.to_csv('tiktokdata.csv', index=False)


if __name__ == '__main__':
    get_data(sys.argv[1])
