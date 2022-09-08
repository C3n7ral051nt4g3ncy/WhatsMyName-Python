#!/usr/bin/env python3
# File name       : whatsmyname.py
# By              : C3n7ral051nt4g3ncy | aka OSINT Tactical https://github.com/C3n7ral051nt4g3ncy
# Usage           : 1.Scan for Target Username | 2.Current supported sites list | 3.Total number of sites | 4. Single Search
# Version         : Version 0.1
# Support         : Please do not support me, Support this project --> https://github.com/WebBreacher/WhatsMyName

# Py Libs
import sys
import time
import argparse
import json
import requests
from tqdm import tqdm


# script banner
def banner():
    print(
        """\033[39m\033[1m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⢀⠀⠀⣰⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⣾⣿⡄⠹⢿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣤⣼⣿⣿⣿⣿⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀   ⢀⣴⡶⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣟⢿⠇⢀ ⣶⡆⢰⣶⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀  ⢀⣴⡿⠋⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣇⢻⣿⣮⣀ ⣘⠻⠀  ⠙⢿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀ ⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠈⠉⣽⣿⣿⣿⣌⠛⠻⠿⠿⠿⠇⠀⠀⠀⠀⠀⠀ ⠙⢿⣷⣄⠀⠀⠀
⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⢿⣿⣿⡖⣰⣶⠂⠀⠀⠀⠀⠀⠀⠀⠀ ⠀ ⠙⢿⣷⣄⠀
⠀⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡀⠈⠙⢠⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀ ⢀⣴⣿⠟⠀
⠀⠀ ⠈⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⢀⣿⡟⣰⡄⠀⠀⠀⠀⠀⠀⠀ ⢀⣴⣿⠟⠁⠀⠀
⠀⠀⠀⠀  ⠈⠻⣿⣦⡀⠀⠀⠀⠀⠀⢀⣿⣿⠇⠀⣾⡿⢠⣿⡇⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀   ⠈⠻⣿⣦⠀⠀⠀⢸⣿⣿⠀⣼⣿⠁⠈⠉⠀⠀⠀⠀⢰⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠙⠉⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀
             < WebBreacher >"""
    )
    print(
        """ \033[32m\033[1m
       ╦ ╦┬ ┬┌─┐┌┬┐┌─┐╔╦╗┬ ┬╔╗╔┌─┐┌┬┐┌─┐
       ║║║├─┤├─┤ │ └─┐║║║└┬┘║║║├─┤│││├┤ 
       ╚╩╝┴ ┴┴ ┴ ┴ └─┘╩ ╩ ┴ ╝╚╝┴ ┴┴ ┴└─┘ Version 0.1"""
    )
    print(
        """\033[39m\033[1m
       by C3n7ral051nt4g3ncy
       github.com/WebBreacher/WhatsMyName\n\n
      \033[32m\033[1m\033[40mUsage: python3 whatsmyname.py -h\033[0m\n\n"""
    )

    time.sleep(1)


# Get data from inside the 'wmn_data.json' file
def read_json():
    with open("wmn-data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data


# main
if __name__ == "__main__":
    banner()
    data = read_json()

    # Argparse arguments
    parser = argparse.ArgumentParser(
        description="Scan all sites on Project WhatsMyName for a target username "
        "and wait for\033[32m\033[1m positive\033[0m identification."
    )

    parser.add_argument(
        "-u", "--username", help="\033[32m\033[1m\nTarget Username \033[0m"
    )

    parser.add_argument(
        "-s",
        "--singlesearch",
        nargs="*",
        help="\033[32m\033[1m\nSingle site search\033[0m",
    )

    parser.add_argument(
        "-f",
        "--fulllist",
        action="store_true",
        help="\033[32m\033[1m\nView full sites list on Project WMN | Find site name for a single search\033[0m\n\n",
    )

    parser.add_argument(
        "-c",
        "--countsites",
        action="store_true",
        help="\033[32m\033[1m\nNumber of sites currently supported on Project WhatsMyName\033[0m\n",
    )

    # args settings
    args = parser.parse_args()

    username = args.username

    singlesearch = args.singlesearch

    countsites = args.countsites

    fulllist = args.fulllist

    # Get full list of sites currently supported on Project WhatsMyName
    if fulllist:

        for i in tqdm(range(10)):
            time.sleep(0.06)

        for site in data["sites"]:
            site_name = site["name"]
            print(
                f"""
    ╔════════════════╦══════════════════════════════════╗
    ║ WEBSITE NAME:  ║ ✅   \033[1m{site_name}                       
    ╚════════════════╩══════════════════════════════════╝"""
            )

    # Get exact number of sites supported on Project WhatsMyName
    if countsites:
        for i in tqdm(range(10)):
            time.sleep(0.1)

        search_word = "uri_check"
        with open("wmn-data.json", "r") as f:
            data = f.read()
            total = data.count(search_word)
            print(
                "\033[32m\033[1mTotal Number\033[0m\033[32m of sites currently supported on \033[1mProject WhatsMyName  \033[40m -->",
                total,
            )

    # Scan all websites for target username confirmation
    if username:

        headers = {
            "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-language": "en-US;q=0.9,en,q=0,8",
            "accept-encoding": "gzip, deflate",
            "user-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        }

        response = requests.get(
            "https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json"
        )
        sites = response.json()["sites"]
        if singlesearch:
            if singlesearch[0].lower() in [s["name"].lower() for s in sites]:
                for site in sites:
                    uri_check = site["uri_check"]
                    site_name = site["name"]

                    if site_name.lower() == singlesearch[0].lower():
                        uri_check = uri_check.format(account=username)

                        try:
                            res = requests.get(uri_check, headers=headers)

                            estring_pos = res.text.find(site["e_string"]) > 0

                            estring_neg = res.text.find(site["m_string"]) > 0

                        except Exception as e:
                            print(
                                f"\033[91mNot able to verify the website [{singlesearch}]! please use the correct name"
                            )
                            break

                        if res.status_code == 200 and estring_pos:
                            print("\033[32m-" * 133)
                            print(
                                f"\033[32m[+] \033[1mTarget found\033[0m\033[32m ✓ on:\033[1m    \033[40m{site_name}\033[0m"
                            )
                            print(
                                f"\033[32m[+] Profile URL:\033[1m          {uri_check}\033[0m"
                            )
                            print("\033[32m\033[1m-" * 133)

                        if estring_neg:
                            print("\033[32m\033[1m-" * 133)
                            print(
                                f"\033[91m[-]Target not found on:  \033[1m", site_name
                            )
                        break

            else:
                print(
                    "\033[91mThe site you specified can't be verified ;(  , its either not supported or you spelt it wrong!"
                )
        else:
            for site in sites:
                uri_check = site["uri_check"]
                site_name = site["name"]
                uri_check = uri_check.format(account=username)

                try:
                    res = requests.get(uri_check, headers=headers)

                    estring_pos = res.text.find(site["e_string"]) > 0

                    estring_neg = res.text.find(site["m_string"]) > 0

                except Exception as e:
                    continue

                if res.status_code == 200 and estring_pos:
                    print("\033[32m-" * 133)
                    print(
                        f"\033[32m[+] \033[1mTarget found\033[0m\033[32m ✓ on:\033[1m    \033[40m{site_name}\033[0m"
                    )
                    print(
                        f"\033[32m[+] Profile URL:\033[1m          {uri_check}\033[0m"
                    )
                    print("\033[32m\033[1m-" * 133)

                if estring_neg:
                    print("\033[32m\033[1m-\033[0m" * 133)
                    print(f"\033[31m[-]Target not found on:  \033[1m", site_name)
