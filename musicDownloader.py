from pytube import YouTube
import os

ROOT_PATH = os.getcwd()
MUSICS_LIST = f"{ROOT_PATH}/list.txt"

def simgerebis_raodenoba(file):

    f = open(file,'r')
    count = 0
    for links in f:
        count+=1
    f.close()
    return count



def musicDownloader(file):

    raodenoba = simgerebis_raodenoba(MUSICS_LIST)
    print(f'You requested to download {raodenoba} songs')


    gadmowerili = 0
    numeration = 1

    f = open(file,'r')
    for links in f:
        music = YouTube(links)
        music = music.streams.get_audio_only()
        try:

            print('Wait...')
            music.download()

        except:
            print(f'Music #{numeration} is not downloaded')
        print(f"Succesfully Downloaded Music #{numeration}")
        numeration+=1
        gadmowerili+=1


    print(f"Downloaded: {gadmowerili}/{raodenoba} ")

    pass

musicDownloader(MUSICS_LIST)




