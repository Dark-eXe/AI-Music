
from ast import Delete
from operator import delitem
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile #helps by asking user to open a specific file
from tkinter import filedialog #helps to create file/directory windows
from tkinter import messagebox #helps show users errors
from theAI import mid_button #file that will do the function calls and talking between our gui and our ai
import tkinter
import tkinter.messagebox
import customtkinter
import pygame 
import os
import time

# This program intends to create an graphical user-interface for our AI-generated music project.
# Start Date: 2022-10-10

#Code by Tariq
#THe code in the link below has a tutorial on how to get started
#https://realpython.com/python-gui-tkinter/

#Update: Since tkinter looks like windows 98, let's use this modern library for tkinter from github
#https://github.com/TomSchimansky/CustomTkinter
#Documentation can be found -> https://github.com/TomSchimansky/CustomTkinter/wiki
#use this to install-> pip3 install customtkinter 

#starts the intial GUI window

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
#button default color
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 330
    HEIGHT = 400


    def __init__(self):
        super().__init__()

        self.title("AI Music- AI generated Music")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        self.resizable(False, False) #Turns off fullscreen or resizing mode

         # ============ create two frames ============

        # Create a top and bottom fram we don't use a grid layout

        self.frame_top = customtkinter.CTkFrame(master=self,
                                                 width=App.WIDTH,
                                                 height=App.HEIGHT,
                                                 corner_radius=0, border_width=0)
        self.frame_top.pack(fill = BOTH)

        self.frame_bottom = customtkinter.CTkFrame(master = self, width=App.WIDTH, height=App.HEIGHT, corner_radius=0, border_width=0)
        self.frame_bottom.pack(fill = BOTH,side = BOTTOM, expand = True)

        #The title to our program
        self.label_1 = customtkinter.CTkLabel(master=self.frame_top,
                                              text="AI MUSIC GENERATOR",
                                              font=("Roboto Medium", 16))  # font name and size in px
        self.label_1.pack(side = TOP)
        
        global showSheetMusic
        showSheetMusic = False
        def sheetMusic_event():
            global showSheetMusic
            if showSheetMusic:
                showSheetMusic = False
                #print("switch toggled, current value:", switch_var.get(),showSheetMusic)
            else:
                showSheetMusic = True
                #print("switch toggled, current value:", switch_var.get(),showSheetMusic)

        def open_helpWindow():
            helpwin = Tk()
            #helpwin.geometry("400 x 250")


            w1 = Label(helpwin, text ='Welcome to AI Music Help', font = ('default_theme', 16)) 
            w1.pack()
            w2 = Label(helpwin, text ='Select the Instrument from the first dropdown bar', font = ('default_theme', 15)) 
            w2.pack()
            w3 = Label(helpwin, text ='Select the Artist from the second dropdown bar', font = ('default_theme', 15)) 
            w3.pack()
            w4 = Label(helpwin, text ='Select the Tempo from the third dropdown bar', font = ('default_theme', 15)) 
            w4.pack()
            w5 = Label(helpwin, text ='Enter a numerical value for the measure value.', font = ('default_theme', 15)) 
            w5.pack()
            w6 = Label(helpwin, text ='Choose if you want the music to be displayed on a music sheet.', font = ('default_theme', 15)) 
            w6.pack()
            w7 = Label(helpwin, text ='Afterwards please indicate where you want to store your file.', font = ('default_theme', 15)) 
            w7.pack()
            w8 = Label(helpwin, text ='Then click to generate your song. This will take a moment.', font = ('default_theme', 15)) 
            w8.pack()
            w9 = Label(helpwin, text ='If you choose to leave any choice blank it will randomize it for you.', font = ('default_theme', 15)) 
            w9.pack() 
            #messagebox.showinfo("HELP", "WELcome")
            helpwin.mainloop()


            #top = Toplevel(win)
            helpwin.title("Help")
            #Add the text stuff for this location
            
        #print(os.path.abspath('../ai'))
        #Sets current value of buttons before user entry
        tempoVar = customtkinter.StringVar(value = "Tempo")
        artistVar = customtkinter.StringVar(value = "Artist")
        timeSigVar = customtkinter.StringVar(value = "Time Signature")
        keyVar = customtkinter.StringVar(value = "Key")
        instrumentVar = customtkinter.StringVar(value = "Instrument")
        measuresVar = customtkinter.StringVar(value = "Measure")

        #Button to choose tempo
        self.tempo_button = customtkinter.CTkOptionMenu(master=self.frame_top,
                                                values=["Largo", "Adagio", "Andante", "Moderato", "Allegro", "Presto", "Slow", "Moderate", "Fast"],
                                                height=30, width=165, font= ('default_theme', 16), variable=tempoVar)
       
    
        pianoArt = ["Bach","Chopin","Debussy","Ellington","Corea","Anime"]
        violinArt = ["Mozart","Paganini","Vivaldi"]
        fluteArt = ["Brahms","Wagner"]

        def instrument_manager(e):
            if self.instrument_button.get() == "Piano":
                self.artist_button.configure(values = pianoArt)
            elif self.instrument_button.get() == "Violin":
                self.artist_button.configure(values = violinArt)
            elif self.instrument_button.get() == "Flute":
                self.artist_button.configure(values = fluteArt)

        def artist_manager(e):
            if self.artist_button.get() == "Bach":
                self.instrument_button.configure(values = ["Piano"])
            elif self.artist_button.get() == "Chopin":
                self.instrument_button.configure(values = ["Piano"])
            elif self.artist_button.get() == "Debussy":
                self.instrument_button.configure(values = ["Piano"])
            elif self.artist_button.get() == "Ellington":
                self.instrument_button.configure(values = ["Piano"])
            elif self.artist_button.get() == "Corea":
                self.instrument_button.configure(values = ["Piano"])
            elif self.artist_button.get() == "Anime":
                self.instrument_button.configure(values = ["Piano"])
            elif self.artist_button.get() == "Mozart":
                self.instrument_button.configure(values = ["Violin"])
            elif self.artist_button.get() == "Paganini":
                self.instrument_button.configure(values = ["Violin"])             
            elif self.artist_button.get() == "Vivaldi":
                self.instrument_button.configure(values = ["Violin"])
            elif self.artist_button.get() == "Brahms":
                self.instrument_button.configure(values = ["Flute"])
            elif self.artist_button.get() == "Wagner":
                self.instrument_button.configure(values = ["Flute"])

        #Instruments button
        self.instrument_button = customtkinter.CTkOptionMenu(master=self.frame_top,
                                                values=["Piano", "Violin", "Flute"],command=instrument_manager,
                                                height=30, width = 165, font= ('default_theme', 16), variable=instrumentVar)

        #Artist button
        self.artist_button = customtkinter.CTkOptionMenu(master=self.frame_top,
                                                values=["Bach", "Chopin", "Debussy", "Ellington", "Corea", "Anime", "Mozart", "Paganini", "Vivaldi", "Brahms", "Wagner"],
                                                height=30, width = 165, font= ('default_theme', 16), variable=artistVar)

        #Help button
        self.help_button = customtkinter.CTkButton(master = self.frame_bottom, height=30, width = 30, font= ('default_theme', 13), text= "Help", command=open_helpWindow)


        #Sheet music button
        switch_var = customtkinter.StringVar(value="off")
        self.SheetMusic_button = customtkinter.CTkSwitch(master = self.frame_bottom, text= "Sheet Music",command=sheetMusic_event, 
                                                        font= ('default_theme', 13),variable=switch_var, onvalue="on", offvalue="off")

        #User entry for measures
        self.measures_entry = customtkinter.CTkEntry(master = self.frame_bottom, placeholder_text="Measure Value")

        #The label that reads measures
        self.measuresLabel = customtkinter.CTkLabel(master = self.frame_bottom, height=30, width = 80, font= ('default_theme', 13), text="Measures:")
        
        #currently not used
        self.appearance_label = customtkinter.CTkLabel(master=self.frame_bottom, text="Change Theme:", font= ('default_theme', 10))

        #currently doesnt exist
        self.theme_switch = customtkinter.CTkSwitch(master=self.frame_bottom,
                                                    text=["Dark Mode"],
                                                    command=self.changeUITheme, font= ('default_theme', 10))

        #currently useless for switching themes
        self.theme_switch.select()

        self.createSongButton = customtkinter.CTkButton(master=self.frame_bottom,
                                                text="Create Music",
                                                command=self.create_button, height=40, width = 165, font= ('default_theme', 18), state='disabled')

        #Button for selectFile
        self.selectFile = customtkinter.CTkButton(master=self.frame_bottom, text = "File Location", command = self.get_file_path, height=30, width = 165, font= ('default_theme', 16))

        self.fileSaveNameText = customtkinter.CTkLabel(master = self.frame_bottom, width = 100, height = 25)

        # THIS AREA IS EXCLUSIVELY FOR PACKING THINGS THEY NEED TO BE PACKED IN A CORRECT ORDER DON'T PACK OUTSIDE THIS UNLESS IT IS IN A FUNCTION
            #Top from part of pack
        self.instrument_button.pack(side = TOP, pady = 8)
        self.artist_button.pack(side = TOP, pady = 8)
        #self.timeSig_button.pack(side = TOP, pady = 5)
        self.tempo_button.pack(side = TOP, pady = 8)
        #self.key_button.pack(side = TOP, pady = 5)
        self.SheetMusic_button.place(anchor = S, relx = .5, rely = .3)
        
        #Bottom part of pack
        self.measuresLabel.place(anchor = S, relx = .33, rely = .15)
        self.measures_entry.place(anchor = S, relx = .66, rely = .15)

        self.createSongButton.pack(side = BOTTOM, pady = 5)
        #self.theme_switch.pack(side = LEFT, pady = 5)        
        #self.appearance_label.pack(side = LEFT, pady = 5)
        self.selectFile.pack(side = BOTTOM, pady = 5)
        #self.help_button.pack()
        self.help_button.place(anchor = NW, bordermode = INSIDE, relx = 0.87, rely = 0.87)
        

    def IntializePygame(self):
        # Shili ....
        # Initiating pygame package for sound/music features.
        pygame.init()
        pygame.mixer.init()
    
    # Muhammad: Added a dark mode and light mode function to cha1nge the theme of the UI
    def changeUITheme(self):
        if self.theme_switch.get() == 1:
            self.theme_switch.configure(text=["Dark Mode"])
            customtkinter.set_appearance_mode("dark")
        else:
            self.theme_switch.configure(text=["Light Mode"])
            customtkinter.set_appearance_mode("light")

    # a frequently asked questions window
    def openFAQWindow(self):
        newWindow = Tk()
        newWindow.title("Frequently Asked Questions")
        newsize = Frame(newWindow)
        newsize.pack(fill=BOTH, expand=True)
        faq1 = customtkinter.CTkButton(newsize, text='Why should I use this application for music?', font="120", command=
        print("This application provides a unique way of creating music that meets the requirements of the given inputs."))
        faq1.pack(fill = BOTH, expand = True)
        faq2 = customtkinter.CTkButton(newsize, text='What is the purpose of this application?', font="120", command=
        print("This application is intended to create music by using Artifical Intelligence with given inputs such as instruments, artists, and tempo."))
        faq2.pack(fill = BOTH, expand = True)
        faq3 = customtkinter.CTkButton(newsize, text='Is this application free to use?', font="120", command=
        print("As of right now, this application is free to use, but will include monetization in the future."))
        faq3.pack(fill = BOTH, expand = True)
        faq4 = customtkinter.CTkButton(newsize, text='Will I be able to save the generated music files', font="120", command=
        print("Yes, you may save the newly created music file."))
        faq4.pack(fill = BOTH, expand = True)
        newWindow.mainloop()
        # we can add more questions as this application develops               

    def get_file_path(self):
        #stuff for selecting file var and function
        global file_path_var
        # Open and return file path
        file_path_var = tkinter.filedialog.asksaveasfilename(filetypes = [('Midi File', '*.mid')], defaultextension = '.mid')
        self.fileSaveNameText.configure(text = file_path_var)
        self.fileSaveNameText.pack_forget        
        self.fileSaveNameText.pack(side = BOTTOM)
        #Turns on create song button only if a file location was selected
        if file_path_var != "":
            self.createSongButton.configure(state = 'normal')

    def create_button(self):
        #Jaylen - The following code gets all the correct parameters that were selected by the user
        global instruments 
        instruments = self.instrument_button.get()
        global measures
        measures = self.measures_entry.get()
        measures = int(measures)
        global tempo
        tempo = self.tempo_button.get()
        global artist
        artist = self.artist_button.get()

        #Jaylen - The following code calls mid_button from theAI to start generating and open the file from theAI.py
        # moved this function here to open the file right away (or throw error if no file was able to be made).
        # our application should be able to open any (.mid) music files that it can play through
        global mid_file
        mid_file = mid_button(instruments, artist, tempo, measures, file_path_var, showSheetMusic)

        '''
        # check if the file has been opened
        if mid_file is not None:
            music = mid_file.read()
            print(music)
            self.music
            self.play_button = customtkinter.CTkButton(master=self.frame_top, text="Play", command=self.play)
            self.pause_button = customtkinter.CTkButton(master=self.frame_top, text="Pause", command=self.pause)
            self.terminates = customtkinter.CTkButton(master=self.frame_top, text="Terminate", command = self.terminate)
        else:
            messagebox.showerror('error', 'Unable to open file ' + mid_file)
        '''

    # Shili--Creates button for playsong, pausesong, and terminate. 
    def music(self):
        self.play_button.pack(side = BOTTOM, pady = 8)
        self.pause_button.pack(side = BOTTOM, pady = 7)
        self.terminates.pack(side = BOTTOM, pady = 6)
    def play(self):
        pygame.mixer.music.load(mid_file)
        pygame.mixer.music.play(loops=0)
    def pause(self):
        pygame.mixer.music.pause()
    def terminate(self):
        pygame.mixer.music.stop()
        
    #Code to be executed when the app closes
    #We could later on add some code to close open files, auto save if the user didn't manually save or
    #offer a would you like to save prompt etc....
    def on_closing(self, event=0):
        self.destroy()

    



#Calls the GUI - Tariq
#We should consider using perhaps MVC "Model-View Controller "to layout our classes and functions

if __name__ == "__main__":
    print("Running UI version of get_music")
    print("Be advised: sheet music functionality has not been tested since the original BitBucket")
    app = App()
    app.mainloop()
    print("Happy music!")
    print("")
    #app.IntializePygame()
    #app.on_closing()


