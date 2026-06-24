import pygame
from Gamestates.GamestateIs import GamestateIs


music_on = True
jukebox_mode = False 
current_song_title = " "
current_song_position = 0


SOUNDTRACK = [

"./audio/sound_bites.wav",
"./audio/blips.wav",
"./audio/castle_glass.wav",
"./audio/forest_sprite_stormy_night.wav",
"./audio/machinery.wav",
"./audio/new_beginnings.wav",
"./audio/night_sky.wav",
"./audio/old_friends.wav",
"./audio/sand_castle.wav",
"./audio/snowfall.wav",
"./audio/spcb0.wav",
"./audio/spcb1.wav",
"./audio/spcb2.wav",
"./audio/spcb3.wav",
"./audio/spcb4.wav",
"./audio/strange_signal.wav",
"./audio/streetlights.wav",
"./audio/sunrise.wav",
"./audio/sunset.wav",

]

soundtrack_length = len(SOUNDTRACK)

@staticmethod
def play_soundtrack():
    loadAndPlayForever(SOUNDTRACK[0], 0)
    pass 

@staticmethod
def play_observing():
    loadAndPlayForever(SOUNDTRACK[3], 3)
    pass 

@staticmethod
def playGamestateBase(gamestate: GamestateIs):
    match gamestate:
        case GamestateIs.MAIN_MENU:
            loadAndPlayForever(SOUNDTRACK[0], 0)
            pass

        case GamestateIs.OBSERVING:
            loadAndPlayForever(SOUNDTRACK[1], 1)
            pass 

@staticmethod 
def loadAndPlayForever(track_as_string, track_position):
    pygame.mixer.music.unload()
    pygame.mixer.music.load(track_as_string)
    pygame.mixer.music.play(-1)
    global current_song_title
    current_song_title = track_as_string 
    global current_song_position 
    current_song_position = track_position     


@staticmethod 
def getPreviousTrack() -> str:
    if current_song_position -1 >= 0:
        return SOUNDTRACK[current_song_position-1]
    else: 
        return SOUNDTRACK[0]

@staticmethod
def getPreviousTrackPos() -> int:
    if current_song_position -1 >= 0:
        return current_song_position -1
    else: 
        return 0

@staticmethod
def getCurrentTrack() -> str:
    return SOUNDTRACK[current_song_position]


@staticmethod
def getNextTrack() -> str:
    if current_song_position + 1 > len(SOUNDTRACK):
        return SOUNDTRACK[len(SOUNDTRACK)]
    else:
        return SOUNDTRACK[current_song_position+1]

@staticmethod
def getNextTrackPos() -> int:
    if current_song_position + 1 > len(SOUNDTRACK):
        return len(SOUNDTRACK)
    else:
        return current_song_position + 1


