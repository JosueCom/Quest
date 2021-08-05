import tkinter as tk
import ui
  
# creating window
window = tk.Tk()
  
# setting attribute
window.attributes('-fullscreen', True)
window.configure(bg='#111313')
window.title("Quest")
  
# creating text label to display on window screen
app = ui.App()
  
window.mainloop()