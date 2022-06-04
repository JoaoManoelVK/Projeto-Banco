#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    Jun 04, 2022 02:43:19 PM -03  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import banco_support

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
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+361+109")
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

        self.cadastrar = ttk.Button(self.Frame1)
        self.cadastrar.place(relx=0.446, rely=0.725, height=25, width=76)
        self.cadastrar.configure(takefocus="")
        self.cadastrar.configure(text='''Cadastrar''')
        self.cadastrar.configure(compound='left')

        self.username = ttk.Entry(self.Frame1)
        self.username.place(relx=0.413, rely=0.396, relheight=0.046
                , relwidth=0.291)
        self.username.configure(takefocus="")
        self.username.configure(cursor="ibeam")

        self.password = ttk.Entry(self.Frame1)
        self.password.place(relx=0.413, rely=0.462, relheight=0.046
                , relwidth=0.291)
        self.password.configure(takefocus="")
        self.password.configure(cursor="ibeam")

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.264, rely=0.396, height=19, width=75)
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''USERNAME:''')
        self.TLabel1.configure(compound='left')

        self.TLabel2 = ttk.Label(self.Frame1)
        self.TLabel2.place(relx=0.264, rely=0.462, height=19, width=75)
        self.TLabel2.configure(background="#ffffff")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''PASSWORD:''')
        self.TLabel2.configure(compound='left')

        self.TLabel3 = ttk.Label(self.Frame1)
        self.TLabel3.place(relx=0.38, rely=0.198, height=39, width=155)
        self.TLabel3.configure(background="#ffffff")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="-family {SimSun-ExtB} -size 24 -weight bold")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''BEM VINDO''')
        self.TLabel3.configure(compound='left')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

class Menu:
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
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("500x300+420+82")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Menu")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.BTdeposito = ttk.Button(self.top)
        self.BTdeposito.place(relx=0.3, rely=0.4, height=25, width=206)
        self.BTdeposito.configure(takefocus="")
        self.BTdeposito.configure(text='''Deposito''')
        self.BTdeposito.configure(compound='left')

        self.BTsaque = ttk.Button(self.top)
        self.BTsaque.place(relx=0.3, rely=0.533, height=25, width=206)
        self.BTsaque.configure(takefocus="")
        self.BTsaque.configure(text='''Saque''')
        self.BTsaque.configure(compound='left')

        self.BTextrato = ttk.Button(self.top)
        self.BTextrato.place(relx=0.3, rely=0.667, height=25, width=206)
        self.BTextrato.configure(takefocus="")
        self.BTextrato.configure(text='''Extrato''')
        self.BTextrato.configure(compound='left')

        self.TLabel1 = ttk.Label(self.top)
        self.TLabel1.place(relx=0.34, rely=0.033, height=39, width=155)
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="-family {SimSun} -size 24")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''BEM VINDO''')
        self.TLabel1.configure(compound='left')

        self.Nameuser = ttk.Label(self.top)
        self.Nameuser.place(relx=0.4, rely=0.2, height=21, width=101)
        self.Nameuser.configure(background="#ffffff")
        self.Nameuser.configure(foreground="#000000")
        self.Nameuser.configure(font="-family {Segoe UI} -size 9")
        self.Nameuser.configure(relief="flat")
        self.Nameuser.configure(anchor='w')
        self.Nameuser.configure(justify='center')
        self.Nameuser.configure(text='''Nome''')
        self.Nameuser.configure(compound='left')

class Cadastro:
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
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+378+86")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Cadastro")
        top.configure(background="#ffffff")
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

        self.name = ttk.Entry(self.Frame1)
        self.name.place(relx=0.397, rely=0.22, relheight=0.046, relwidth=0.241)
        self.name.configure(takefocus="")
        self.name.configure(cursor="ibeam")

        self.CPF = ttk.Entry(self.Frame1)
        self.CPF.place(relx=0.397, rely=0.308, relheight=0.046, relwidth=0.241)
        self.CPF.configure(takefocus="")
        self.CPF.configure(cursor="ibeam")

        self.number = ttk.Entry(self.Frame1)
        self.number.place(relx=0.397, rely=0.396, relheight=0.046
                , relwidth=0.241)
        self.number.configure(takefocus="")
        self.number.configure(cursor="ibeam")

        self.login = ttk.Entry(self.Frame1)
        self.login.place(relx=0.397, rely=0.484, relheight=0.046, relwidth=0.241)

        self.login.configure(takefocus="")
        self.login.configure(cursor="ibeam")

        self.password = ttk.Entry(self.Frame1)
        self.password.place(relx=0.397, rely=0.571, relheight=0.046
                , relwidth=0.241)
        self.password.configure(takefocus="")
        self.password.configure(cursor="ibeam")

        self.typeaccount = ttk.Combobox(self.Frame1)
        self.typeaccount.place(relx=0.397, rely=0.659, relheight=0.046
                , relwidth=0.236)
        self.value_list = ['poupança,corrente',]
        self.typeaccount.configure(values=self.value_list)
        self.typeaccount.configure(takefocus="")

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.314, rely=0.22, height=19, width=44)
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Nome:''')
        self.TLabel1.configure(compound='left')

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.331, rely=0.308, height=19, width=35)
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''CPF:''')
        self.TLabel1.configure(compound='left')

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.298, rely=0.396, height=19, width=55)
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Numero:''')
        self.TLabel1.configure(compound='left')

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.314, rely=0.484, height=19, width=44)
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Login:''')
        self.TLabel1.configure(compound='left')

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.314, rely=0.571, height=19, width=45)
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Senha:''')
        self.TLabel1.configure(compound='left')

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.248, rely=0.659, height=19, width=84)
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Tipo de Conta:''')
        self.TLabel1.configure(compound='left')

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.066, rely=0.066, height=49, width=505)
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="-family {Arial} -size 24 -weight bold")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''INSIRA AS SUAS INFORMAÇÕES''')
        self.TLabel1.configure(compound='left')

        self.Cadastrar = ttk.Button(self.Frame1)
        self.Cadastrar.place(relx=0.446, rely=0.835, height=25, width=76)
        self.Cadastrar.configure(takefocus="")
        self.Cadastrar.configure(text='''Cadastrar''')
        self.Cadastrar.configure(compound='left')

        self.TEntry1 = ttk.Entry(self.Frame1)
        self.TEntry1.place(relx=0.397, rely=0.747, relheight=0.046
                , relwidth=0.241)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.231, rely=0.747, height=19, width=95)
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#030303")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Cheque Especial:''')
        self.TLabel1.configure(compound='left')

class deposito:
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

        top.geometry("600x450+379+83")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Toplevel 3")
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

def start_up():
    banco_support.main()

if __name__ == '__main__':
    banco_support.main()



