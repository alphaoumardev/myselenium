import csv

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

df = pd.read_excel('bookid.xlsx',)
channels_id = df['IDS'].tolist()

with open('channel_ids.txt') as f:
    ids = f.read().splitlines()
# channel_usernames = ['javascriptmastery', 'mohamed_hoblos', 'CodingWithDawid', 'FoxNews', 'IdrissJAberkane']
# UCB0d0JLn1WcGYcwwZ87d2LA, UCBR8-60-B28hp2BmDPdntcQ
channels_ids = ['UC-lHJZR3Gqxm24_Vd_AJ5Yw', 'UCq-Fj5jknLsUf-MWSy4_brA', 'UCIwFjwMjI0y7PDBVEO9-bkQ', 'UC295-Dw_tDNtZXFeAPAW6Aw', 'UCJ5v_MCY6GNUBTO8-D3XoAg', 'UCRijo3ddMTht_IHyNSNXpNQ', 'UC0C-w0YjGpqDXGB8IHb662A', 'UCpEhnqL0y41EpW2TvWAHD7Q', 'UCfM3zsQsOnfWNUppiycmBuw', 'UCYvmuw-JtVrTZQ-7Y4kd63Q', 'UCqECaJ8Gagnn7YCbPEzWH6g', 'UCcgqSM4YEo5vVQpqwN-MaNw', 'UCp0hYYBW6IMayGgR-WeoCvQ', 'UCb2HGwORFBo94DmRx4oLzow', 'UCANLZYMidaCbLQFWXBC95Jg', 'UC9CoOnJkIBMdeijd9qYoT_g', 'UC-8Q-hLdECwQmaWNwXitYDw', 'UC20vb-R_px4CguHzzBPhoyQ', 'UC2xskkQVFEpLcGFnNSLQY0A', 'UCcMTZY1rFXO3Rj44D5VMyiw', 'UCRzzwLpLiUNIs6YOPe33eMg', 'UCZkURf9tDolFOeuw_4RD7XQ', 'UCGRtuAmEObNSmlOLDWzZfVg', 'UC4PooiX37Pld1T8J5SYT-SQ', 'UCi9cDo6239RAzPpBZO9y5SA', 'UCcdwLMPsaU2ezNSJU1nFoBQ', 'UCR4s1DE9J4DHzZYXMltSMAg', 'UCk8GzjMOrta8yxDcKfylJYw', 'UCfm4y4rHF5HGrSr-qbvOwOg', 'UC0WP5P-ufpRfjbNrmOWwLBQ', 'UCPDis9pjXuqyI7RYLJ-TTSA', 'UCpko_-a4wgz2u_DgDgd9fqA', 'UCuHzBCaKmtaLcRAOoazhCPA', 'UC_W0_Nv-3rxpWVvosddhrPw', 'UCcvNYxWXR_5TjVK7cSCdW-g', 'UCyxbZF7_PK4nLiexj0kkCNg',
                'UCUK0HBIBWgM2c4vsPhkYY4w', 'UCFFbwnve3yF62-tVXkTyHqg', 'UCbCmjCuTUZos6Inko4u57UQ', 'UCYLNGLIzMhRTi6ZOLjAPSmw', 'UCwppdrjsBPAZg5_cUwQjfMQ', 'UCWwWOFsW68TqXE-HZLC3WIA', 'UCaayLD9i5x4MmIoVZxXSv_g', 'UCjtLOfx1yt1NlnFIDyAX3Ug', 'UC-6czyMkxDi8E8akPl0c7_w', 'UCAvCL8hyXjSUHKEGuUPr1BA', 'UCxSz6JVYmzVhtkraHWZC7HQ', 'UComP_epzeKzvBX156r6pm1Q', 'UC4rlAVgAK0SGk-yTfe48Qpw', 'UCGnjeahCJW1AF34HBmQTJ-Q', 'UC3gNmTGu-TTbFPpfSs5kNkg', 'UC_aEa8K-EOJ3D6gOs7HcyNg', 'UCLsooMJoIpl_7ux2jvdPB-Q', 'UCF1JIbMUs6uqoZEY1Haw0GQ', 'UCJrDMFOdv1I2k8n9oK_V21w', 'UC4NALVCmcmL5ntpV0thoH6w', 'UCMu5gPmKp5av0QCAajKTMhw', 'UCrHL_BF5lHyK43BxLU8-vBQ', 'UCRv76wLBC73jiP7LX4C3l8Q', 'UC2pmfLm7iq6Ov1UwYrWYkZA', 'UCcgVECVN4OKV6DH1jLkqmcA', 'UC1SqP7_RfOC9Jf9L_GRHANg', 'UCKlhpmbHGxBE6uw9B_uLeqQ', 'UCMJ5Qf3sOvQpcYiai1Noa3Q', 'UC_vcKmg67vjMP7ciLnSxSHQ', 'UC65afEgL62PGFWXY7n6CUbA', 'UCKqH_9mk1waLgBiL2vT5b9g', 'UCY30JRSgfhYXA6i6xX1erWg', 'UCpDJl2EmP7Oh90Vylx0dZtA', 'UCa10nxShhzNrCE1o2ZOPztg', 'UCbW18JZRgko_mOGm5er8Yzg', 'UCsTcErHg8oDvUnTzoqsYeNw', 'UCPDXXXJj9nax0fr0Wfc048g',
                'UCa6vGFO9ty8v5KZJXQxdhaw', 'UCD1Em4q90ZUK2R5HKesszJg', 'UC6-F5tO8uklgE9Zy8IvbdFw', 'UCzVIrPfZBE-XkBISBybMBLA', 'UC4rasfm9J-X4jNl9SvXp8xA', 'UCmv1CLT6ZcFdTJMHxaR9XeA', 'UCpGdL9Sn3Q5YWUH2DVUW1Ug', 'UCN1hnUccO4FD5WfM7ithXaw', 'UCjK8ORC71kwyj1DWFwril_A', 'UC56gTxNs4f9xZ7Pa2i5xNzg', 'UCaWd5_7JhbQBe4dknZhsHJg', 'UC0VOyT2OCBKdQhF3BAbZ-1g', 'UCV9_KinVpV-snHe3C3n1hvA', 'UCJrOtniJ0-NWz37R30urifQ', 'UC1l7wYrva1qCH-wgqcHaaRg', 'UCMNmwqCtCSpftrbvR3KkHDA', 'UCw8ZhLPdQ0u_Y-TLKd61hGA', 'UCmBA_wu8xGg1OfOkfW13Q0Q',
                'UCM9r1xn6s30OnlJWb-jc3Sw', 'UCweOkPb1wVVH0Q0Tlj4a5Pw', 'UC55IWqFLDH1Xp7iu1_xknRA', 'UCVttQE6tS_agDSAU61Q65aA', 'UC6nSFpj9HTCZ5t-N3Rm3-HA', 'UC-yXuc1__OzjwpsJPlxYUCQ', 'UC9TO_oo4c_LrOiKNaY6aysA', 'UC3jOd7GUMhpgJRBhiLzuLsg', 'UChGJGhZ9SOOHvBB0Y4DOO_w', 'UCOsyDsO5tIt-VZ1iwjdQmew', 'UCgwv23FVv3lqh567yagXfNg', 'UClVrJwcIy7saPcGc1nct80A', 'UCF_fDSgPpBQuh1MsUTgIARQ', 'UCNL1ZadSjHpjm4q9j2sVtOA', 'UCClNRixXlagwAd--5MwJKCw', 'UCUtZaxDF3hD5VK4xRYFBePQ', 'UCoUM-UJ7rirJYP8CQ0EIaHA', 'UC7_YxT-KID8kRbqZo7MyscQ', 'UCEdvpU2pFRCVqU6yIPyTpMQ', 'UCBVjMGOIkavEAhyqpxJ73Dw', 'UCSAUGyc_xA8uYzaIVG6MESQ', 'UCDPM_n1atn2ijUwHd0NNRQw', 'UCZU9T1ceaOgwfLRq7OKFU4Q', 'UC48h7Dst_hX82HxOf3xJw_w', 'UCi8e0iOVk1fEOogdfu4YgfA', 'UCYVinkwSX7szARULgYpvhLw', 'UCsT0YIqwnpJCM-mx7-gSA4Q', 'UC3MLnJtqc_phABBriLRhtgQ', 'UCbTLwN10NoCU4WDzLf1JMOA', 'UCFkoPRmuxqr37jvGmmpzhzQ', 'UCRx3mKNUdl8QE06nEug7p6Q', 'UC9gFih9rw0zNCK3ZtoKQQyA', 'UC8-Th83bH_thdKZDJCrn88g', 'UCt-k6JwNWHMXDBGm9IYHdsg', 'UCLp8RBhQHu9wSsq62j_Md6A', 'UCnyB9MYKRkSFK3IIB32CoVw', 'UCdxi8d8qRsRyUi2ERYjYb-w',
                'UCMtpmPs9end-dTNwVq16g4Q', 'UCgc00bfF_PvO_2AvqJZHXFg', 'UC9zX2xZIJ4cnwRsgBpHGvMg', 'UCKAqou7V9FAWXpZd9xtOg3Q', 'UCpb_iJuhFe8V6rQdbNqfAlQ', 'UCP6uH_XlsxrXwZQ4DlqbqPg', 'UCEf_Bc-KVd7onSeifS3py9g', 'UCVp3nfGRxmMadNDuVbJSk8A', 'UCo_IB5145EVNcf8hw1Kku7w', 'UCNdqe5zJ6k-i7XKoYWA4Z2g', 'UCkvK_5omS-42Ovgah8KRKtg', 'UCyC_4jvPzLiSkJkLIkA7B8g', 'UCzTKskwIc_-a0cGvCXA848Q', 'UCppHT7SZKKvar4Oc9J4oljQ', 'UCBnZ16ahKA2DZ_T5W0FPUXg', 'UCYzPXprvl5Y-Sf0g4vX-m6g', 'UCS5Oz6CHmeoF7vSad0qqXfw', 'UCKqx9r4mrFglauNBJc1L_eg', 'UC6E2mP01ZLH_kbAyeazCNdg', 'UCaHNFIob5Ixv74f5on3lvIw', 'UCpB959t8iPrxQWj7G6n0ctQ', 'UCD9PZYV5heAevh9vrsYmt1g', 'UCm1dsgJNnhaLkY3uAdqN4mA', 'UCIjYyZxkFucP_W-tmXg_9Ow', 'UCX52tYZiEh_mHoFja3Veciw', 'UC-SV8-bUJfXjrRMnp7F8Wzw', 'UCT9zcQNlyht7fRlcjmflRSA', 'UC7TTtOQKMXTWWMtWQMIgVSA', 'UCG8rbF3g2AMX70yOd8vqIZg', 'UCsRM0YB_dabtEPGPTKo-gcw', 'UC22nIfOTM7KLIQuFGMKzQbg', 'UCWRV5AVOlKJR1Flvgt310Cw', 'UCAuUUnT6oDeKwE6v1NGQxug', 'UCmL1WlDI8UkXDXCXcBQN9CA', 'UCn7dB9UMTBDjKtEKBy_XISw', 'UCstEtN0pgOmCf02EdXsGChw',
                'UCN9HPn2fq-NL8M5_kp4RWZQ', 'UCaum3Yzdl3TbBt8YUeUGZLQ', 'UCrFiA0hztL9e8zTi_qBuW4w', 'UCyoXW-Dse7fURq30EWl_CUA', 'UCJ0uqCI0Vqr2Rrt1HseGirg', 'UCq3Ci-h945sbEYXpVlw7rJg', 'UCVtFOytbRpEvzLjvqGG5gxQ', 'UCAW-NpUFkMyCNrvRSSGIvDQ', 'UCwD4x63A9KC7Si2RuSfg-SA', 'UC6pjHMC4QXMi4llCCjtDXWg', 'UCIEv3lZ_tNXHzL3ox-_uUGQ', 'UCm3hAp1m1xlAz0ve_EKAo4g', 'UCDLmS9vkPcTz3cAc-c9QIzg', 'UC7eHZXheF8nVOfwB2PEslMw', 'UCpsSadsgX_Qk9i6i_bJoUwQ', 'UCf3cbfAXgPFL6OywH7JwOzA', 'UCGwPbAQdGA3_88WBuGtg9tw', 'UCC-RHF_77zQdKcA75hr5oTQ',
                'UCe4LM_eKc9ywRmVuBm5pjQg', 'UCNnwYefwrkVBAbMUzLpxbEQ', 'UCNhqvQMXIgRfjAGmxQqdNRw', 'UCwjoPtSoNLAoX2sLBaKLYng', 'UCKvn9VBLAiLiYL4FFJHri6g', 'UCn8zNIfYAQNdrFRrr8oibKw', 'UCshoKvlZGZ20rVgazZp5vnQ', 'UCelMeixAOTs2OQAAi9wU8-g', 'UCmKdSrwf1e8coqAzUsrVHZw', 'UCCI5Xsd_gCbZb9eTeOf9FdQ', 'UCgtNC51EUSgcZ6kKyVoPxKA', 'UC5H_KXkPbEsGs0tFt8R35mA', 'UCKy1dAqELo0zrOtPkf0eTMw', 'UCmh5gdwCx6lN7gEC20leNVA', 'UC6sSkkemzPjmrzS0Y0V_2zw', 'UCWr4vlkj5xXQ4bSXNeTT2AA', 'UC_TVqp_SyG6j5hG-xVRy95A', 'UC0v-tlzsn0QZwJnkiaUSJVQ', 'UCByOQJjav0CUDwxCk-jVNRQ', 'UCsPF3cApzCohxPp5oKdoWSQ', 'UCttspZesZIDEwwpVIgoZtWQ', 'UC2wKfjlioOCLP4xQMOWNcgg']


driver = webdriver.Chrome()
driver.maximize_window()

# Create a new CSV file to store the data
with open('channels2.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Platform', 'Avatar', 'Channel Name', 'Username', 'Channel Url', 'Location', 'Subscribers Count',
                     'Video count', 'Description', 'joined', 'Views', 'Email', '3 Latest Videos Url', '3 Latest Videos Title', '3 Latest videos image']) #'Latest Video 1', 'Latest Video 2', 'Latest Video 3'

    # Loop through each channel username and extract information
    for channel_id in channels_ids:

        # Visit the About page for the channel
        try:
            driver.get(f'https://www.youtube.com/channel/{channel_id}/about')
            driver.refresh()
        # Extract the channel name, subscribers, views, and description

            platform = 'Youtube'
            avatar = driver.find_element(By.XPATH, value='//*[@id="img"]').get_attribute('src')
            name = driver.find_element(by="xpath", value='//*[@id="text"]').text
            channel_username = driver.find_element(by="xpath", value='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[1]/yt-formatted-string[1]').text
            channel_url = driver.current_url
            location = driver.find_element(by='xpath', value='//*[@id="details-container"]/table/tbody/tr[2]/td[2]').text
            subscribers_count = driver.find_element(by="xpath", value='//*[@id="subscriber-count"]').text
            video_count = driver.find_element(by="xpath", value='//*[@id="videos-count"]/span[1]').text
            description = driver.find_element(by="xpath", value='//*[@id="description-container"]').text
            joined = driver.find_element(by="xpath", value='//*[@id="right-column"]/yt-formatted-string[2]/span[2]').text
            views = driver.find_element(by='xpath', value='//*[@id="right-column"]/yt-formatted-string[3]').text
            try:
                driver.execute_script("document.getElementById('email').style.display = 'block';")
                email = driver.find_element(by='xpath', value='//*[@id="email"]').get_attribute('href')
            except:
                print('email not found for this channel', channel_id)
            driver.implicitly_wait(3)

            driver.get(f'https://www.youtube.com/channel/{channel_id}/videos')
            driver.refresh()
            driver.implicitly_wait(1)
            # The latest videos url
            latest_videos_url = driver.find_elements(by='xpath', value='//*[@id="video-title-link"]')
            latest_video_url = [video.get_attribute('href') for video in latest_videos_url][:3]

            #The latest videos title
            latest_videos_title = driver.find_elements(by='xpath', value='//*[@id="video-title"]')
            latest_video_title = [title.get_attribute('aria-label') for title in latest_videos_title[:3]]

            # The latest videos image
            latest_videos_image = driver.find_elements(by='xpath', value='//*[@id="thumbnail"]/yt-image/img')
            latest_video_image = [image.get_attribute('src') for image in latest_videos_image[:3]]

            # Write the data to the CSV file
            writer.writerow([platform, avatar, name, channel_username, channel_url, location, subscribers_count, video_count, description, joined, views, email, latest_video_url, latest_video_title,  latest_video_image]) #latest_video_urls[0], latest_video_urls[1], latest_video_urls[2]
            driver.implicitly_wait(5)
        except:
            print('Channel not Found', channel_id)

# driver.quit()
