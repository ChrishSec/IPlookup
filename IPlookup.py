#!/usr/bin/python3

"""

__author__ = "ChrishSec"
__copyright__ = "Copyright (C) 2024 ChrishSec"
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.0"

Website: https://ChrishSec.com
GitHub: https://github.com/ChrishSec
Twitter: https://twitter.com/ChrishSec

"""

import re
import sys
import json
import requests
from bs4 import BeautifulSoup

def main():
    def sayhello():
        print("\n Usage: cat IP/Domain.txt | python3 IPlookup.py OR echo '<IP/Domain>' | python3 IPlookup.py\n")
        sys.exit(1)

    def api(ip_address, output_file):
        try:
            url = "https://iplookup.chrishsec.com/"
            headers = {
                "Host": "iplookup.chrishsec.com",
                "User-Agent": "IPlookup/v1.0.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://iplookup.chrishsec.com",
                "Referer": "https://iplookup.chrishsec.com/",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Dnt": "1",
                "Sec-Gpc": "1",
                "Te": "trailers",
            }

            data = {
                "ipAddress": ip_address
            }

            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            script_tags = soup.find_all('script')

            json_data = None
            for script_tag in script_tags:
                script_text = script_tag.get_text()
                if 'var jsonData =' in script_text:
                    json_data = re.search(r'var jsonData = (.+?);', script_text).group(1)
                    decoded_info = json.loads(json_data)

                    print("\n DEVELOPED BY >> ChrishSec.com")
                    print("\n" + "-" * 12)
                    print_info(decoded_info, 'ipaddress', '\n IP Address')
                    print_info(decoded_info, 'country', ' Country')
                    print_info(decoded_info, 'countrycode', ' Country Code')
                    print_info(decoded_info, 'city', ' City')
                    print_info(decoded_info, 'zip', ' Zip')
                    print_info(decoded_info, 'lat', ' Lat')   
                    print_info(decoded_info, 'lon', ' Lon')
                    print_info(decoded_info, 'timezone', ' Timezone')
                    print_info(decoded_info, 'isp', ' ISP')
                    print_info(decoded_info, 'org', ' Org')
                    print_info(decoded_info, 'asn', ' ASN')
                    print("\n" + "-" * 12)

                    with open(output_file, 'a') as file:
                        file.write("\n DEVELOPED BY >> ChrishSec.com")
                        file.write("\n\n" + "-" * 12 + "\n")
                        print_info_to_file(file, decoded_info, 'ipaddress', '\n IP Address')
                        print_info_to_file(file, decoded_info, 'country', ' Country')
                        print_info_to_file(file, decoded_info, 'countrycode', ' Country Code')
                        print_info_to_file(file, decoded_info, 'city', ' City')
                        print_info_to_file(file, decoded_info, 'zip', ' Zip')
                        print_info_to_file(file, decoded_info, 'lat', ' Lat')   
                        print_info_to_file(file, decoded_info, 'lon', ' Lon')
                        print_info_to_file(file, decoded_info, 'timezone', ' Timezone')
                        print_info_to_file(file, decoded_info, 'isp', ' ISP')
                        print_info_to_file(file, decoded_info, 'org', ' Org')
                        print_info_to_file(file, decoded_info, 'asn', ' ASN')
                        file.write("\n" + "-" * 12 + "\n")
                    
                    return
        except requests.exceptions.RequestException:
            return
        except json.JSONDecodeError:
            return
        except AttributeError:
            return
        except KeyboardInterrupt:
            print("\n Exiting.")
            sys.exit(0)
        except Exception as e:
            return

    def print_info(data, key, label):
        value = data.get(key, 'N/A') if key in data and data[key] else 'N/A'
        print(f"{label}: {value}")

    def print_info_to_file(file, data, key, label):
        value = data.get(key, 'N/A') if key in data and data[key] else 'N/A'
        file.write(f"{label}: {value}\n")

    output_file = "output.txt"

    if not sys.stdin.isatty():
        input_data = sys.stdin.read().strip()
        input_lines = input_data.split("\n")
        for ip_address in input_lines:
            api(ip_address.strip(), output_file)
    else:
        sayhello()

if __name__ == "__main__":
    main()

