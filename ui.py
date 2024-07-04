import random
import tkinter as tk
from random import randint
from tkinter import PhotoImage

def spieler_festlegen():
    global spielereingabe, entry_widgets,players
    entry_widgets = []
    def safe_player():
        global players
        n_game.config(state="disabled")
        players = [entry.get() for entry in entry_widgets]
        spielereingabe.destroy()
        update_player_display()

    def spieler_namen_eingabe(anzahl):
        try:
            vali = int(anzahl)
        except ValueError:
            return
        spieler_anzahl.destroy()
        for i in range(int(anzahl)):
            tk.Label(spielereingabe,text=f'Spieler {i+1}').pack()
            entry = tk.Entry(spielereingabe)
            entry.pack()
            entry_widgets.append(entry)
        tk.Button(spielereingabe,text="Speichern", command=safe_player).pack(padx=5,pady=5)
    spielereingabe = tk.Tk()
    spielereingabe.title("Legen Sie Ihre Spieler fest")
    spielereingabe.geometry('300x500')
    tk.Label(spielereingabe,text='Wie viele Spieler sollen Spielen?', font=('Arial',12), pady=2, padx=2).pack()
    spieler_anzahl = tk.Entry(spielereingabe)
    spieler_anzahl.pack()
    spieler_anzahl.bind('<Return>', lambda event: spieler_namen_eingabe(spieler_anzahl.get()))
    spielereingabe.mainloop()

def update_player_display():
    for widget in spieler_anzeige.winfo_children():
        widget.destroy()
    for player in players:
        tk.Button(spieler_anzeige, text=f'{player} | P:{0}',padx=50).pack(side=tk.LEFT, padx=2)



def wueferln():
    global anzahl_wurf, counter
    if counter < 3 :
        w_becher_u_pfad = 'assets/becher-u.png'
        w_becher_u_bild = PhotoImage(file=w_becher_u_pfad)
        w_becher_label.config(image=w_becher_u_bild)
        w_becher_label.image = w_becher_u_bild
        # Clear existing dice images
        for widget in dice_frame.winfo_children():
            widget.destroy()

        dice_images = []

        for _ in range(3):
            wuerfel_pfad = f'assets/{random.randint(1, 6)}.png'
            wuerfel_bild = tk.PhotoImage(file=wuerfel_pfad)
            dice_images.append(wuerfel_bild)
            tk.Label(dice_frame, image=wuerfel_bild).pack(side=tk.LEFT, padx=5)
        counter += 1
        anzahl_wurf.set(f'Würfe: {counter}')


        dice_frame.dice_images = dice_images
    else:
        counter = 0





players = []
counter = 0

#GUI
main = tk.Tk()
main.title('Schocken')
main.geometry('1280x720')
main.resizable(False, False)

#Navbar
navbar = tk.Frame(main, bg='grey')
navbar.pack(side=tk.TOP,fill=tk.X)
n_game = tk.Button(navbar,text='New Game', command=spieler_festlegen)
n_game.pack(side=tk.LEFT, padx=5,pady=5)
highscore = tk.Button(navbar, text='Leaderbord')
highscore.pack(side=tk.LEFT, padx=5,pady=5)

#Content
content = tk.Frame(main,bg='green')
content.pack(side=tk.TOP,expand=True, fill=tk.BOTH)

#Player Labels
spieler_anzeige = tk.Frame(content, bg='gold', pady=2)
spieler_anzeige.pack(side=tk.TOP,fill=tk.X)

#Playground
playground = tk.Frame(content, bg='green',padx=10,pady=10,width=300)
playground.pack(side=tk.LEFT)

w_becher_pfad = 'assets/becher.png'
w_becher_bild = PhotoImage(file=w_becher_pfad)
w_becher_label = tk.Label(playground,image=w_becher_bild, bg='green')
w_becher_label.pack()
w_becher_label.bind('<Button-1>',lambda event: wueferln())
dice_frame = tk.Frame(playground, bg='green')
dice_frame.pack()
rauslegen = tk.Frame(playground, bg='brown', padx=30,pady=30,width=213, height=70)
rauslegen.pack(pady=10)

#Status
status = tk.Frame(main, bg='green',padx=3,pady=3)
status.pack(side=tk.TOP, fill=tk.X)


#Wurfanzeige
anzahl_wurf = tk.StringVar()
wurfanzeige = tk.Label(status, textvariable=anzahl_wurf, fg='white', bg='green', font=('Arial', 13,'bold'))
wurfanzeige.pack(side=tk.LEFT)


main.mainloop()