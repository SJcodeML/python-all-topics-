import requests 

def main():
    response = requests.get('https://api.example.com/data')
    data = response.json()
    print(data)

if __name__ == "__main__":
    main()
