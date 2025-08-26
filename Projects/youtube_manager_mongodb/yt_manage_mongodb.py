from pymongo import MongoClient
from bson import ObjectId
client=MongoClient("mongodb+srv://balajpy:balajpy@cluster0.jlo3y.mongodb.net/",tlsAllowInvalidCertificates=True)
db=client["balajpy"]
video_Collection = db["videos"]
from bson import ObjectId

# print(video_Collection)

def list_videos():
   for video in video_Collection.find():
      print(f"ID:{video['_id']} , Name:{video['name']},time:{video['time']}")

def add_video(name,time):
   video_Collection.insert_one({"name":name, "time":time})

def update_video(video_id,new_name,new_time):
    _id = ObjectId(video_id)
    video_Collection.update_one(
       {'_id':_id},
       {"$set":{"name":new_name,"time":new_time}}
    )

def delete_video(video_id):
   _id = ObjectId(video_id)
   video_Collection.delete_one({"_id": video_id})
def  main ():
     
     while True:
        print("/n Youtube manager app with db")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Videos")
        print("5. exit app")
        choice = input("Enter your choice: ") 

        if choice == '1' :
            list_videos()

        elif choice == '2' :
           name = input("enter the video name: ")    
           time =  input("enter the video time: ")    
           add_video(name ,time)

        elif choice == '3' :
           video_id = input("Enter video ID to update: ")
           name = input("enter the updated video name")    
           time =  input("enter the updated video time:")    
           update_video(video_id ,name ,time)

        elif choice == '4' :
           video_id = input("Enter video ID to delete: ")
           delete_video(video_id)
           
        elif choice == '5' :
            break
        else:
            print ("Invalid choice")


if __name__ == "__main__":
  main()