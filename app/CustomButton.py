from customtkinter import *

class Button(CTkButton):
    def __init__(self,master,text,command=None,**kwargs):
        super().__init__(master,text=text,command=command,**kwargs)
