import os
from random import randint # import random
start_tag="#EXTM3U" # Start Tag Of m3u files 
song_tag="#EXTINF:" # start tag of each file information
music_format=[".ogg",".mp3",".wav"] # lists of music file formats
pwd=os.getcwd() # Save Current Directory Path
    
def get_name(): # funtion for get playlist name from user
    name=input("Please Enter Your Playlist Name : ") # Get input for playlist name
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
def create_playlist(name,file_list,save_path,random=False,modify_flag=False): # create playlist
    selected_file=[]
    file_counter=0
    if len(file_list)==0:
        print("Your music folder is empty")
        return None
    if modify_flag==True:
        file=open(save_path+"\\"+name)
        file_lines=file.readlines()
        file.close()
        print_counter=0
        for i in range(len(file_lines)):
            if file_lines[i].find(".mp3")!=-1:
                print(print_counter,"-",file_lines[i][:-1])
                print_counter=print_counter+1
    file=open(save_path+"\\"+name,"a")
    file.write(start_tag+"\n")
    if random==False:
        for i in range(len(file_list)):
            for j in range(len(music_format)):
                if file_list[i].find(music_format[j])!=-1:
                    
                    if modify_flag==True and file_list[i]+"\n" not in file_lines:
                        file_counter=file_counter+1
                        file.write(song_tag+str(i)+","+str(i)+"-"+str(i)+"\n"+file_list[i]+"\n")
                        print(file_counter,"- ",file_list[i],"+NEW")
                    elif modify_flag==False:
                        file_counter=file_counter+1
                        file.write(song_tag+str(i)+","+str(i)+"-"+str(i)+"\n"+file_list[i]+"\n")
                        print(file_counter,"- ",file_list[i],"+NEW")
                        
    elif random==True:
        while(file_counter<len(file_list)):
            coin=randint(0,len(file_list)-1)
            if coin not in selected_file:
                selected_file.append(coin)
                file_counter=file_counter+1
                file.write(song_tag+str(coin)+","+str(coin)+"-"+str(coin)+"\n"+file_list[coin]+"\n")
                print(file_counter,"- ",file_list[coin])
        
    line_printer(40) # print a divider line
    print(str(file_counter)+" Files added to playlist")
    print(save_path+"\\"+name)
    file.close()
def modify_get(path):
    m3u_list=[]
    all_list=os.listdir(path)
    for i in range(len(all_list)):
        if all_list[i].find(".m3u")!=-1:
            m3u_list.append(all_list[i])
    if len(m3u_list)==0:
        print("There is no m3u file in this location for modify")
    return m3u_list
def modify(file_list):
    for i in range(len(file_list)):
        print(i,"-",file_list[i])
    file_choose=-1
    while(file_choose<0 or file_choose>len(file_list)-1):
        file_choose=int(input("Please choose one file to modify"))
    return file_list[file_choose]
    
   
if __name__=="__main__":
    try:
        flag=False
        save_path=saving_path()
        path_file_lists=os.listdir()
        modify_create=int(input(" Create new playlist[1] Add to a playlist[2] :"))
        if modify_create==2:
            m3u_list=modify_get(save_path)
            if len(m3u_list)==0:
                modify_create=1
                print("Create new playlist")
            else:
                playlist_name=modify(m3u_list)
                flag=True
        if modify_create!=2:
            playlist_name=get_name()
            flag=False
            while(playlist_name in path_file_lists):
                print("This File Exsit")
                playlist_name=get_name()
            
        file_list=get_files("Music")
        random_select=int(input("Random Adding[1] Nomral Adding[2]  "))
        if random_select==1:
            random_select=True
        else :
            random_select=False
        create_playlist(playlist_name,file_list,save_path,random_select,flag)
    except ValueError:
        print("Error on incorrect input key , please enter correct key")
    
    
