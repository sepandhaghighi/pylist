import os
from random import randint # import random
start_tag="#EXTM3U" # Start Tag Of m3u files 
song_tag="#EXTINF:" # start tag of each file information
music_format=[".ogg",".mp3",".wav"] # lists of music file formats
pwd=os.getcwd() # Save Current Directory Path
    
def get_name(): # funtion for get playlist name from user
    name=input("Please Enter Your Playlist Name : ") # Get input for playlist name
    return name+".m3u" # Add .m3u to the end of each file

def line_printer(num): # function for printing line
    line_text="" # initial string
    for i in range(num): # add "-" in a loop at the end of line
        line_text=line_text+"-"
    print(line_text) # print line
    
def saving_path():
    
    print("Please choose one for playlist location") # print information
    print("[1]-Root Directory") # pint information
    print("[2]-Enter Another Location") # print information
    input_index=input()   # get input from user
    if int(input_index)==2: # if user choose another location
        location=input("Please Enter Saving Location : ") # get location from user as a string
        location.replace("\\","\\") # replace "/" with "//"
    else:
        location=pwd # if user choose root location , copy current directory to location variable
    return location # return location variable

def get_files(path): # function for creating list of a directory files
    location=pwd+"\\"+path # declare location variable with input folder name
    file_lists=os.listdir() # extract files and folder in this location
    return file_lists # return files as lists
def create_playlist(name,file_list,save_path,random=False,modify_flag=False): # create playlist
    selected_file=[] # init a empty list as selected_file lists
    file_counter=0 # init a counter
    if len(file_list)==0: # if length this list is zero
        print("Your music folder is empty") # print folder in empty and return none
        return None
    if modify_flag==True: # if the application is on modify mode
        file=open(save_path+"\\"+name) # open selected m3u file as reader
        file_lines=file.readlines() # extract lines in this file
        file.close() # close file
        print_counter=0 # counter for printig lines
        for i in range(len(file_lines)): # extract music tracks line in lines
            if file_lines[i].find(".mp3")!=-1:
                print(print_counter,"-",file_lines[i][:-1]) # print it
                print_counter=print_counter+1 # update print counter
    file=open(save_path+"\\"+name,"a") # open m3u file as appender
    if modify_flag==False:
        file.write(start_tag+"\n") # write start_tag if its on non_modify mode
    if random==False: #check random flag if its False
        for i in range(len(file_list)): # for loop on file_list list
            for j in range(len(music_format)): # extract defined musics
                if file_list[i].find(music_format[j])!=-1:
                    
                    if modify_flag==True and file_list[i]+"\n" not in file_lines: # if application is on modify mode and this music its not on the playlist add it as new song
                        file_counter=file_counter+1 # update file_counter
                        file.write(song_tag+str(i)+","+str(i)+"-"+str(i)+"\n"+file_list[i]+"\n")
                        print(file_counter,"- ",file_list[i],"+NEW")
                    elif modify_flag==False: # if the modify mode is off and add files for first time 
                        file_counter=file_counter+1 # update file_counter
                        file.write(song_tag+str(i)+","+str(i)+"-"+str(i)+"\n"+file_list[i]+"\n")
                        print(file_counter,"- ",file_list[i],"+NEW")
                        
    elif random==True: # if random mode is On
        while(file_counter<len(file_list)): # loop until select each music files
            coin=randint(0,len(file_list)-1) # generate new random integer in [0,length(file_list)]
            if coin not in selected_file: # if this random number didnt select previusoly
                selected_file.append(coin) # added it to a selected_file list
                file_counter=file_counter+1 # increase file_counter
                file.write(song_tag+str(coin)+","+str(coin)+"-"+str(coin)+"\n"+file_list[coin]+"\n") # write text on m3u file
                print(file_counter,"- ",file_list[coin]) # print information
        
    line_printer(40) # print a divider line
    print(str(file_counter)+" Files added to playlist") # print information about number of added files to playlist file
    print(save_path+"\\"+name) # show saving location
    file.close() # close file
def modify_get(path):  
    m3u_list=[] # init new empty list for m3u files
    all_list=os.listdir(path) # extract all of the files and folders in this location 
    for i in range(len(all_list)): # filter playlists with .m3u
        if all_list[i].find(".m3u")!=-1:
            m3u_list.append(all_list[i]) # add this files name to the m3u_list
    if len(m3u_list)==0: # if there is no playlist in this location
        print("There is no m3u file in this location for modify") # print information about no file existence
    return m3u_list # return  m3u_list
def modify(file_list):
    for i in range(len(file_list)): # print each files names in file_list
        print(i,"-",file_list[i])
    file_choose=-1 # initial state of this variable force porgram to get to the while atleast once
    while(file_choose<0 or file_choose>len(file_list)-1): # get number from user until user enter correct index
        file_choose=int(input("Please choose one file to modify"))
    return file_list[file_choose] # return m3u file name
    
   
if __name__=="__main__":
    try:
        flag=False # inital state of modify_flag in False
        save_path=saving_path() # call saving_path and get save path from user by this func
        path_file_lists=os.listdir() # extract file and list in current folder
        modify_create=int(input(" Create new playlist[1] Add to a playlist[2] :")) # get input from user to choose between creating new playlist or adding music to the end of another
        if modify_create==2: # if user choose add to a playlist option
            m3u_list=modify_get(save_path) # return m3u_list by calling modify_get func
            if len(m3u_list)==0: # if there is no m3u file in this folder
                modify_create=1 # switch to creating new playlist
                print("Create new playlist") # print information
            else:
                playlist_name=modify(m3u_list) # get playlist name from user by this func
                flag=True # update modify flag
        if modify_create!=2: # on new mode
            playlist_name=get_name() # get playlist name but calling this function
            flag=False # update flag
            while(playlist_name in path_file_lists): # get name from user until user enter new unique name
                print("This File Exsit")
                playlist_name=get_name()
            
        file_list=get_files("Music") # extract music files in Music folder
        random_select=int(input("Random Adding[1] Nomral Adding[2]  ")) # get input from user about random or normal selection of music tracks
        if random_select==1: # if random mode selected
            random_select=True # update random flag to True
        else :
            random_select=False # else update random flag to False
        create_playlist(playlist_name,file_list,save_path,random_select,flag) #call main function create_playlist and create of update playlist
    except ValueError: # on ValueError , when user enter another key instead of number 
        print("Error on incorrect input key , please enter correct key") # print infromation about error
    
    
