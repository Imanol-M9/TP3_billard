import subprocess
import os

COOEFICIENT = 4
HAUTEUR = 122 * COOEFICIENT
LONGEUR = 214 * COOEFICIENT
BORDURE = 10 * COOEFICIENT
RAYON = 2.5 * COOEFICIENT
PAT = 20
FROTEMENT = 0.3
EPSILON = 0.05

TROU = (
    (
        ((LONGEUR // 2 - 2 * RAYON), (BORDURE - 2 * RAYON)),
        ((LONGEUR // 2 + 2 * RAYON), (BORDURE + 2 * RAYON)),
    ),
    (
        (
            (LONGEUR // 2 - 2 * RAYON),
            (HAUTEUR - BORDURE - 2 * RAYON),
        ),
        (
            (LONGEUR // 2 + 2 * RAYON),
            (HAUTEUR - BORDURE + 2 * RAYON),
        ),
    ),
    (
        ((BORDURE - 2 * RAYON), (BORDURE - 2 * RAYON)),
        ((BORDURE + 2 * RAYON), (BORDURE + 2 * RAYON)),
    ),
    (
        ((LONGEUR - BORDURE - 2 * RAYON), (HAUTEUR - BORDURE - 2 * RAYON)),
        ((LONGEUR - BORDURE + 2 * RAYON), (HAUTEUR - BORDURE + 2 * RAYON)),
    ),
    (
        ((LONGEUR - BORDURE - 2 * RAYON), (BORDURE - 2 * RAYON)),
        ((LONGEUR - BORDURE + 2 * RAYON), (BORDURE + 2 * RAYON)),
    ),
    (
        ((BORDURE - 2 * RAYON), (HAUTEUR - BORDURE - 2 * RAYON)),
        ((BORDURE + 2 * RAYON), (HAUTEUR - BORDURE + 2 * RAYON)),
    ),
)
# # exec(open("./interface.py").read())
# # subprocess.run(["python", "interface.py"])
# os.system("python test.py")