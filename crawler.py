import requests
import tarfile
import json
import re

def main():
    with open('binaries.json', 'r') as json_file:
        binaries = json.load(json_file)
    
    for name in binaries['binaries']:
        repo = name['name']
        assets = name['assets']
        download_binary(repo, assets)

def download_binary(repo, assets):
    all_assets = []
    # Fetch all assets of latest release version
    # curl -sL https://api.github.com/repos/nicocha30/ligolo-ng/releases/latest | jq -r ".assets[].browser_download_url"
    response = requests.get(f'https://api.github.com/repos/{repo}/releases/latest')
    data = response.json()
    # Extract the browser download URLs from the assets

    for asset in data['assets']:
        all_assets.append(asset['browser_download_url'])

    # Function to check if an element of list1 contains any regex from list2
    for i in all_assets:
        for regex in assets:
            if re.search(regex, i):
                print('True')
        print('False')


    print(all_assets)
    
#   # Build the URL for the latest release
#   url = f'https://github.com/derailed/k9s/releases/download/{latest_version}/ligolo-ng_proxy_0.4.3_Linux_64bit.tar.gz'
#   
#   # Download the file
#   response = requests.get(url, stream=True)
#   
#   # Save the file
#   filename = 'k9s_Linux_amd64.tar.gz'
#   with open(filename, 'wb') as f:
#       for chunk in response.iter_content(chunk_size=1024):
#           if chunk:
#               f.write(chunk)
#   
#   print(f'Downloaded: {filename}')

if __name__ == '__main__':
    main()
