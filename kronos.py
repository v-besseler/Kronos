import tkinter as tk
import datetime

class TimerWidget(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.running = False
        self.start_time = None
        self.button_start = tk.Button(self, width=8, text="Start", command=self.start)
        self.button_stop = tk.Button(self, width=8, text="Stop", command=self.stop)
        self.time_readout = tk.Label(self, text="0:00:00.000000", font=("FreeMono", 24))
        self.button_start.pack(side=tk.LEFT)
        self.button_stop.pack(side=tk.LEFT)
        self.time_readout.pack(fill=tk.X)
        self.pack()

    def start(self):
        self.start_time = datetime.datetime.now()
        self.running = True
        self.update_label()

    def current_timespan(self):
        return datetime.datetime.now() - self.start_time

    def update_label(self):
        if self.running:
            self.time_readout.config(text=str(self.current_timespan()))
            self.time_readout.after(100, self.update_label)

    def stop(self):
        self.running = False
        self.write_to_file()

    def write_to_file(self):
        file = open("python.txt", "a")
        message = str(self.start_time) + ", " + str(datetime.datetime.now()) + ", " + str(self.current_timespan()) + "\n"
        file.write(message)
        file.close()

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Kronos")

        ele = TimerWidget(self)
        ele.button_start.config(text="Python")
        ele.pack(side=tk.TOP)

        ele = TimerWidget(self)
        ele.button_start.config(text="HTML/CSS")
        ele.pack(side=tk.BOTTOM)

        ele = TimerWidget(self)
        ele.button_start.config(text="Java")
        ele.pack(side=tk.BOTTOM)
        self.pack()

def main():
    root = tk.Tk()
    app = App(root)
    app.mainloop()

main()

