import json


with open("fichier_configuration.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)


TROU = (
    (
        ((cfg["LONGEUR"] // 2 - 2 * cfg["RAYON"]), (cfg["BORDURE"] - 2 * cfg["RAYON"])),
        ((cfg["LONGEUR"] // 2 + 2 * cfg["RAYON"]), (cfg["BORDURE"] + 2 * cfg["RAYON"])),
    ),
    (
        (
            (cfg["LONGEUR"] // 2 - 2 * cfg["RAYON"]),
            (cfg["HAUTEUR"] - cfg["BORDURE"] - 2 * cfg["RAYON"]),
        ),
        (
            (cfg["LONGEUR"] // 2 + 2 * cfg["RAYON"]),
            (cfg["HAUTEUR"] - cfg["BORDURE"] + 2 * cfg["RAYON"]),
        ),
    ),
    (
        ((cfg["BORDURE"] - 2 * cfg["RAYON"]), (cfg["BORDURE"] - 2 * cfg["RAYON"])),
        ((cfg["BORDURE"] + 2 * cfg["RAYON"]), (cfg["BORDURE"] + 2 * cfg["RAYON"])),
    ),
    (
        (
            (cfg["LONGEUR"] - cfg["BORDURE"] - 2 * cfg["RAYON"]),
            (cfg["HAUTEUR"] - cfg["BORDURE"] - 2 * cfg["RAYON"]),
        ),
        (
            (cfg["LONGEUR"] - cfg["BORDURE"] + 2 * cfg["RAYON"]),
            (cfg["HAUTEUR"] - cfg["BORDURE"] + 2 * cfg["RAYON"]),
        ),
    ),
    (
        ((cfg["LONGEUR"] - cfg["BORDURE"] - 2 * cfg["RAYON"]), (cfg["BORDURE"] - 2 * cfg["RAYON"])),
        ((cfg["LONGEUR"] - cfg["BORDURE"] + 2 * cfg["RAYON"]), (cfg["BORDURE"] + 2 * cfg["RAYON"])),
    ),
    (
        ((cfg["BORDURE"] - 2 * cfg["RAYON"]), (cfg["HAUTEUR"] - cfg["BORDURE"] - 2 * cfg["RAYON"])),
        ((cfg["BORDURE"] + 2 * cfg["RAYON"]), (cfg["HAUTEUR"] - cfg["BORDURE"] + 2 * cfg["RAYON"])),
    ),
)
# # exec(open("./interface.py").read())
# # subprocess.run(["python", "interface.py"])
# os.system("python test.py")
