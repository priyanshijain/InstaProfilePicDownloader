#!/usr/bin/env python3

import argparse
import re
import sys
import requests


def fetchProfilePic(username):
    url = "https://www.instagram.com/{}/?__a=1".format(username)

    r = requests.get(url)

    if r.ok:
        data = r.json()
        print("Biography of the " +data['graphql']['user']['full_name'] +" is "+data['graphql']['user']['biography'])
        return data['graphql']['user']['profile_pic_url_hd']

    else:
        print("\033[91m✘ Cannot find user ID \033[0m")
        sys.exit()


def main():
    username=input("Enter the username of your insta handle")
    file_url = fetchProfilePic(username)
    fname = username + ".jpg"
    print("Profile Picture is getting downloaded Please Wait")
    r = requests.get(file_url, stream=True)
    if r.ok:
        with open(fname, 'wb') as f:
            f.write(r.content)
            print("\033[92m✔ Downloaded:\033[0m {}".format(fname))
    else:
        print("Cannot make connection to download image")


if __name__ == "__main__":
    main()
