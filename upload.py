#!/usr/bin/env python

import sys
import os

from ytmusicapi import YTMusic

def main():
    path = sys.argv[1]
    if not os.path.exists(path):
        print("Invalid file path. %s" % path)
        return

    api = YTMusic('headers_auth.json')

    #if not api.is_authenticated():
    #    print("Login Error\n")
    #    return

    print("start upload...\n")
    upload_info = api.upload_song(path)
    print(upload_info)
    print("upload is completed.\n")

    # api.logout()


if __name__ == '__main__':
    main()
