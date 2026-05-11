import tkinter as tk
from Ball_class import Ball, ensemble_balls
from Table_class import Table, table
import keyboard
import math
import main

list_fleche = []
dic_and_ball = {}


def fonction_quit():
    fenetre.destroy()


def DLC():
    Coeffficient_friction_text.place(
        x=45, y=main.HAUTEUR + 140 + 100, width=55, height=20
    )
    Coeffficient_friction.place(x=32, y=main.HAUTEUR + 140, width=50, height=100)
    Coeffficient_de_restitution.place(x=102, y=main.HAUTEUR + 140, width=50, height=100)
    Coeffficient_de_restitution_texte.place(
        x=109, y=main.HAUTEUR + 240, width=55, height=20
    )
    bouton.place(x=10, y=main.HAUTEUR + 150 + 120)


def supression_fleche():
    for f in list_fleche:
        canvas.delete(f)
    bouton.config(text=f"Lancer la ball a {vitesse.get()} m/s a {angle.get()} degree")


def deplacement_ball_initiation():
    supression_fleche()
    Vx = main.COOEFICIENT * (-vitesse.get() * math.cos(math.radians(180 + angle.get())))
    Vy = main.COOEFICIENT * (vitesse.get() * math.sin(math.radians(180 + angle.get())))
    ensemble_balls["white"].set_mouvement(angle.get(), vitesse.get())
    deplacement_ball(Vx, Vy)


def deplacement_ball(Vx, Vy, temps=0):
    print(f"{Vx, Vy},{temps}")
    for ball in ensemble_balls:
        if ensemble_balls[ball].norm != 0:
            canvas.move(dic_and_ball["white"], Vx, Vy)
    table.step_and_write(
        (
            temps,
            ensemble_balls["white"].centre(
                canvas.coords(ensemble_balls["white"].objet_canva)
            ),
            [Vx, Vy],
        )
    )
    if -main.EPSILON < Vx < main.EPSILON:
        Vx = 0
    else:
        Vx = Vx * (1 - main.FROTEMENT * main.PAT / 100)
    if -main.EPSILON < Vy < main.EPSILON:
        Vy = 0
    else:
        Vy = Vy * (1 - main.FROTEMENT * main.PAT / 100)

    print(f"{Vx, Vy},{temps}")
    if Vx != 0 or Vy != 0:
        canvas.after(
            main.PAT,
            deplacement_ball,
            Vx,
            Vy,
            temps + 1,
        )


def changement_test(donner):
    supression_fleche()
    print(
        canvas.coords(ensemble_balls["white"].objet_canva)[0]
        + 2 * main.RAYON
        + vitesse.get(),
        canvas.coords(ensemble_balls["white"].objet_canva)[1]
        + main.RAYON
        + vitesse.get(),
        math.cos(math.radians(angle.get())),
        math.sin(math.radians(angle.get())),
    )
    fleche = canvas.create_line(
        (canvas.coords(ensemble_balls["white"].objet_canva)[0]) + main.RAYON,
        canvas.coords(ensemble_balls["white"].objet_canva)[1] + main.RAYON,
        (canvas.coords(ensemble_balls["white"].objet_canva)[0] + main.RAYON)
        + -vitesse.get() * math.cos(math.radians(180 + angle.get())),
        (canvas.coords(ensemble_balls["white"].objet_canva)[1] + main.RAYON)
        + vitesse.get() * math.sin(math.radians(180 + angle.get())),
        arrow="last",
        width=3,
    )
    list_fleche.append(fleche)


fenetre = tk.Tk()
fenetre.title("Le billard rigolo des gigolos")
fenetre.attributes("-fullscreen", True)


angle = tk.Scale(fenetre, from_=0, to=360, command=changement_test)
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
    width=main.LONGEUR,
    height=main.HAUTEUR,
    bg="#4E4E4E",
)
canvas.place(x=0, y=0, width=main.LONGEUR, height=main.HAUTEUR)

canvas.create_rectangle(
    (main.BORDURE, main.BORDURE),
    ((main.LONGEUR - main.BORDURE), (main.HAUTEUR - main.BORDURE)),
    fill="green",
)
for cerlce in main.TROU:
    canvas.create_oval(*cerlce, fill="black")



for ball in ensemble_balls:
    INITIAL_POSITION = -20
    print(ball)
    print(ensemble_balls[ball])
    dic_and_ball[ball] = canvas.create_oval(
        (
            (INITIAL_POSITION, INITIAL_POSITION),
            (INITIAL_POSITION + 2 * main.RAYON, INITIAL_POSITION + 2 * main.RAYON),
        ),
        fill=ensemble_balls[ball].color,
    )
    ensemble_balls[ball].set_canva(dic_and_ball[ball])
    print(canvas.coords(ensemble_balls["white"].objet_canva))
canvas.move( dic_and_ball["white"],100, 250)
print(dic_and_ball)
# (x0, y0, x1, y1) = canvas.coords(ball)


bouton.place(x=10, y=main.HAUTEUR + 150, width=200, height=30)
angel_text.place(x=45, y=main.HAUTEUR + 115, width=40, height=20)
angle.place(x=32, y=main.HAUTEUR + 15, width=50, height=100)

vitesse_text.place(x=109, y=main.HAUTEUR + 115, width=40, height=20)
vitesse.place(x=102, y=main.HAUTEUR + 15, width=50, height=100)

Frame1.place(x=250, y=main.HAUTEUR + 10, width=500, height=200)


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
