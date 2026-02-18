import tkinter as tk

class gui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jednostavna Fullscreen Aplikacija")
        
        # Postavljanje aplikacije preko cijelog ekrana
        self.window.attributes('-fullscreen', True)
        
        # Dodavanje gumba za izlaz (pritiskom na ESC)
        self.window.bind("<Escape>", self.exit_app)
        
        # Jednostavna oznaka na sredini ekrana
        self.label = tk.Label(self.window, text="Pozdrav! Ovo je fullscreen aplikacija.", font=("Arial", 24))
        self.label.pack(expand=True)
        
        # Gumb za otvaranje popup prozora
        self.popup_button = tk.Button(self.window, text="Otvori Popup", command=self.show_popup, font=("Arial", 16))
        self.popup_button.pack(pady=20)

    def show_popup(self):
        # Kreiranje popup prozora
        popup = tk.Toplevel(self.window)
        popup.title("Informacija")
        popup.geometry("400x200")
        
        # Tekst u popup prozoru
        message = tk.Label(popup, text="Ovo je popup prozor!\n\nKliknite Zatvori za izlaz.", font=("Arial", 14))
        message.pack(expand=True, pady=20)
        
        # Gumb za zatvaranje popup-a
        close_button = tk.Button(popup, text="Zatvori", command=popup.destroy, font=("Arial", 12))
        close_button.pack(pady=10)

    def exit_app(self, event=None):
        self.window.destroy()

    def run(self):
        self.window.mainloop()


if __name__ =="__main__":
    GUI = gui()
    GUI.run()