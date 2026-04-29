import tkinter as tk
import keyboard

HAUTEUR = 122
LONGEUR = 214
BORDURE = 14
COOEFICIENT = 4




def fonction_quit():
    fenetre.destroy()
    shunt_yarded.config(text="postfix : erreur")
    resultat.config(text="résultat : erreur")
    erreur_page.config(text="")


fenetre = tk.Tk()
fenetre.title("Le billard rigolo des gigolos")

Bouton = tk.Button(fenetre, text="Calculer", command=None)
equation = tk.Entry(fenetre)
shunt_yarded = tk.Label(fenetre, text="postfix : ")
resultat = tk.Label(fenetre, text="résultat : ")
erreur_page = tk.Label(fenetre, text=" ")
racourti_clav = tk.Label(
    fenetre,
    text="liste racourcise est clavier\n "
    "Escape --> sortire du programe\n "
    "Enter --> effectuer le calcule\n "
    "Ctrl BackSpace  --> vider la console d'entrer",
)

Bouton.grid(row=3, column=5, padx=5, pady=5)
equation.grid(row=1, column=5, padx=5, pady=5)
shunt_yarded.grid(row=4, column=5, padx=5, pady=5)
resultat.grid(row=5, column=5, padx=5, pady=5)
erreur_page.grid(row=6, column=5, padx=5, pady=5)
racourti_clav.grid(row=1, column=6, padx=5, pady=5)


keyboard.add_hotkey("esc", fonction_quit)
keyboard.add_hotkey("enter", None)


fenetre.geometry("800x600")
fenetre.title("Canvas Demo")

trou = ()


canvas = tk.Canvas(
    fenetre,
    width=LONGEUR * COOEFICIENT,
    height=HAUTEUR * COOEFICIENT,
    bg="#4E4E4E",
)
# table = tk.Canvas(
#     fenetre,
#     width=DIMENTION_X_TALBE * COOEFICIENT,
#     height=DIMENTION_y_TALBE * COOEFICIENT,
#     bg="#05A313",
# )
# table.grid(row=0, column=0, padx=0, pady=0)
canvas.grid(row=0, column=0, padx=0, pady=0)

canvas.create_rectangle(
    (BORDURE),
    (BORDURE)
    (555, 444),
    fill="green",
)
for cerlce in trou:
    canvas.create_oval(*cerlce, fill="purple")


fenetre.mainloop()
