import numpy as np
import os

hair = np.genfromtxt("hairout.txt", dtype=str)


for i in  hair :
    try :
        os.replace("archive/img_align_celeba/img_align_celeba/" + i, "hairpics/" + i)
    except FileNotFoundError:
        print("miss")
        continue