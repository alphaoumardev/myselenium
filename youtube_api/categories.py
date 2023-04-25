import csv
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# list of tags to search for
tags = ['python', 'javascript', 'machine+learning', 'data+science', 'web+development']

# configure chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # run Chrome in headless mode
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--start-maximized')

# create Chrome driver
driver = webdriver.Chrome()

# loop over tags
for tag in tags:
    driver.get(f"https://www.youtube.com/results?search_query={tag}&sp=EgIQAg%253D%253D")
    time.sleep(1)

    # Scroll down to load more channels
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    # find all channel elements and store in a list
    channels = driver.find_elements('xpath', '//*[@id="subscribers"]')

    # create a list of dictionaries with channel name and current tag
    channel_data = []
    for channel in channels:
        channel_dict = {'username': channel.text, 'current_tag': tag}
        channel_data.append(channel_dict)

    # write channel data to CSV file
    with open(f"cates.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["username", "current_tag"])
        writer.writeheader()
        for data in channel_data:
            writer.writerow(data)

# close Chrome driver
# driver.quit()

# mw6niii
# modicaderi
# imreneewinter
# essta0
# yushinoda0721
# musicadomomentos
# megaseries.panggilan
# projetomilionario.ofc
# emoneyhairsalon
# shahad.alsalal
# honarmandpluss
# powerboat.training
# ali798r
# ranandegi_aram
# n558__
# hunteredits_2.0
# inkedpeople__
# dr_omnia.elabd
# angelika_0723
# insta_rajasthani_official100k
# monnyhang_vee
# 6g_world_manjeri
# amandaferreira_master
# nutellaoopis
# pulgo_miguelzinho
# beauty.by.diba
# zohreh__araab
# taylorscosmos
# mathsolverr
# wearelindywell
# _messi__fanboy_
# deliteengineer
# elham_mohamadi_7
# mar1a.one
# matincars.ir
# diegodemivida
# brcentralesporte
# bherji_bhati_082
# look_like_mehndi_design
# majogomez_s
# by.rovik
# natural_skintips
# hoodskiiz
# parentinganakofficial
# schad_ape_
# van_world_of_martial_arts
# versoedificante
# j0.ivyy
# receitasfitness_faceis_
# remix___reels_
# 708l9
# pedarkhoondeh
# saint4taylor
# dharmastatuesindia
# pp5y1
# elithepianist
# olesya_tarasenko__
# guaracyjr_
# kedar__0810
# sachellsmit
# live_vijay_jornang132
# benim_guncem0061
# dra.nataliakarolina
# mosbatt_andishann
# evolvewithseemapuri
# arislonraximov
# marianitaaa68
# doganhabermaras
# stylekingkumar_official
# pollypastel_
# _duaa91
# azorelius
# sahm_team
# official_dallu_02
# alexernum
# mustafagorkemozdemir10
# imranriazkhan.pk
# cecilewolfromoff
# kobra6uno
# lojasfmstore
# hassan.ilyas.sh
# shikayaatein
# earnie.finance
# puja_palash_halder
# sk.indonesia
# shams_forex
# bundeli_ankesh
# hanmade.details
# kitteno0o
# sonam__rajput.78
# itsericarayy
# shelby_sonhador
# astana_vites
# promo_verified
# vidadosfamososonline
# r2ioj
# aufeventofficial
# p66qv
# ashok_todmal
# lianacardinalle_