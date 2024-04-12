import customtkinter as ctk
import json

class ctk_core:
    def init(self):
        settings = json.load(open("settings.json", "r"))
        self.x_scale = float(settings["RESX"]) / 1920.0
        self.y_scale = float(settings["RESY"]) / 1080.0
        print("x_scale: {}, y_scale: {}".format(self.x_scale, self.y_scale))
        
    def init_ctk(self):
        ctk.set_appearance_mode("dark")
        self.root = ctk.CTk()
        self.root.geometry("1600x800")
        self.root.title("analog-py-designer")
        
    def ctk_run(self):
        self.load_model()
        self.root.mainloop()

    def quit(self):
        self.root.quit()
        self.root.destroy()