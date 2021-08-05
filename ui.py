import tkinter as tk

class App(tk.Frame):

    def __init__(self, color='#111313', font= ('Helvetica 25 bold')):
        super().__init__()
        self.color = color
        self["bg"] = self.color
        self.memory = {"font": ('Helvetica 25 bold')}


        self.pack(fill=tk.BOTH, expand=True)

        closeButton = StopButton(self)
        closeButton.place(relx=.5, rely=0.9, anchor= tk.S)

class UIElement():

    memory = {}

    def inherit(self, *elements):
        for elm in elements:
            self[elm] = self.master.memory[elm]
            self.memory[elm] = self.master.memory[elm]

class StopButton(tk.Button, UIElement):

    def __init__(self, parent, text = "Stop"):
        super().__init__(parent, text=text, command=self.stop)
        self.inherit("font")

        self["bg"] = "#CC2800"
        self["padx"] = 5
        self["pady"] = 5
        self["activebackground"] = "#00CC28"

    def stop(self):
        self["text"] = "Stopped"
        pass

class Leveler(tk.Scale, UIElement):

    def __init__(self, parent, pins: tuple, start = 0, end = 100, vertical = True):
        super().__init__(parent, 
                from_=start, to=end, 
                orient = tk.VERTICAL if vertical else tk.HORIZONTAL
            )

        self.pins = pins
        self.start = start
        self.end = end
        self.direction = vertical
        self.initiate()
        self.inherit()

    def initiate(self):
        pass

class AutoLeveler(Leveler):

    def __init__(self, parent, motors_pins: tuple, switch_pins: tuple, start = 0, end = 100, vertical = True):
        self.switch_pins = switch_pins
        super().__init__(parent, motors_pins, start, end = 100, vertical = True)

    def initiate(self):
        self.set()
        pass