from pprint import pprint
import instagram_scraper

args = {"login_user": "chesislub", "login_pass": "abcd4321", "maximum":"25", "media-types":"image"}

def main(uname):
    insta_scraper = instagram_scraper.InstagramScraper(**args)
    insta_scraper.authenticate_with_login()
    shared_data = insta_scraper.get_shared_data_userinfo(username=uname)

    arr = []

    for item in insta_scraper.query_media_gen(shared_data):
        arr.append(item)

    pprint(arr)

#main("aliaabhatt")
