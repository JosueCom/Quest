import tkinter as tk
  
# creating window
window = tk.Tk()
  
# setting attribute
window.attributes('-fullscreen', True)
window.configure(bg='#AFC4C0')
window.title("Quest")
  
# creating text label to display on window screen
label = tk.Label(window, text="Hello Tkinter!")
label.pack()
  
window.mainloop()