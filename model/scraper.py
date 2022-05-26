from pprint import pprint
import instagram_scraper

args = {"login_user": "login", "login_pass": "pass", "maximum":"10"}

def main(uname):
    insta_scraper = instagram_scraper.InstagramScraper(**args)
    insta_scraper.authenticate_as_guest()
    shared_data = insta_scraper.get_shared_data_userinfo(username=uname)

    arr = []

    for item in insta_scraper.query_media_gen(shared_data):
        arr.append(item)

    pprint(arr)
