from PIL import Image
from Model.persons_enum import EnumPerson
import os

list_ph = []


def parse(target):
    X = []
    Y = []

    dir_name = EnumPerson

    def rec_path(path):
        if os.path.basename(path) != "origin":
            global dir_name
            if os.path.isdir(path):
                lst_dir = os.listdir(path)
                if os.path.basename(path) == "johny_depp":
                    dir_name = EnumPerson.Johny_Depp
                elif os.path.basename(path) == "scarlett_johansson":
                    dir_name = EnumPerson.Scarlett_Johansson
                elif os.path.basename(path) == "bill_gates":
                    dir_name = EnumPerson.Bill_Gates
                elif os.path.basename(path) == "billie_eilish":
                    dir_name = EnumPerson.Billie_Eilish
                elif os.path.basename(path) == "vladymyr_zelenskiy":
                    dir_name = EnumPerson.Vladymyr_Zelenskiy
                elif os.path.basename(path) == "angela_merkel":
                    dir_name = EnumPerson.Angela_Merkel

                for elem in lst_dir:
                    rec_path(path + "/" + elem)
            else:
                im = Image.open(path)
                imageSizeW, imageSizeH = im.size
                pixel = []
                for i in range(0, imageSizeW):
                    for j in range(0, imageSizeH):
                        pixel.append(im.getpixel((i, j)))
                x_row = []

                for i in range(0, len(pixel)):
                    x_row.append(pixel[i][0] / 256.0)

                if len(x_row) == 10000:
                    global list_ph
                    X.append(x_row)
                    Y.append(dir_name.value)
                    list_ph.append(path)

    rec_path('../Base/' + target)

    return X, Y, list_ph