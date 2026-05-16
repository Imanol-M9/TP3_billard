import tkinter as tk
from Ball_class import Ball, ensemble_balls
from Table_class import Table, table
import keyboard
import math
import time
import main
import random
import numpy as np
import presimulation as simu


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
    simu.all_frame = simu.Liste_Frame()
    supression_fleche()
    for ball in ensemble_balls:
        ensemble_balls[ball].set_mouvement(math.radians(-angle.get()), vitesse.get())
    dic_and_ball = {}
    for ball in ensemble_balls:
        dic_and_ball[ball] = {
            "position": ensemble_balls[ball].position,
            "norm": ensemble_balls[ball].norm,
            "angle": ensemble_balls[ball].angle,
            "vitesse": [ensemble_balls[ball].speed[0], ensemble_balls[ball].speed[1]],
            "objet": ensemble_balls[ball].objet_canva,
        }
        # current["white"],np.cos*[ball]["angle"] *current["norm"],np.sin*current["angle"] *current["norm"])
    simu.all_frame.insertEnd(dic_and_ball)
    deplacement_ball()


def deplacement_ball(temps=0):
    # print(
    #     f"{ensemble_balls['white'].speed[0], ensemble_balls['white'].speed[1], 'norm :', np.linalg.norm(ensemble_balls['white'].speed), ensemble_balls['white'].angle}"
    # )
    # print(ensemble_balls["white"])
    dic_and_ball = {}

    for ball in ensemble_balls:
        # print(
        #     f"setage de norm avec{ensemble_balls[ball].speed[0], ensemble_balls[ball].speed[1]}"
        # )
        ensemble_balls[ball].next_step()
        ensemble_balls[ball].set_position_mouvement()
    for ball in ensemble_balls:
        dic_and_ball[ball] = {
            # "position": canvas.coords(ensemble_balls[ball].objet_canva),
            "position":ensemble_balls[ball].position,
            "norm": ensemble_balls[ball].norm,
            "angle": ensemble_balls[ball].angle,
            "temps": temps,
            "vitesse": [ensemble_balls[ball].speed[0], ensemble_balls[ball].speed[1]],
            "objet": ensemble_balls[ball].objet_canva,
        }
        # deplacement_ball(ensemble_balls["white"].speed[0], ensemble_balls["white"].speed[1])
    print(dic_and_ball["white"]["position"])
    simu.all_frame.insertEnd(dic_and_ball)

    if ensemble_balls["white"].norm != 0:
        canvas.after(
            main.PAT,
            deplacement_ball,
            temps + 1,
        )
    else:
        affichage(simu.all_frame.head)


def affichage(fram):
    for ball in fram.info:
        canvas.coords(dic_and_ball[ball], fram.info[ball]["position"])
    next_fram = fram.prochain
    if fram.prochain != None:
        canvas.after(main.PAT, affichage, next_fram)


def changement_test(donner):
    supression_fleche()
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
vitesse = tk.Scale(fenetre, from_=0, to=25, command=changement_test)
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
print(
    main.BORDURE, main.BORDURE, main.LONGEUR - main.BORDURE, main.HAUTEUR - main.BORDURE
)
for cerlce in main.TROU:
    canvas.create_oval(*cerlce, fill="black")


# for ball in ensemble_balls:
#     INITIAL_POSITION_x = random.randint(0,0)
#     INITIAL_POSITION_y = random.randint(0,0)
#     # print(ball)
#     # print(ensemble_balls[ball])
#     dic_and_ball[ball] = canvas.create_oval(
#         (
#             (INITIAL_POSITION_x, INITIAL_POSITION_y),
#             (INITIAL_POSITION_x + 2 * main.RAYON, INITIAL_POSITION_y + 2 * main.RAYON),
#         ),
#         fill=ensemble_balls[ball].color,
#     )
#     ensemble_balls[ball].set_position(
#         (
#             INITIAL_POSITION_x,
#             INITIAL_POSITION_y,
#             INITIAL_POSITION_x + 2 * main.RAYON,
#             INITIAL_POSITION_y + 2 * main.RAYON,
#         )
#     )
#     ensemble_balls[ball].set_canva(dic_and_ball[ball])
# print(canvas.coords(ensemble_balls["white"].objet_canva))
# canvas.move(dic_and_ball["white"], 100, 250)
# canvas.create_rectangle(
#     50, 50, 806, 438, fill="black"
# )
canvas.create_oval(np.float64(797.7436646735027), np.float64(418.0), np.float64(817.7436646735027), np.float64(438.0), fill="red")
dic_and_ball["white"] = canvas.create_oval(
    100, 100, 100+2*main.RAYON, 100+2*main.RAYON, fill=ensemble_balls["white"].color
)
ensemble_balls["white"].set_canva(dic_and_ball["white"])
ensemble_balls["white"].set_position(canvas.coords(ensemble_balls["white"].objet_canva))
# print(dic_and_ball)
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
