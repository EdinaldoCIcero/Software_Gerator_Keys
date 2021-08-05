import PySimpleGUI as sg
from pytube import YouTube
import re 
import os
import sys




sg.theme("DarkBrown4")

Cores = [ "#ffffff"  , "#0091ff" , "#242424" , "#ba4747" ]



class AppClass():
    def __init__(self):
        
        self.ImagemLayer = [
        [sg.Canvas(canvas=None, background_color=Cores[0] ,size=(150, 300) )],
        #[sg.Image(filename = None,size = (None, None))]
        ]


        self.lay = [
                
                #---------------------------------------------------------------------------------------
                #[sg.Image(filename = None,size = (None, None))]
                [sg.Canvas(canvas=None, background_color=Cores[0],size=(720, 120)) ,],


                [
                sg.Text("URL do video",text_color=Cores[3] , size=( 10 , 1))
                ],
                #---------------------------------------------------------------------------------------

                #---------------------------------------------------------------------------------------
                [sg.HorizontalSeparator(color=Cores[3],key="separador002")],

                
                #---------------------------------------------------------------------------------------
                #[sg.Canvas(canvas=None, background_color=Cores[2],size=(70, 5)) ,],
                #---------------------------------------------------------------------------------------

                [
                sg.Canvas(canvas=None, background_color=Cores[2],size=(70, 5)) , 
                sg.Checkbox("360" , text_color=Cores[3], key="360" ),

                sg.Canvas(canvas=None, background_color=Cores[2],size=(70, 5)) , 
                sg.Checkbox("720" , text_color=Cores[3], key="720" )
                ],


                #---------------------------------------------------------------------------------------
                [sg.HSeparator()],
                
                #---------------------------------------------------------------------------------------
                [ sg.Canvas(canvas=None, background_color=Cores[2],size=(200, 5)),
                sg.Multiline(default_text="",autoscroll=False , size=(30,0),background_color="#e0e0e0",text_color=None ,key ="Mult")],
                #[sg.Output(size=(40,5),  background_color=Cores[3] ,key="out") ],

                [
                #sg.HSeparator(),
                sg.Button("Download_video", button_color=Cores[3], key="down", size=(21,1)),
                
                ],

                ]


        self.layout = [
                [self.lay  

                #self.ImagemLayer
                #sg.Column(self.ImagemLayer),
                #sg.VSeparator(),
                ],

                ]


        self.janela = sg.Window("Gerator_Keys",background_color=Cores[2] , size=(720,480)).layout(self.layout)



    def Update(self):
        while True:
            self.events, self.values = self.janela.Read()

            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break

            if self.events == "down":
                self.values["Mult"] = "alfagouangowug"




app = AppClass()
app.Update()