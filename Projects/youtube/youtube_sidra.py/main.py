
from pymongo import MongoClient
from bson import ObjectId

# Connection (keep TLS certs setting if needed)
client = MongoClient(
    "mongodb+srv://balajpy:balajpy@cluster0.jlo3y.mongodb.net/",
    tlsAllowInvalidCertificates=True
)
db = client["balajpy"]
video_collection = db["videos"]

# def list_videos():
#     # Fetch all videos and print
#     for video in video_Collection.find():
#         vid_id = video.get('_id')
#         name = video.get('name')
#         time = video.get('time')
#         print(f"ID:{vid_id} , Name:{name}, time:{time}")

# def add_video(name, time):
#     video_Collection.insert_one({"name": name, "time": time})

# def update_video(video_id, new_name, new_time):
#     # try:
#     _id = ObjectId(video_id)
#     # except Exception as e:
#     #     print(f"Invalid ID format: {video_id} - {e}")
#     #     return

#     video_Collection.update_one(
#         {'_id': _id},
#         {"$set": {"name": new_name, "time": new_time}}
#     )

# def delete_video(video_id):
#     # try:
#     _id = ObjectId(video_id)
#     # except Exception as e:
#     #     print(f"Invalid ID format: {video_id} - {e}")
#     #     return

#     video_Collection.delete_one({"_id": _id})

# def main():
#     while True:
#         print("\nYoutube manager app with db")
#         print("1. List Videos")
#         print("2. Add Video")
#         print("3. Update Video")
#         print("4. Delete Video")
#         print("5. Exit app")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             list_videos()

#         elif choice == '2':
#             name = input("Enter the video name: ").strip()
#             time = input("Enter the video time: ").strip()
#             if name and time:
#                 add_video(name, time)
#             else:
#                 print("Name and time are required.")

#         elif choice == '3':
#             video_id = input("Enter video ID to update: ").strip()
#             name = input("Enter the updated video name: ").strip()
#             time = input("Enter the updated video time: ").strip()
#             if video_id and name and time:
#                 update_video(video_id, name, time)
#             else:
#                 print("Video ID, name, and time are required.")

#         elif choice == '4':
#             video_id = input("Enter video ID to delete: ").strip()
#             if video_id:
#                 delete_video(video_id)
#             else:
#                 print("Video ID is required.")

#         elif choice == '5':
#             break
#         else:
#             print("Invalid choice")

# if __name__ == "__main__":
#     main()




# from pymongo import MongoClient
# from bson import ObjectId



# client = MongoClient("mongodb+srv://balajpy:balajpy@cluster0.jlo3y.mongodb.net/",
#      tlsAllowInvalidCertificates=True  )


# db = client("balajpy")
# video_collection = db["videos"]


def list_videos():
    for video in video_collection.find():
        print(f"Id : {video['_id']} , Name : {video['name']} , Time : {video['time']})")
        
def Add_videos(add_name , add_time):
   
    video_collection.insert_one({'name' :add_name , 'time' : add_time} )
def Update_videos(Videos_id, new_name, new_time):
    _id = ObjectId(Videos_id)
    video_collection.update_one({'_id':_id},{'$set' : {'name':new_name , 'time' : new_time}})

# def update_video(video_id,new_name,new_time):
#     _id = ObjectId(video_id)
#     video_collection.update_one(
#        {'_id':_id},
#        {"$set":{"name":new_name,"time":new_time}}
#     )



def Delete_videos(videos_id):
    _id = ObjectId(videos_id)
    video_collection.delete_one({'_id':_id})


def main ():

    while True :
       print("\nWELCOME TO YOUTUBE MANAGER APP \n")
       print("1.List videos")
       print("2.Add videos")
       print("3.Update Videos")
       print("4.Delete Videos")
       print("5.Exit\n")

       choice = input("Enter your query: ")

       if choice == '1':
           list_videos()
       elif choice == '2':
           name = input("Enter your video name: ")
           time = input ("Enter your time: ")
           Add_videos(name , time)
       elif choice == '3':
           id = input("Enter your ID to update: ")
           name = input("Enter your video name: ")
           time = input ("Enter your time: ")
           Update_videos(id , name , time)
       elif choice == '4':
         id=input("Enter your ID to update: ")
         Delete_videos(id)
       elif choice == '5':
           break
       else:
           print("Invalid query")




if __name__  == '__main__':
    main()   