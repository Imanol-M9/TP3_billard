import tkinter as tk
from Ball_class import Ball, ensemble_balls
from Table_class import Table, table
import keyboard
import math
import main


COOEFICIENT = 4
HAUTEUR = 122 * COOEFICIENT
LONGEUR = 214 * COOEFICIENT
BORDURE = 10 * COOEFICIENT
RAYON = 5 * COOEFICIENT
PAT = 25
FROTEMENT = 0.3
list_fleche = []

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


def DLC():
    Coeffficient_friction_text.place(x=45, y=HAUTEUR + 140 + 100, width=55, height=20)
    Coeffficient_friction.place(x=32, y=HAUTEUR + 140, width=50, height=100)
    Coeffficient_de_restitution.place(x=102, y=HAUTEUR + 140, width=50, height=100)
    Coeffficient_de_restitution_texte.place(x=109, y=HAUTEUR + 240, width=55, height=20)
    bouton.place(x=10, y=HAUTEUR + 150 + 120)


def supression_fleche():
    for f in list_fleche:
        canvas.delete(f)
    bouton.config(text=f"Lancer la ball a {vitesse.get()} m/s a {angle.get()} degree")


def deplacement_ball_initiation():
    supression_fleche()
    Vx = COOEFICIENT * (-vitesse.get() * math.cos(math.radians(180 + angle.get())))
    Vy = COOEFICIENT * (vitesse.get() * math.sin(math.radians(180 + angle.get())))
    ensemble_balls[0].set_mouvement(angle.get(), vitesse.get())
    deplacement_ball(Vx, Vy, 0)


def deplacement_ball(Vx, Vy, temps=0):
    if -main.EPSILON < Vx < main.EPSILON:
        Vx = 0
    if -main.EPSILON < Vy < main.EPSILON:
        Vy = 0
    print(f"{Vx, Vy},{temps}")
    canvas.move(ball, Vx, Vy)
    table.step_and_write((temps, canvas.coords(ball), [Vx, Vy]))
    if Vx < main.EPSILON:
        Vx = 0
    else:
        Vx = Vx * (1 - FROTEMENT * PAT / 100)
    if Vy < main.EPSILON:
        Vy = 0
    else:
        Vy = Vy * (1 - FROTEMENT * PAT / 100)
    print(f"{Vx, Vy},{temps}")
    if Vx != 0 or Vy != 0:
        canvas.after(
            PAT,
            deplacement_ball,
            Vx,
            Vy,
            temps + 1,
        )


def changement_test(donner):
    supression_fleche()
    print(
        canvas.coords(ball)[0] + RAYON + vitesse.get(),
        canvas.coords(ball)[1] + RAYON / 2 + vitesse.get(),
        math.cos(math.radians(angle.get())),
        math.sin(math.radians(angle.get())),
    )
    fleche = canvas.create_line(
        (canvas.coords(ball)[0]) + RAYON / 2,
        canvas.coords(ball)[1] + RAYON / 2,
        (canvas.coords(ball)[0] + RAYON / 2)
        + -vitesse.get() * math.cos(math.radians(180 + angle.get())),
        (canvas.coords(ball)[1] + RAYON / 2)
        + vitesse.get() * math.sin(math.radians(180 + angle.get())),
        arrow="last",
        width=3,
    )
    list_fleche.append(fleche)


fenetre = tk.Tk()
fenetre.title("Le billard rigolo des gigolos")
fenetre.attributes("-fullscreen", True)


angle = tk.Scale(fenetre, from_=0, to=180, command=changement_test)
angel_text = tk.Label(fenetre, text="angle")
vitesse = tk.Scale(fenetre, from_=-25, to=25, command=changement_test)
vitesse_text = tk.Label(fenetre, text="m/s")

Coeffficient_friction = tk.Scale(fenetre, from_=0, to=1, resolution=0.01)
Coeffficient_friction_text = tk.Label(fenetre, text="frotement")
Coeffficient_de_restitution = tk.Scale(fenetre, from_=0, to=100)
Coeffficient_de_restitution_texte = tk.Label(fenetre, text="perte E (%)")

Frame1 = tk.Frame(fenetre, borderwidth=2, relief="groove")


COULEUR = "#7216CE"
COULEUR_FOND = "#000000"
retour_ini = tk.Button(
    Frame1,
    text="<<",
    font=("Arial", 14),
    fg=COULEUR_FOND,
    bg=COULEUR,
    width=10,
    height=2,
    padx=10,
    pady=5,
    relief=tk.RAISED,
)
retour_moin_un = tk.Button(
    Frame1,
    text="<",
    font=("Arial", 14),
    fg=COULEUR_FOND,
    bg=COULEUR,
    width=10,
    height=2,
    padx=10,
    pady=5,
    relief=tk.RAISED,
)
pause = tk.Button(
    Frame1,
    text="⏸",
    font=("Arial", 14),
    fg=COULEUR_FOND,
    bg=COULEUR,
    width=10,
    height=2,
    padx=10,
    pady=5,
    relief=tk.RAISED,
)
continu = tk.Button(
    Frame1,
    text="▶",
    font=("Arial", 14),
    fg=COULEUR_FOND,
    bg=COULEUR,
    width=10,
    height=2,
    padx=10,
    pady=5,
    relief=tk.RAISED,
)
avant_un = tk.Button(
    Frame1,
    text=">",
    font=("Arial", 14),
    fg=COULEUR_FOND,
    bg=COULEUR,
    width=10,
    height=2,
    padx=10,
    pady=5,
    relief=tk.RAISED,
)
fin_sim = tk.Button(
    Frame1,
    text=">>",
    font=("Arial", 14),
    fg=COULEUR_FOND,
    bg=COULEUR,
    width=10,
    height=2,
    padx=10,
    pady=5,
    relief=tk.RAISED,
)


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


(x0, y0, x1, y1) = canvas.coords(ball)
canvas.move(ball, 1, 0)
(x0f, y0f, x1f, y1f) = canvas.coords(ball)


bouton.place(x=10, y=HAUTEUR + 150, width=200, height=30)
angel_text.place(x=45, y=HAUTEUR + 115, width=40, height=20)
angle.place(x=32, y=HAUTEUR + 15, width=50, height=100)

vitesse_text.place(x=109, y=HAUTEUR + 115, width=40, height=20)
vitesse.place(x=102, y=HAUTEUR + 15, width=50, height=100)

Frame1.place(x=250, y=HAUTEUR + 10, width=500, height=200)


DIMENTION = 50

retour_ini.place(x=0, y=0, width=DIMENTION, height=DIMENTION)
retour_moin_un.place(x=DIMENTION, y=0, width=DIMENTION, height=DIMENTION)
pause.place(x=2 * DIMENTION, y=0, width=DIMENTION, height=DIMENTION)
continu.place(x=3 * DIMENTION, y=DIMENTION, width=DIMENTION, height=DIMENTION)
avant_un.place(x=3 * DIMENTION, y=0, width=DIMENTION, height=DIMENTION)
fin_sim.place(x=4 * DIMENTION, y=0, width=DIMENTION, height=DIMENTION)

keyboard.add_hotkey("esc", fonction_quit)
keyboard.add_hotkey("Alt+f+4", DLC)

keyboard.add_hotkey("enter", deplacement_ball_initiation)
# keyboard.add_hotkey("",None)


if __name__ == "__main__":
    fenetre.mainloop()
