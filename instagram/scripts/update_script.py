import time

import requests

from scrap import InstagramScraper


class UpdateLogger:
    @staticmethod
    def print_log(msg):
        print("[UPDATE BOT] {}".format(msg))


class UpdateBot:
    def __init__(self):
        self.base_url = 'http://127.0.0.1:8000/api/'
        self.scraper = InstagramScraper()
        self.headers = {'Content-type': 'application/json', 'Accept': '*/*'}
        self.logger = UpdateLogger()

    def get_accounts_from_api(self):
        self.logger.print_log("Getting accounts from db.")
        link = "{}update_accounts/".format(self.base_url)
        response = requests.get(link).json()
        return response.get('accounts', [])

    def send_update_info_to_api(self, profile_page_metrics, profile_page_recent_posts, account):
        self.logger.print_log("Updating {}...".format(account))
        link = "{} update_accounts/".format(self.base_url)
        body = {
            'account': account,
            'profile_page_metrics': profile_page_metrics,
            'profile_page_recent_posts': profile_page_recent_posts,
        }
        r = requests.post(link, json=body, headers=self.headers)
        if r.status_code == 200:
            return True
        else:
            return False

    def iterate_through_accounts_and_update(self, accounts):
        for account in accounts:
            profile_page_metrics, profile_page_recent_posts = self.scraper.get_current_profile_info(account)
            self.send_update_info_to_api(profile_page_metrics, profile_page_recent_posts, account)
            time.sleep(2)

    def update_accounts(self):
        self.logger.print_log('started bot.')
        # it updates 50 accounts
        accounts = self.get_accounts_from_api()
        self.logger.print_log(f"Amount of accounts to update: {len(accounts)}")
        self.iterate_through_accounts_and_update(accounts)


if __name__ == '__main__':
    bot = UpdateBot()
    bot.update_accounts()
