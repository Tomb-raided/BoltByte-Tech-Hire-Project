import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
try:
    import PIL 
except:
    messagebox.showerror("Error, library PIL failed to Initialise, please read the README.MD file and restart the Program")