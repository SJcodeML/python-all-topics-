# import requests

# # API details
# app_id = "1976702"
# key = "afef0768dc2c5a5967b7"
# secret = "893d844b63cc4d4bfad3"
# cluster = "ap2"
# url= "https://chatify.najam.pk/api/v1/sendmessage"
# params = {
#     "number" : "03402745283",
#     "message":" Message from sir Najam",
#     "apikey" : key
# }


# try :
#     # send the request
#     response = requests.get(url , params=params)

#     # check if the request was successful
#     if response.status_code == 200:
#         print("Message sent successfully!")
#     else:
#         print(f"Failed to send message . status code {response.status_code}")

# except requests.exceptions.RequestException as e:
#     print ("An eroor occured while sending the message ")
#     print ("error details : {e}")



# ERROR HANDLING:
try:
    num = int(input("enter your number"))
    result = num/0
    print (f"Result is :{result}")

except ZeroDivisionError:
    print ("cannot divide by zero")

except ValueError:

    print("numbers cant be divide by numerals`")        


# USING EXCEPTIONS:

try:
    num = int(input("enter your number"))
    result = num/0
    print (f"Result is :{result}")

except ZeroDivisionError:
    print ("cannot divide by zero")

except ValueError:

    print("numbers cant be divide by numerals`")        
except Exception as e :
    print(e)