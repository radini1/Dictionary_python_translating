from tkinter import *
from PyDictionary import PyDictionary
from sys import builtin_module_names

root = Tk()
root.geometry('800x500')
root.title('Dictionary')

dictionary = PyDictionary
def dict():  
    meaning.config(text=dictionary.meaning(word.get()))['noun'][0]
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))
    
Label(root, text="Dictionary", font=("Arial", 20, "bold"), fg="blue").pack(pady=10)
frame = Frame(root)
Label(frame, text="Type word ", font=("Helvetica", 15, "bold"))
word = Entry(frame, font=("Helvetica", 15, "bold"))
word.pack()
frame.pack(pady=10)

frame1 = Frame(root)
Label(frame1, text="Meaning ", font=("Helvetica", 12, "bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Helvetica", 12, "bold"))
meaning.pack()
frame1.pack(pady=10)

frame2 = Frame(root)
Label(frame2, text="Synonym ", font=("Helvetica", 12, "bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Helvetica", 12, "bold"))
synonym.pack()
frame2.pack(pady=10)

frame3 = Frame(root)
Label(frame3, text="Antonym", font=("Helvetica", 12, "bold")).pack(side=LEFT)
antonym = Label(frame3, text="", font=("Helvetica", 12, "bold"))
antonym.pack()
frame3.pack(pady=10)

Button(root, text="submit", font=("Helvetica", 14, "bold",), bg='silver', command=dict).pack()

root.mainloop()


    


