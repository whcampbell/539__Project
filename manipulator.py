import numpy as np
from PIL import Image

bald = np.genfromtxt("baldout.txt", dtype=str)
bald = bald[::6]
hair = np.genfromtxt("hairout.txt", dtype=str)
hair = hair[::6]
big = np.append(bald, hair)
BigCsv = open("SmallerDataBW.csv", "a")
counter = 0


#aight lets dance
for i in big :
    img = Image.open("archive/img_align_celeba/img_align_celeba/" + i)
    bw = img.convert("L")
    data = np.asarray(bw)
    for j in data :
        for k in j :
            BigCsv.write(str(k) + ",")
    if counter < 758 :
        BigCsv.write("1")
    else :
        BigCsv.write("0")
    counter = counter + 1
    BigCsv.write("\n")
    img.close()

