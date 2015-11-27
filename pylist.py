import os
from random import randint
start_tag="#EXTM3U" # Start Tag Of m3u files 
song_tag="#EXTINF:" # start tag of each file information
music_format=[".ogg",".mp3",".wav"] # lists of music file formats
pwd=os.getcwd() # Save Current Directory Path
    
def get_name(): # funtion for get playlist name from user
    name=input("Please Enter Your Playlist Name : ")
    return name+".m3u"
def line_printer(num): # function for printing line
    line_text=""
    for i in range(num):
        line_text=line_text+"-"
    print(line_text)
def saving_path():
    print("Please choose one for playlist location")
    print("[1]-Root Directory")
    print("[2]-Enter Another Location")
    input_index=input()  
    if int(input_index)==2:
        location=input("Please Enter Saving Location : ")
        location.replace("\\","\\")
    else:
        location=pwd
    return location
def get_files(path): # function for creating list of a directory files
    location=pwd+"\\"+path
    file_lists=os.listdir(location)
    return file_lists
def create_playlist(name,file_list,save_path,random=False): # create playlist
    selected_file=[]
    file_counter=0
    if len(file_list)==0:
        print("Your music folder is empty")
        return None
    file=open(save_path+"\\"+name,"a")
    file.write(start_tag+"\n")
    if random==False:
        for i in range(len(file_list)):
            for j in range(len(music_format)):
                if file_list[i].find(music_format[j])!=-1:
                    file_counter=file_counter+1
                    file.write(song_tag+str(i)+","+str(i)+"-"+str(i)+"\n"+file_list[i]+"\n")
                    print(file_counter,"- ",file_list[i])
    elif random==True:
        while(file_counter<len(file_list)):
            coin=randint(0,len(file_list)-1)
            if coin not in selected_file:
                selected_file.append(coin)
                file_counter=file_counter+1
                file.write(song_tag+str(coin)+","+str(coin)+"-"+str(coin)+"\n"+file_list[coin]+"\n")
                print(file_counter,"- ",file_list[coin])
        
    line_printer(40)
    print(str(file_counter)+" Files added to playlist")
    print(save_path+"\\"+name)
    file.close()

if __name__=="__main__":
    save_path=saving_path()
    path_file_lists=os.listdir()
    playlist_name=get_name()
    while(playlist_name in path_file_lists):
        print("This File Exsit")
        playlist_name=get_name()
    file_list=get_files("Music")
    random_select=int(input("Random Adding[1] Nomral Adding[2]  "))
    if random_select==1:
        random_select=True
    else :
        random_select=False
    create_playlist(playlist_name,file_list,save_path,random=random_select)
    
    
