import tkinter as tk
import keyboard
import time

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
    angle.config(text="postfix : erreur")
    angel_text.config(text="résultat : erreur")
    erreur_page.config(text="")


def deplacement_ball():
    canvas.move(ball, 100, 100)


fenetre = tk.Tk()
fenetre.title("Le billard rigolo des gigolos")
fenetre.attributes("-fullscreen", True)


angle = tk.Scale(fenetre, from_=0, to=180)
angel_text = tk.Label(fenetre, text="angle")
vitesse = tk.Scale(fenetre, from_=-50, to=50)
vitesse_text = tk.Label(fenetre, text="m/s")
erreur_page = tk.Label(fenetre, text=" ")
Bouton = tk.Button(
    fenetre,
    text=f"Lancer la ball a {vitesse.get()} m/s a {angle.get()} degree",
    command=None,
)
racourti_clav = tk.Label(
    fenetre,
    text="liste racourcise est clavier\n "
    "Escape --> sortire du programe\n "
    "Enter --> effectuer le calcule\n "
    "Ctrl BackSpace  --> vider la console d'entrer",
)

Bouton.place(x=10, y=HAUTEUR + 150, width=200, height=30)
angel_text.place(x=43, y=HAUTEUR + 115, width=40, height=20)
angle.place(x=30, y=HAUTEUR + 15, width=50, height=100)

vitesse_text.place(x=107, y=HAUTEUR + 115, width=40, height=20)
vitesse.place(x=100, y=HAUTEUR + 15, width=50, height=100)

racourti_clav.grid(row=1, column=6, padx=5, pady=5)


keyboard.add_hotkey("esc", fonction_quit)
keyboard.add_hotkey("enter", deplacement_ball)
# keyboard.add_hotkey("",None)


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
(x0, y0, x1, y1) = canvas.coords(ball)
canvas.move(ball, 100, 100)
(x0f, y0f, x1f, y1f) = canvas.coords(ball)


print(x0)
print(x0f)
fenetre.mainloop()
