import pytube
from gtts import gTTS
from playsound import playsound


def play_sound(voice):
    sound = 'sound.mp3'
    speak = gTTS(text=str(voice), lang='ru', slow=False)
    speak.save(sound)
    playsound(sound)


try:
    print("Input URL from youtube:")
    url = input()
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download('/home/seroga/Видео')
    print('download is complete')
    play_sound('загрузка выполнена успешно')

except KeyboardInterrupt:
    print('Program stop')
    play_sound('загрузка отменена')
