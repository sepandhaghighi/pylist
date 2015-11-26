import os

start_tag="#EXTM3U"
song_tag="#EXTINF:"
music_format=[".ogg",".mp3",".wav"]

    
def get_name():
    name=input("Please Enter Your Playlist Name : ")
    return name
def line_printer(num):
    line_text=""
    for i in range(num):
        line_text=line_text+"-"
    print(line_text)
    
def get_files(path):
    pwd=os.getcwd()
    pwd=pwd+"\\"+path
    file_lists=os.listdir(pwd)
    return file_lists

def create_playlist(name,file_list):
    playlist_name=name+".m3u"
    file_counter=0
    if len(file_list)==0:
        print("Your music folder is empty")
        return None
    file=open(playlist_name,"a")
    file.write(start_tag+"\n")
    for i in range(len(file_list)):
        for j in range(len(music_format)):
            if file_list[i].find(music_format[j])!=-1:
                file_counter=file_counter+1
                file.write(song_tag+str(i)+","+str(i)+"-"+str(i)+"\n"+file_list[i]+"\n")
                print(file_counter,"- ",file_list[i])
    line_printer(40)
    print(str(file_counter)+" Files added to playlist")
    file.close()

if __name__=="__main__":
    playlist_name=get_name()
    file_list=get_files("Music")
    create_playlist(playlist_name,file_list)
    
    
