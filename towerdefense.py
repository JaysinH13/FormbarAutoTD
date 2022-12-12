#Imports
import tkinter
import webbrowser


#Code
window = tkinter.Tk()
def map01():
    webbrowser.open('Maps\map01.py')
def map02():
    webbrowser.open('Maps\map02.py')
def map03():
    webbrowser.open('Maps\map03.py')
def map04():
    webbrowser.open('Maps\map04.py')
def map05():
    webbrowser.open('Maps\map05.py')
def where_dja_go():
    webbrowser.open('Maps\where_dja_go.py')
def jiggle_n_juke():
    webbrowser.open('Maps\jiggle_n_juke.py')
def outer_loop():
    webbrowser.open('Maps\outer_loop.py')
def celtic_knot():
    webbrowser.open('Maps\celtic_knot.py')
def mouse():
    webbrowser.open('Maps\mouse.py')


b1 = tkinter.Button(text='Map#01', command=map01, width=50)
b1.pack()
b2 = tkinter.Button(text='Map#02', command=map02, width=50)
b2.pack()
b3 = tkinter.Button(text='Map#03', command=map03, width=50)
b3.pack()
b4 = tkinter.Button(text='Map#04', command=map04, width=50)
b4.pack()
b5 = tkinter.Button(text='Map#05', command=map05, width=50)
b5.pack()
b6 = tkinter.Button(text='Celtic Knot', command=celtic_knot, width=50)
b6.pack()
b7 = tkinter.Button(text='Outer Loop', command=outer_loop, width=50)
b7.pack()
b8 = tkinter.Button(text="Where'dja Go?", command=where_dja_go, width=50)
b8.pack()
b9 = tkinter.Button(text="Jiggle'n'Juke", command=jiggle_n_juke, width=50)
b9.pack()
b10 = tkinter.Button(text="Mouse Info", command=mouse, width=50)
b10.pack()

window.mainloop()
