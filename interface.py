import tkinter as tk
import main
from Ball_class import Ball, ensemble_balls
import exception_perso as ex
import fonctions_pour_fichier_configuration as fich_con
import presimulation as simu
import keyboard
import math
import random


is_renable = True
pause = False
is_running = False
nombre_fram_ecouler = 0
list_fleche = []
dic_and_ball = {}


def fonction_quit():
    fenetre.destroy()


def DLC():
    Coeffficient_friction_text.place(
        x=45, y=main.cfg["HAUTEUR"] + 140 + 100, width=55, height=20
    )
    Coeffficient_friction.place(x=32, y=main.cfg["HAUTEUR"] + 140, width=50, height=100)
    Coeffficient_de_restitution.place(
        x=102, y=main.cfg["HAUTEUR"] + 140, width=50, height=100
    )
    Coeffficient_de_restitution_texte.place(
        x=109, y=main.cfg["HAUTEUR"] + 240, width=55, height=20
    )
    bouton.place(x=10, y=main.cfg["HAUTEUR"] + 150 + 120)


def supression_fleche():
    for f in list_fleche:
        canvas.delete(f)
    bouton.config(
        text=f"Lancer la ball a {vitesse.get()} m/s a {angle.get()} degree", fg="black"
    )


def deplacement_ball_initiation_erreur_texte():
    # la raison pour laquel je faire ça c'est pour pas avoir tout la fonction suivant en try exepte
    global is_running, is_renable
    enleve_erreur()
    try:
        if is_running == True:
            raise ex.MyError("peux pas runer un sim is deja runer")
        if is_renable == False:
            raise ex.MyError(
                "vous etres en deplacement dans la simulation \n imposible de lancer un ball"
            )
        else:
            deplacement_ball_initiation()
    except ex.MyError as e:
        affiche_erreur(e)


def deplacement_ball_initiation():
    global is_running
    is_running = True
    simu.all_frame = simu.Liste_Frame()
    supression_fleche()
    ensemble_balls["white"].set_mouvement(math.radians(-angle.get()), vitesse.get())
    for ball in ensemble_balls:
        if ball != "white":
            ensemble_balls[ball].set_mouvement(0, 0)
    dic_and_ball = {}
    for ball in ensemble_balls:
        dic_and_ball[ball] = Ball(
            color=ball,
            position=ensemble_balls[ball].position,
            norm=ensemble_balls[ball].norm,
            objet_canva=ensemble_balls[ball].objet_canva,
        )

    simu.all_frame.insertEnd(dic_and_ball)
    deplacement_ball()


def deplacement_ball(temps=0):
    dic_and_ball = {}
    for ball in ensemble_balls:
        ensemble_balls[ball].friction()
        ensemble_balls[ball].coll_avec_ball(ensemble_balls)
        ensemble_balls[ball].collision_with_wall()
        ensemble_balls[ball].set_position_mouvement()
        dic_and_ball[ball] = Ball(
            color=ball,
            position=ensemble_balls[ball].position,
            norm=ensemble_balls[ball].norm,
            objet_canva=ensemble_balls[ball].objet_canva,
        )

    simu.all_frame.insertEnd(dic_and_ball)

    ball_imobile = 0
    for ball in ensemble_balls:
        if ensemble_balls[ball].norm == 0:
            ball_imobile +=1
    if ball_imobile != len(ensemble_balls):
        temps += 1
        deplacement_ball(temps)
    else:
        affichage(simu.all_frame.head)
        

def affichage(fram):
    global nombre_fram_ecouler, is_running, pause
    for ball in fram.info:
        canvas.coords(dic_and_ball[ball], fram.info[ball].position)
    next_fram = fram.prochain
    nombre_fram_ecouler += 1
    if fram.prochain != None:
        canvas.after(main.cfg["PAT"], affichage, next_fram)
    else:
        is_running = False
        bouton.config(fg="black")
        fram = simu.all_frame.head
        while fram.prochain != None:
            fram = fram.prochain
        fich_con.conteneur["donnees"] = fram.info


def changement_test(donner):
    supression_fleche()
    fleche = canvas.create_line(
        ((canvas.coords(ensemble_balls["white"].objet_canva)[0]) + main.cfg["RAYON"]),
        (canvas.coords(ensemble_balls["white"].objet_canva)[1] + main.cfg["RAYON"]),
        (canvas.coords(ensemble_balls["white"].objet_canva)[0] + main.cfg["RAYON"])
        + -vitesse.get() * math.cos(math.radians(180 + angle.get())) * 2,
        (canvas.coords(ensemble_balls["white"].objet_canva)[1] + main.cfg["RAYON"])
        + vitesse.get() * math.sin(math.radians(180 + angle.get())) * 2,
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


def retour_initial():
    global nombre_fram_ecouler, is_renable, is_running
    bouton.config(fg="red")
    is_renable = False
    try:
        if is_running == True:
            raise ex.MyError(
                "la simulation est en train d'etre rouler \n attendre la fin avant de faire cette operation"
            )
        for ball in simu.all_frame.head.info:
            canvas.coords(dic_and_ball[ball], simu.all_frame.head.info[ball].position)
        nombre_fram_ecouler = 1
    except AttributeError:
        message = "imposible de faire l'action de retour a la possition initial \n si auqu'un simulation n'a ete faite prealablement"
        affiche_erreur(message)
    except ex.MyError as e:
        affiche_erreur(e)
    else:
        enleve_erreur()


def demar_fin():
    global is_running
    try:
        if is_running == True:
            raise ex.MyError(
                "la simulation est en train d'etre rouler \n attendre la fin avant de faire cette operation"
            )
        retour_fin(simu.all_frame.head)
    except AttributeError:
        message = "imposible de faire l'action de retour a la fin \n si auqu'un simulation n'a ete faite prealablement"
        affiche_erreur(message)
    except ex.MyError as e:
        affiche_erreur(e)
    else:
        enleve_erreur()
        bouton.config(fg="black")


def retour_fin(fram):
    global nombre_fram_ecouler, is_renable
    nombre_fram_ecouler = 0
    is_renable = True
    while fram.prochain != None:
        nombre_fram_ecouler += 1
        fram = fram.prochain
    for ball in fram.info:
        canvas.coords(dic_and_ball[ball], fram.info[ball].position)


def avance_un():
    global nombre_fram_ecouler, is_renable
    try:
        fram = simu.all_frame.head
        if is_running == True:
            raise ex.MyError(
                "la simulation est en train d'etre rouler \n attendre la fin avant de faire cette operation"
            )
        if nombre_fram_ecouler >= simu.all_frame.taille - 1:
            bouton.config(fg="black")
        if nombre_fram_ecouler >= simu.all_frame.taille:
            raise ex.MyError(
                "Impossible de d'avancer,\n vous etes deja a la fin de la simulation"
            )
        for i in range(nombre_fram_ecouler):
            fram = fram.prochain
        nombre_fram_ecouler += 1
        good_fram = fram.prochain
        for ball in good_fram.info:
            canvas.coords(dic_and_ball[ball], good_fram.info[ball].position)
    except ex.MyError as e:
        is_renable = True
        affiche_erreur(e)
    except AttributeError:
        is_renable = True
        message = "imposible de faire l'action d'avance d'une frame \n si auqu'un simulation n'a ete faite prealablement"
        affiche_erreur(message)

    else:
        enleve_erreur()


def recule_un():
    global nombre_fram_ecouler, is_renable
    is_renable = False
    bouton.config(fg="red")
    try:
        if is_running == True:
            raise ex.MyError(
                "la simulation est en train d'etre rouler \n attendre la fin avant de faire cette operation"
            )
        fram = simu.all_frame.head
        if nombre_fram_ecouler <= 1:
            raise ex.MyError(
                "Impossible de reculer, vous etes deja au debut de la simulation"
            )
        for i in range(nombre_fram_ecouler):
            fram = fram.prochain
        nombre_fram_ecouler -= 1
        good_fram = fram.avant
        for ball in good_fram.info:
            canvas.coords(dic_and_ball[ball], good_fram.info[ball].position)
    except AttributeError:
        message = "imposible de faire l'action de reculer d'une frame \n si auqu'un simulation n'a ete faite prealablement"
        affiche_erreur(message)
    except ex.MyError as e:
        affiche_erreur(e)
    else:
        enleve_erreur()


def mettre_pause():
    global pause
    pause = True


def mettre_continu():
    global pause
    pause = False


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
    command=retour_initial,
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
    command=recule_un,
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
    command=avance_un,
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
    command=demar_fin,
)


bouton = tk.Button(
    fenetre,
    text=f"Lancer la ball a {vitesse.get()} m/s a {angle.get()} degree",
    command=deplacement_ball_initiation_erreur_texte,
)
erreur_fram = tk.Label(fenetre, text="")


canvas = tk.Canvas(
    fenetre,
    width=main.cfg["LONGEUR"],
    height=main.cfg["HAUTEUR"],
    bg="#4E4E4E",
)
canvas.place(x=0, y=0, width=main.cfg["LONGEUR"], height=main.cfg["HAUTEUR"])

canvas.create_rectangle(
    (main.cfg["BORDURE"], main.cfg["BORDURE"]),
    (
        (main.cfg["LONGEUR"] - main.cfg["BORDURE"]),
        (main.cfg["HAUTEUR"] - main.cfg["BORDURE"]),
    ),
    fill="green",
)

for cerlce in main.TROU:
    canvas.create_oval(*cerlce, fill="black")

"""
save numero deux des position pour casser le jeux
j'ai juste vraiement pas envie de refaire sa sa ma pris du temps pour rien"""
for ball in ensemble_balls:
    #     if ball == "white":
    #         INITIAL_POSITION_x = 100
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2
    #     elif ball == "red":
    #         INITIAL_POSITION_x = 3 * main.cfg["LONGEUR"] / 5 - 1
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2
    #     elif ball == "purple":
    #         INITIAL_POSITION_x = (3 * main.cfg["LONGEUR"] / 5) + (main.cfg["RAYON"]) * 1.7
    #         INITIAL_POSITION_y = (main.cfg["HAUTEUR"] / 2) + (main.cfg["RAYON"]) * 1
    #     elif ball == "blue":
    #         INITIAL_POSITION_x = (3 * main.cfg["LONGEUR"] / 5) + main.cfg["RAYON"] * 1.7
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2 - main.cfg["RAYON"] * 1
    #     elif ball == "black":
    #         INITIAL_POSITION_x = (3 * main.cfg["LONGEUR"] / 5) + main.cfg[
    #             "RAYON"
    #         ] * 1.7 * 2.1
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2
    #     elif ball == "yellow":
    #         INITIAL_POSITION_x = (3 * main.cfg["LONGEUR"] / 5) + main.cfg[
    #             "RAYON"
    #         ] * 1.7 * 2.1
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2 - main.cfg["RAYON"] * 2
    #     elif ball == "violet":
    #         INITIAL_POSITION_x = (3 * main.cfg["LONGEUR"] / 5) + main.cfg[
    #             "RAYON"
    #         ] * 1.7 * 2.1
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2 + main.cfg["RAYON"] * 2
    #     elif ball == "orange":
    #         INITIAL_POSITION_x = (3 * main.cfg["LONGEUR"] / 5) + main.cfg[
    #             "RAYON"
    #         ] * 1.7 * 3.15
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2 - main.cfg["RAYON"] * 1
    #     elif ball == "teal":
    #         INITIAL_POSITION_x = (3 * main.cfg["LONGEUR"] / 5) + main.cfg[
    #             "RAYON"
    #         ] * 1.7 * 3.15
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2 + main.cfg["RAYON"] * 1
    #     elif ball == "indianred4":
    #         INITIAL_POSITION_x = (3 * main.cfg["LONGEUR"] / 5) + main.cfg[
    #             "RAYON"
    #         ] * 1.7 * 3.15
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2 - main.cfg["RAYON"] * 2 * 1.5
    #     elif ball == "midnightblue":
    #         INITIAL_POSITION_x = (3 * main.cfg["LONGEUR"] / 5) + main.cfg[
    #             "RAYON"
    #         ] * 1.7 * 3.15
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2 + main.cfg["RAYON"] * 2 * 1.5

    #     elif ball == "darkgreen":
    #         INITIAL_POSITION_x = (3 * main.cfg["LONGEUR"] / 5) + main.cfg[
    #             "RAYON"
    #         ] * 1.7 * 4.2
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2

    #     elif ball =="maroon":
    #         INITIAL_POSITION_x = (3 * main.cfg["LONGEUR"] / 5) + main.cfg[
    #             "RAYON"
    #         ] * 1.7 * 4.2
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2 - main.cfg["RAYON"] * 2
    #     elif ball == "tan":
    #         INITIAL_POSITION_x = (3 * main.cfg["LONGEUR"] / 5) + main.cfg[
    #             "RAYON"
    #         ] * 1.7 * 4.2
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2 +main.cfg["RAYON"] * 4
    #     elif ball == "indigo":
    #         INITIAL_POSITION_x = (3 * main.cfg["LONGEUR"] / 5) + main.cfg[
    #             "RAYON"
    #         ] * 1.7 * 4.2
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2 -main.cfg["RAYON"] * 4
    #     elif ball =="olive":
    #         INITIAL_POSITION_x = (3 * main.cfg["LONGEUR"] / 5) + main.cfg["RAYON"] * 1.7 * 4.2
    #         INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2 + main.cfg["RAYON"] * 2

    if ball == "white":
        INITIAL_POSITION_x = 100
        INITIAL_POSITION_y = main.cfg["HAUTEUR"] / 2
    else:
        INITIAL_POSITION_x = random.randint(
            int(main.cfg["LONGEUR"] / 2) - main.cfg["BORDURE"] * 2,
            main.cfg["LONGEUR"] - main.cfg["BORDURE"] * 2,
        )
        INITIAL_POSITION_y = random.randint(
            main.cfg["BORDURE"] * 2, main.cfg["HAUTEUR"] - (main.cfg["BORDURE"] * 2)
        )

    dic_and_ball[ball] = canvas.create_oval(
        (
            (INITIAL_POSITION_x, INITIAL_POSITION_y),
            (
                INITIAL_POSITION_x + 2 * main.cfg["RAYON"],
                INITIAL_POSITION_y + 2 * main.cfg["RAYON"],
            ),
        ),
        fill=ensemble_balls[ball].color,
    )
    ensemble_balls[ball].set_position(
        (
            INITIAL_POSITION_x,
            INITIAL_POSITION_y,
            INITIAL_POSITION_x + 2 * main.cfg["RAYON"],
            INITIAL_POSITION_y + 2 * main.cfg["RAYON"],
        )
    )
    ensemble_balls[ball].set_canva(dic_and_ball[ball])


bouton.place(x=10, y=main.cfg["HAUTEUR"] + 150, width=200, height=30)
erreur_fram.place(x=main.cfg["LONGEUR"] + 25, y=10, width=300, height=100)
angel_text.place(x=45, y=main.cfg["HAUTEUR"] + 115, width=40, height=20)
angle.place(x=32, y=main.cfg["HAUTEUR"] + 15, width=50, height=100)

vitesse_text.place(x=109, y=main.cfg["HAUTEUR"] + 115, width=40, height=20)
vitesse.place(x=102, y=main.cfg["HAUTEUR"] + 15, width=50, height=100)

Frame1.place(x=250, y=main.cfg["HAUTEUR"] + 10, width=500, height=200)


DIMENTION = 50


retour_ini.place(x=0, y=0, width=DIMENTION, height=DIMENTION)
retour_moin_un.place(x=DIMENTION, y=0, width=DIMENTION, height=DIMENTION)
# pause.place(x=2 * DIMENTION, y=0, width=DIMENTION, height=DIMENTION)
# continu.place(x=3 * DIMENTION, y=DIMENTION, width=DIMENTION, height=DIMENTION)
avant_un.place(x=3 * DIMENTION, y=0, width=DIMENTION, height=DIMENTION)
fin_sim.place(x=4 * DIMENTION, y=0, width=DIMENTION, height=DIMENTION)

tk.Button(
    Frame1,
    text="Ouvrir",
    command=lambda: fich_con.lire_json(fenetre, canvas, dic_and_ball, ensemble_balls),
).place(x=DIMENTION * 7, y=0, width=DIMENTION * 2, height=DIMENTION)
tk.Button(Frame1, text="Sauvegarder", command=fich_con.sauvegarder).place(
    x=DIMENTION * 7, y=DIMENTION, width=DIMENTION * 2, height=DIMENTION
)

keyboard.add_hotkey("esc", fonction_quit)
keyboard.add_hotkey("Alt+f+4", DLC)

keyboard.add_hotkey("enter", deplacement_ball_initiation_erreur_texte)


def affiche_erreur(texte_affiche):
    erreur_fram.config(text=texte_affiche)


def enleve_erreur():
    erreur_fram.config(text="")


if __name__ == "__main__":
    fenetre.mainloop()
