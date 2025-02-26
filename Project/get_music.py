from keras.models import load_model
import random
import numpy as np
import os
from music21 import *
from theAI import *

instruments = ["Piano", "Violin", "Flute"]
tempi = ["Largo", "Adagio", "Andante", "Moderato", "Allegro", "Presto", "Slow", "Moderate", "Fast"]
pianoArtists = ["Bach", "Chopin", "Debussy", "Ellington", "Corea", "Anime"]
violinArtists = ["Mozart", "Paganini", "Vivaldi"]
fluteArtists = ["Brahms", "Wagner"]

def getInst():
    print("Available instruments:")
    for index, inst in enumerate(instruments):
        print(f"({index}): {inst}")
    print("Other inputs: Random")
    print("~" * 50)
    user_input = input("Enter instrument (number or random): ")
    if isinstance(user_input, str):
        if user_input.isdigit():
            user_input = int(user_input)
    if user_input not in np.arange(0, len(instruments)):
        user_input = random.randint(0, len(instruments)-1)
    return instruments[user_input]

def getArtist(inst):
    if inst == "Piano":
        print("Piano artists:")
        for index, inst in enumerate(pianoArtists):
            print(f"({index}): {inst}")
        print("Other inputs: Random")
        print("~" * 50)
        user_input = input("Enter artist (number or random): ")
        if user_input not in list(range(len(pianoArtists))):
            user_input = random.randint(0, len(pianoArtists)-1)
        user_input = pianoArtists[user_input]
    elif inst == "Violin":
        print("Violin artists:")
        for index, inst in enumerate(violinArtists):
            print(f"({index}): {inst}")
        print("Other inputs: Random")
        print("~" * 50)
        user_input = input("Enter artist (number or random): ")
        if user_input not in list(range(len(violinArtists))):
            user_input = random.randint(0, len(violinArtists)-1)
        user_input = violinArtists[user_input]
    else:
        print("Flute artists:")
        for index, inst in enumerate(fluteArtists):
            print(f"({index}): {inst}")
        print("Other inputs: Random")
        print("~" * 50)
        user_input = input("Enter artist (number or random): ")
        if user_input not in list(range(len(fluteArtists))):
            user_input = random.randint(0, len(fluteArtists)-1)
        user_input = fluteArtists[user_input]    

    print("")
    return user_input

def getTempo():
    print("Tempi:")
    for index, tempo in enumerate(tempi):
        print(f"({index}): {tempo}")
    print("Other inputs: Random")

    print("~" * 50)
    user_input = input("Enter tempo (number or random): ")
    if user_input not in np.arange(0, len(tempi)):
        user_input = random.randint(0, len(tempi)-1)

    user_input = tempi[user_input]
    return user_input

def getMeasures():
    user_input = input("Enter number of measures (default is 12, max is 100): ")

    if not isinstance(user_input, int):
        user_input = 12

    if user_input not in np.arange(1, 101):
        user_input = 12
        
    return user_input

def getFile():
    def find_dir(dir, search_path):
        for root, dirs, _ in os.walk(search_path):
            if dir in dirs:
                return os.path.join(root, dir)
        return None
    
    try:
        user_input = input("Enter write file (.mid): ")
        if user_input[-4:] != ".mid" or len(user_input) < 5:
            raise Exception("Invalid write file... will save as 'new_music.mid'")
    except Exception as input_error:
        print(input_error)
        return find_dir("generated_music", "../") + "/new_music.mid"

    return find_dir("generated_music", "../") + "/" + user_input
def getSheetMusicInput():
    return input("Would you like to generate sheet music? (y/n) ")

def getRepeat():
    print("~" * 50)
    return input("Would you like to generate music with the same settings? (y/n) ")

def musicTime():
    print("\n\n")
    print("AI MUSIC GENERATOR")
    print("-" * 100)
    inst = getInst()
    print("")
    artist = getArtist(inst)
    print("")
    tempo = getTempo()
    print("")
    numMeasures = getMeasures()
    print("")
    inputFile = getFile()
    print("")
    
    #inputFile = inst + artist + "_predicted.mid"
    showSheetMusic = False
    #if getSheetMusicInput() == 'y':
    #    showSheetMusic = True
    
    print("\n")
    print("-" * 100)
    print("Generating music...\n")
    
    generateMusic(inst, artist, tempo, numMeasures, inputFile, showSheetMusic)
    
    generateSame = True
    while generateSame:
        if getRepeat() == 'y':
            print("-" * 100)
            generateMusic(inst, artist, tempo, numMeasures, inputFile, showSheetMusic)
        else:
            generateSame = False

if __name__ == "__main__":
    print("Be advised: no flute models have been trained yet (as of 2/24/25")
    musicTime()
    print("")
    print("Happy music!")
    print("")