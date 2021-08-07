import PySimpleGUI as sg
from random import randint
import re 
import os
import sys
import string 
import random


import Notify as ny 
import bases_imagens as bimg



#sg.theme("DarkGrey3")


Cores = [ "#ffffff"  , "#0091ff" , "#242424" , "#ba4747" ]
background_image= bimg.back_fundo_base64



def title_bar(title, text_color, background_color):
    bc = background_color
    tc = text_color
    font = 'Helvetica 12'

    return [sg.Col([[sg.T(title, text_color=tc, background_color=bc, font=font, grab=True)]], pad=(0, 0), background_color=bc),

            sg.Col([[sg.T('_', text_color=tc, background_color=bc, enable_events=True, font=font, key='-MINIMIZE-'),

            sg.Text('❎', text_color=tc, background_color=bc, font=font, enable_events=True, key='Exit')]], 
                    element_justification='r', key='-C-', grab=True,pad=(0, 0), background_color=bc)]


class AppClass():
    def __init__(self , background_image ):

        sg.Window._move_all_windows = True

        self.list_senha = []
        self.list_senha_for_save = []

        self.background_layout = [ title_bar('RandomPassaworld_1234', Cores[1], Cores[2] ),[sg.Image(data=background_image)] ]

        self.window_background = sg.Window('Background', self.background_layout, no_titlebar=True, finalize=True, margins=(0, 0),element_padding=(0,0) ,size=(720,480) ,right_click_menu=[[''], ['Exit',]])

        self.window_background['-C-'].expand(True, False, False)  



        self.lay = [
                #---------------------------------------------------------------------------------------
                [sg.Canvas(canvas=None, background_color=sg.theme_background_color(),size=(10, 50)) ,],
                [sg.Image(filename ="img/logosoft.png",size = (720, 105))],
                
                #---------------------------------------------------------------------------------------
                [
                sg.Canvas(canvas=None, background_color=sg.theme_background_color(),size=(180, 5)),
                sg.Text("Arraste no slider para definir o tamnho da sua senha .",text_color=Cores[0] , size=( 50 , 1))
                ],

                #---------------------------------------------------------------------------------------
                [sg.HSeparator()],

                #---------------------------------------------------------------------------------------
                [
                sg.Canvas(canvas=None, background_color=sg.theme_background_color(),size=(80, 5)),
                sg.Slider(range = (0, 100),size=(60 , 10) , default_value = 0 ,orientation="horizontal" , key="sizekey")
                ],
  
                #---------------------------------------------------------------------------------------
                [sg.Canvas(canvas=None, background_color=sg.theme_background_color(),size=(10, 20))],

                #---------------------------------------------------------------------------------------
                [
                sg.Canvas(canvas=None, background_color=sg.theme_background_color(),size=(210, 5)),
                sg.Button("", button_color=(sg.theme_background_color(),sg.theme_background_color() ), border_width=0,key="down", size=(30,1) , image_data=bimg.g_senha  )
                ],

                #---------------------------------------------------------------------------------------
                [sg.Canvas(canvas=None, background_color=sg.theme_background_color(),size=(10, 20))],

                #---------------------------------------------------------------------------------------
                [ 
                sg.Canvas(canvas=None, background_color=sg.theme_background_color(),size=(200, 5)) ,
                sg.InputText(size=(40,2) , background_color="#e0e0e0", pad=(0 ,(0 , 10 )) , key="saida")
                ],

                #---------------------------------------------------------------------------------------
                [sg.Canvas(canvas=None, background_color=sg.theme_background_color(),size=(100, 42))],
                [sg.HSeparator()],

                #---------------------------------------------------------------------------------------
                [
                sg.Canvas(canvas=None, background_color=sg.theme_background_color(),size=(500, 2)),
                sg.Button("", image_data=bimg.salvar_senha , button_color=(sg.theme_background_color(),sg.theme_background_color() ), border_width=0, key="save", size=(21,1)) 
                ],

                #---------------------------------------------------------------------------------------
                [
                sg.Canvas(canvas=None, background_color=sg.theme_background_color(),size=(200, 80)),
                sg.Text("criado por:EdinaldoCicero/Átomos Games Studios",auto_size_text= 2 , text_color=Cores[0] ,size=(30,1),s=(1,1))]
                ]


        self.layout = [ [self.lay] ]


        self.janela = sg.Window('Gerator_Keys', self.layout,finalize=True, keep_on_top=True, grab_anywhere=False,  transparent_color=sg.theme_background_color(), no_titlebar=True)


    def Update(self):
        LINES = ("--"*20)

        while True:
            self.window, self.events, self.values = sg.read_all_windows()
            if self.events is None or self.events == 'Cancel' or self.events == 'Exit':
                break

            if self.events == "down":
                senha_final = string.ascii_letters + string.digits + '!@#$%¨&*()-_=+[]<>,.;:?'
                ran = random.SystemRandom()
                self.janela["saida"].update( "".join(ran.choice(senha_final) for i in range( int( self.values["sizekey"] ) ) ))
                

            if self.events == "save":
                self.list_senha.append(self.values["saida"])
                with open( "senha_gerada.txt" , "w" ) as openedfile:
                    openedfile.write( LINES + "\n" + "SENHA CRAIDA : " + self.list_senha[0] + "\n" + LINES )
                    self.list_senha = []

                nnn = ny.Noti( titulo="SENHA_SALVA" , mensagen="Sua senha foi salva com sussesso!" )




        self.janela.close()
        self.window_background.close()


if __name__ == '__main__':
    
    app = AppClass(background_image)

    app.Update()
