import random
import time
from typing import Dict, List

import requests

from scrap import InstagramScraper


class DiscoveryLogger:
    @staticmethod
    def print_log(msg):
        print("[DISCOVER BOT] {}".format(msg))


class DiscoverBot:
    def __init__(self):
        self.base_url = 'http://127.0.0.1:8000/api/'
        self.scraper = InstagramScraper()
        self.headers = {'Content-type': 'application/json', 'Accept': '*/*'}
        self.logger = DiscoveryLogger()

    def start_bot(self):
        self.logger.print_log('started bot.')
        categories = self.get_categories()
        if categories:
            for category in categories:  # category is a dict
                number_of_hashtags = random.randint(1, 6)
                self.logger.print_log("Number of hashtags random = {}".format(number_of_hashtags))
                self.logger.print_log("Looking for hashtags...")
                hashtags = self.get_hashtags_from_category(category.get("id"))
                if hashtags:
                    hashtags = hashtags[:number_of_hashtags]
                else:
                    self.logger.print_log("No hashtags to this category...")
                    continue
                self.discover_new_accounts_through_hashtags(hashtags, category)
                self.logger.print_log("Sleeping for next category...")
                time.sleep(random.randint(30, 100))
        self.logger.print_log("Finished.")

    def check_if_account_exists(self, username):
        self.logger.print_log("Checking if {} is in db.".format(username))
        link = "{}instagram_accounts?username={}".format(self.base_url, username)
        response = requests.get(link).json()
        if response:
            self.logger.print_log("Account exists.")
            return True
        return False

    def add_account_to_db(self, account: str, category: Dict):
        self.logger.print_log("Adding {} to db.".format(account))
        link_to_adding_account = '{}add_new_account/'.format(self.base_url)
        profile_page_metrics, profile_page_recent_posts = self.scraper.get_current_profile_info(account)
        body = {
            'account': account,
            'category': category,
            'profile_page_metrics': profile_page_metrics,
            'profile_page_recent_posts': profile_page_recent_posts,
        }
        r = requests.post(link_to_adding_account, json=body, headers=self.headers)
        if r.status_code == 200:
            return True
        else:
            return False

    def update_db_with_users(self, accounts: List[str], category: Dict):
        for account in accounts:
            if not self.check_if_account_exists(account):
                if self.add_account_to_db(account, category):
                    self.logger.print_log("Added account to db.")

                else:
                    self.logger.print_log("Something went wrong while adding {} account to db.".format(account))

    def discover_new_accounts_through_hashtags(self, hashtags: List[str], category: Dict):
        for hashtag in hashtags:
            accounts = self.scraper.discover_accounts_from_hashtag(hashtag)
            self.update_db_with_users(accounts, category)
            time.sleep(3)

    def get_categories(self):
        # {'id': 4, 'name': 'Technology'} <-- example of category
        link_to_categories = "{}categories".format(self.base_url)
        categories = requests.get(link_to_categories).json()
        return categories

    def get_hashtags_from_category(self, category_id):
        link_to_hashtags = "{}hashtags?category__id={}".format(self.base_url, category_id)
        hashtags = requests.get(link_to_hashtags).json()
        return [hashtag['name'] for hashtag in hashtags]


if __name__ == '__main__':
    bot = DiscoverBot()
    bot.start_bot()
