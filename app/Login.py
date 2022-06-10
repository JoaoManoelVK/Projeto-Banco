import tkinter.ttk as ttk
import tkinter as tk

from tkinter.constants import *

import sys

import main as app


class Login:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 
        self.style = ttk.Style()

        if sys.platform == "win32":
            self.style.theme_use('winnative')

        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x470+410+113")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Login")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.008)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.login = ttk.Button(self.Frame1)
        self.login.place(relx=0.446, rely=0.615, height=25, width=76)
        self.login.configure(takefocus="")
        self.login.configure(text='''Login''')
        self.login.configure(compound='left')
        self.login.configure(command= app.menu)

        self.cadastrar = ttk.Button(self.Frame1)
        self.cadastrar.place(relx=0.446, rely=0.724, height=25, width=76)
        self.cadastrar.configure(takefocus="")
        self.cadastrar.configure(text='''Cadastrar''')
        self.cadastrar.configure(compound='left')
        self.cadastrar.configure(command= app.cadastrar)

        self.username = ttk.Entry(self.Frame1)
        self.username.place(relx=0.413, rely=0.396, relheight=0.044, relwidth=0.291)
        self.username.configure(takefocus="")
        self.username.configure(cursor="ibeam")

        self.password = ttk.Entry(self.Frame1)
        self.password.place(relx=0.413, rely=0.461, relheight=0.044, relwidth=0.291)
        self.password.configure(takefocus="")
        self.password.configure(cursor="ibeam")

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.264, rely=0.396, height=20, width=75)
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''USERNAME:''')
        self.TLabel1.configure(compound='left')

        self.TLabel2 = ttk.Label(self.Frame1)
        self.TLabel2.place(relx=0.264, rely=0.461, height=20, width=75)
        self.TLabel2.configure(background="#ffffff")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''PASSWORD:''')
        self.TLabel2.configure(compound='left')

        self.TLabel3 = ttk.Label(self.Frame1)
        self.TLabel3.place(relx=0.38, rely=0.198, height=41, width=155)
        self.TLabel3.configure(background="#ffffff")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="-family {SimSun-ExtB} -size 24 -weight bold")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''BEM VINDO''')
        self.TLabel3.configure(compound='left')

        self.menubar = tk.Menu(top,font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu = self.menubar)
