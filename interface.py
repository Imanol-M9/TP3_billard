import tkinter as tk
import keyboard


COOEFICIENT = 4
HAUTEUR = 122 * COOEFICIENT
LONGEUR = 214 * COOEFICIENT
BORDURE = 10 * COOEFICIENT
RAYON = 5 * COOEFICIENT

TROU = (
    (
        ((LONGEUR // 2 - RAYON), (BORDURE - RAYON)),
        ((LONGEUR // 2 + RAYON), (BORDURE + RAYON)),
    ),
    (
        (
            (LONGEUR // 2 - RAYON),
            (HAUTEUR - BORDURE - RAYON),
        ),
        (
            (LONGEUR // 2 + RAYON),
            (HAUTEUR - BORDURE + RAYON),
        ),
    ),
    (
        ((BORDURE - RAYON), (BORDURE - RAYON)),
        ((BORDURE + RAYON), (BORDURE + RAYON)),
    ),
    (
        ((LONGEUR - BORDURE - RAYON), (HAUTEUR - BORDURE - RAYON)),
        ((LONGEUR - BORDURE + RAYON), (HAUTEUR - BORDURE + RAYON)),
    ),
    (
        ((LONGEUR - BORDURE - RAYON), (BORDURE - RAYON)),
        ((LONGEUR - BORDURE + RAYON), (BORDURE + RAYON)),
    ),
    (
        ((BORDURE - RAYON), (HAUTEUR - BORDURE - RAYON)),
        ((BORDURE + RAYON), (HAUTEUR - BORDURE + RAYON)),
    ),
)


def fonction_quit():
    fenetre.destroy()


def deplacement_ball_initiation():
    print("ttttttttttttttttttt")
    Vx = vitesse.get()
    Vy = vitesse.get()
    deplacement_ball(Vx, Vy)


def deplacement_ball(Vx, Vy):
    print(f"{Vx, Vy}")
    canvas.move(ball, Vx, Vy)
    if Vx > 0 and Vy > 0:
        canvas.after(25, deplacement_ball, Vx - 1, Vy - 1)


def changement_test(donner):
    bouton.config(text=f"Lancer la ball a {vitesse.get()} m/s a {angle.get()} degree")
    print(
        canvas.coords(ball)[0] + RAYON + vitesse.get(),
        canvas.coords(ball)[1] + RAYON / 2 + vitesse.get(),
    )


fenetre = tk.Tk()
fenetre.title("Le billard rigolo des gigolos")
fenetre.attributes("-fullscreen", True)


angle = tk.Scale(fenetre, from_=0, to=180, command=changement_test)
angel_text = tk.Label(fenetre, text="angle")
vitesse = tk.Scale(fenetre, from_=-50, to=50, command=changement_test)
vitesse_text = tk.Label(fenetre, text="m/s")


bouton = tk.Button(
    fenetre,
    text=f"Lancer la ball a {vitesse.get()} m/s a {angle.get()} degree",
    command=deplacement_ball_initiation,
)

canvas = tk.Canvas(
    fenetre,
    width=LONGEUR,
    height=HAUTEUR,
    bg="#4E4E4E",
)
canvas.place(x=0, y=0, width=LONGEUR, height=HAUTEUR)

canvas.create_rectangle(
    (BORDURE, BORDURE),
    ((LONGEUR - BORDURE), (HAUTEUR - BORDURE)),
    fill="green",
)
for cerlce in TROU:
    canvas.create_oval(*cerlce, fill="black")

ball = canvas.create_oval(*((100, 100), (100 + RAYON, 100 + RAYON)), fill="white")

fleche = canvas.create_line(
    (canvas.coords(ball)[0]) + RAYON,
    canvas.coords(ball)[1] + RAYON / 2,
    canvas.coords(ball)[0] + RAYON + vitesse.get() + 100,
    canvas.coords(ball)[1] + RAYON / 2 + vitesse.get() + 100,
    arrow="last",
    width=3,
)


(x0, y0, x1, y1) = canvas.coords(ball)
canvas.move(ball, 1, 0)
(x0f, y0f, x1f, y1f) = canvas.coords(ball)


racourti_clav = tk.Label(
    fenetre,
    text="liste racourcise est clavier\n "
    "Escape --> sortire du programe\n "
    "Enter --> effectuer le calcule\n "
    "Ctrl BackSpace  --> vider la console d'entrer",
)


bouton.place(x=10, y=HAUTEUR + 150, width=200, height=30)
angel_text.place(x=43, y=HAUTEUR + 115, width=40, height=20)
angle.place(x=30, y=HAUTEUR + 15, width=50, height=100)

vitesse_text.place(x=107, y=HAUTEUR + 115, width=40, height=20)
vitesse.place(x=100, y=HAUTEUR + 15, width=50, height=100)

racourti_clav.grid(row=1, column=6, padx=5, pady=5)


keyboard.add_hotkey("esc", fonction_quit)
# keyboard.add_hotkey("enter", deplacement_ball(vitesse.get(),vitesse.get()))
# keyboard.add_hotkey("",None)


fenetre.mainloop()
