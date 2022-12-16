#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        response = response.read()
        print("Body response:")
        print("    - type: {}".format(type(response)))
        print("    - content: {}".format(response))
        print("    - utf8 content: {}".format(response.decode(encoding='utf-8')))
