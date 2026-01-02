import requests 

def main():
    response = requests.get('https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1')
    data = response.json()
    print(data['data']['data'][0]['content'])

if __name__ == "__main__":
    main()




