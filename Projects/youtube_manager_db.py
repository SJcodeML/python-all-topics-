import sqlite3

conn = sqlite3.connect('yotube_videos.db')

cursor = conn.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS videos (
              id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              time TEXT NOT NULL 

               )
""")

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print (row)


def add_video(name , time):
    cursor.execute("INSERT INTO videos(name , time) VALUES (? , ?)" , (name , time))
    conn.commit()


def update_video(video_id , new_name , new_time):
    cursor.execute("UPDATE videos SET name = ? , time = ? WHERE id = ?" , (new_name , new_time , video_id))
    conn.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()

def main():
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
           name = input("enter the video name:")    
           time =  input("enter the video time:")    
           update_video(video_id ,name ,time)

        elif choice == '4' :
           video_id = input("Enter video ID to delete: ")
           delete_video(video_id)
           
        elif choice == '5' :
            break
        else:
            print ("Invalid choice")

    conn.close()
           

if __name__ == "__main__":
 main() 