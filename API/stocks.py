import requests

def stocks():
    url = "https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]["data"]
        product_name = user_data[1]["Name"]
        CurrentPrice =user_data[1]["CurrentPrice"]
        return product_name , CurrentPrice

    else : 
        raise Exception("API request failed or returned no data")    
   

def main():
    try :
        product_name , CurrentPrice = stocks()
        
        print(f"Product Name : {product_name}\nCurrent Price of the product is : {CurrentPrice}") 
    except Exception as e :
        print (str(e))


if __name__ == "__main__":
    main()