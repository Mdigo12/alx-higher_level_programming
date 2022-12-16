#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        response = response.read()
        print("Body response:")
        print("    - type: {}".format(type(response)))
        print("    - content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode(encoding='utf-8')))
