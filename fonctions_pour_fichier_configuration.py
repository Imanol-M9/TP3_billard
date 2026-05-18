import tkinter as tk
from tkinter import filedialog, messagebox
import json
import Ball_class as balls

"""
Merci Dassine pour le code
"""


conteneur = {"donnees": {}, "chemin": "current_sim.json", "entrees": {}}


def lire_json(page_simu, canva, dic_ball, ensemble_ball):
    try:
        chemin = filedialog.askopenfilename(filetypes=[("JSON", "*.json")])
        if not chemin:
            return
        with open(chemin, "r", encoding="utf-8") as f:
            conteneur["donnees"] = json.load(f)
        conteneur["chemin"] = chemin
        afficher_donnees(page_simu, canva, dic_ball, ensemble_ball)
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Fichier introuvable.")
    except json.JSONDecodeError:
        messagebox.showerror("Erreur", "JSON invalide.")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))


def afficher_donnees(fenaitre, canva, dic_ball, ensemble_ball):
    for widget in tk.Frame(fenaitre).winfo_children():
        widget.destroy()
    conteneur["entrees"] = {}
    for ball in conteneur["donnees"]:
        canva.coords(dic_ball[ball], conteneur["donnees"][ball])
        ensemble_ball[ball].set_position(conteneur["donnees"][ball])

    for i, (cle, valeur) in enumerate(conteneur["donnees"].items()):
        tk.Label(tk.Frame(fenaitre), text=cle).grid
        var = tk.StringVar(value=str(valeur))
        tk.Entry(tk.Frame(fenaitre), textvariable=var).grid
        conteneur["entrees"][cle] = var


def sauvegarder():
    print(conteneur["donnees"])
    try:
        if not conteneur["chemin"]:
            messagebox.showwarning("Attention", "Aucun fichier ouvert.")
            return None
        for cle, var in conteneur["entrees"].items():
            conteneur["donnees"][cle] = var.get()
        with open(conteneur["chemin"], "r", encoding="utf-8") as f:
            liste_ball = json.load(f)
        for ball in balls.ensemble_balls:
            liste_ball[ball] = balls.ensemble_balls[ball].position
        with open(conteneur["chemin"], "w", encoding="utf-8") as f:
            json.dump(liste_ball, f, indent=4, ensure_ascii=False)
        messagebox.showinfo("Succès", "Fichier sauvegardé !")
    except PermissionError:
        messagebox.showerror("Erreur", "Permission refusée.")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))
