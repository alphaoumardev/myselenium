import time

import requests

from scrap import InstagramScraper


class HashtagLogger:
    @staticmethod
    def print_log(msg):
        print("[HASHTAG BOT] ".format(msg))


class HashtagScript:

    def __init__(self, category, basic_hashtags):
        self.scraper = InstagramScraper()
        self.base_url = 'http://127.0.0.1:8000/api/'
        self.category = category.title()
        self.basic_hashtags = basic_hashtags
        self.headers = {'Content-type': 'application/json', 'Accept': '*/*'}
        self.logger = HashtagLogger()

    def __call__(self, *args, **kwargs):
        self.add_category_to_db()

    def check_current_hashtags(self):
        links_to_hashtags = '{} hashtags?category__name={}'.format(self.base_url, self.category)
        try:
            response = requests.get(links_to_hashtags).json()
            return response
        except Exception as e:
            self.logger.print_log(' ERROR - {}'.format(e))

    def check_amount_current_hashtags(self):
        return len(self.check_current_hashtags())

    def find_new_hashtags(self):
        print('finding new hastags')
        all_hashtags = set(self.basic_hashtags)
        for hashtag in self.basic_hashtags:
            time.sleep(2)
            print("Looking for related hashtags to: ", hashtag)
            related_hashtags = self.scraper.discover_hashtags(hashtag)
            all_hashtags.update(related_hashtags)
        print('all hashtags: ', all_hashtags)
        return all_hashtags

    def add_new_hashtags_to_db(self, category_id):
        hashtags = self.find_new_hashtags()
        link_to_adding_hashtag = '{} add_multi_hashtags/'.format(self.base_url)
        body = {
            "category_id": int(category_id),
            "hashtags": list(hashtags)
        }
        r = requests.post(link_to_adding_hashtag, json=body, headers=self.headers)
        if r.status_code == 200:
            return True
        else:
            return False

    def __add_category(self):
        link_to_category = '{} categories'.format(self.base_url)
        body = {
            "name": "{}".format(self.category.title())
        }
        r = requests.post(link_to_category, json=body, headers=self.headers)
        if r.status_code == 201:  # created
            self.logger.print_log('Added new category to db: {}'.format(r.json()))
            return True
        else:
            self.logger.print_log('Something went wrong: {}'.format(r.json()))
            raise

    def add_category_to_db(self):
        self.logger.print_log('Script started...')
        link_to_category = '{}categories?name={}'.format(self.base_url, self.category)
        try:
            response = requests.get(link_to_category).json()
            category_id = None
            category_name = None
            if response:
                self.logger.print_log('Checking if db is not empty...')
                print(response)
                category_id = response[0].get('id')
                category_name = response[0].get('name').title()
            if category_name == self.category:
                self.logger.print_log("{} category is already in db.".format(category_name))
                amount_of_hashtags = self.check_amount_current_hashtags()
                self.logger.print_log("It has {} hashtags.".format(amount_of_hashtags))
                if amount_of_hashtags < 10:  # not sure about this
                    if self.add_new_hashtags_to_db(category_id):
                        self.logger.print_log('Success')
                    else:
                        self.logger.print_log("Something went wrong with adding hashtags to db")
            else:
                self.logger.print_log('This category is not in db. Adding and finding hashtags.')
                if self.__add_category():
                    response = requests.get(link_to_category).json()
                    self.logger.print_log(' Response: {}'.format(response))
                    category_id = response[0].get('id')
                    if self.add_new_hashtags_to_db(category_id):
                        self.logger.print_log('Success')
                    else:
                        self.logger.print_log("Something went wrong with adding hashtags to db")

        except Exception as e:
            self.logger.print_log(' ERROR - {}'.format(e))


if __name__ == '__main__':
    new_category = "Beauty"
    basic_hashtags = ['fashion', 'beauty']
    script = HashtagScript(new_category, basic_hashtags)
    script()
