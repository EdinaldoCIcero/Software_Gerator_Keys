import PySimpleGUI as sg
from random import randint
import re 
import os
import sys
import string 
import random



sg.theme("DarkGrey3")

Cores = [ "#ffffff"  , "#0091ff" , "#242424" , "#ba4747" ]



class AppClass():
    def __init__(self):

        self.list_senha = []
        self.list_senha_for_save = []


        self.lay = [
                #---------------------------------------------------------------------------------------
                #[sg.Image(filename = None,size = (720, 160))]
                [sg.Canvas(canvas=None, background_color=Cores[0],size=(720, 160)) ,],
                #---------------------------------------------------------------------------------------
                [
                sg.Text("URL do video",text_color=Cores[3] , size=( 10 , 1))
                ],

                #---------------------------------------------------------------------------------------
                [sg.HorizontalSeparator(color=Cores[3],key="separador002")],

                #---------------------------------------------------------------------------------------
                [
                sg.Canvas(canvas=None, background_color=Cores[2],size=(50, 5)),
                sg.Slider(range = (0, 100),size=(60 , 10) , default_value = 0 ,orientation="horizontal" , key="sizekey")
                ],

                #---------------------------------------------------------------------------------------
                [sg.HSeparator()],
                
                #---------------------------------------------------------------------------------------
                [sg.Canvas(canvas=None, background_color=Cores[2],size=(10, 20))],

                #---------------------------------------------------------------------------------------
                [
                sg.Canvas(canvas=None, background_color=Cores[2],size=(178, 5)),
                sg.Button("gerar senha ", button_color=None, key="down", size=(30,1))
                ],

                #---------------------------------------------------------------------------------------
                [sg.Canvas(canvas=None, background_color=Cores[2],size=(10, 20))],

                #---------------------------------------------------------------------------------------
                [ 
                sg.Canvas(canvas=None, background_color=Cores[2],size=(170, 5)) ,
                sg.InputText(size=(40,2) , background_color="#e0e0e0", pad=(0 ,(0 , 10 )) , key="saida")
                ],

                #---------------------------------------------------------------------------------------

                [sg.Canvas(canvas=None, background_color=Cores[2],size=(100, 42))],
                [sg.HSeparator()],
                #---------------------------------------------------------------------------------------
                [
                sg.Canvas(canvas=None, background_color=Cores[2],size=(500, 2)),
                #sg.FolderBrowse("Buscar" , key="path") ,
                sg.Button("salvar senha", button_color=None, key="save", size=(21,1))
                ],

                [
                sg.Canvas(canvas=None, background_color=Cores[2],size=(200, 2)),
                sg.Text("criado por:EdinaldoCicero/Átomos Games Studios",auto_size_text= 2 , text_color=Cores[0] ,size=(30,1),s=(1,1))]
                ]


        self.layout = [
                    [self.lay],

                    ]


        self.janela = sg.Window("Gerator_Keys",background_color=None , size=(720,480)).layout(self.layout)

        pass



    def Update(self):
        while True:
            self.events, self.values = self.janela.Read()
            LINES = ("--"*20)
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break

            if self.events == "down":
                senha_final = string.ascii_letters + string.digits + '!@#$%¨&*()-_=+[]<>,.;:?'
                ran = random.SystemRandom()
                self.janela["saida"].update( "".join(ran.choice(senha_final) for i in range( int( self.values["sizekey"] ) ) ))
                

            if self.events == "save":
                self.list_senha.append(self.values["saida"])

                with open( "senha_gerada.txt" , "w" ) as openedfile:
                    openedfile.write( LINES + "\n" + "SENHA CRAIDA : " + self.list_senha[0] + "\n" + LINES )
                    #print( self.list_senha )
                    self.list_senha = []


app = AppClass()
app.Update()