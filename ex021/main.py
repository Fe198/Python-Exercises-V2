import vlc
import time
music = vlc.MediaPlayer("E:\Programação\Projetos\Python\Exercícios\Exercício021\sfx.mp3")
music.play()
time.sleep(60)
music.stop()