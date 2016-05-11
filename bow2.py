# !/usr/bin/env python
# encoding: utf-8

"""
BOW 2016 family practice version 2
Created by Andre Moncrieff and Marco Rego on 13 April 2016.
Copyright 2016. All rights reserved.
Everything that is snazzy about this version was created by Marco.
"""

import sys
import random
from colorama import init, AnsiToWin32, Fore, Style, deinit


family_number_dict = {"Struthionidae": 2,
                      "Casuariidae": 3,
                      "Dromaiidae": 1,
                      "Apterygidae": 5,
                      "Rheidae": 2,
                      "Tinamidae": 47,
                      "Spheniscidae": 16,
                      "Diomedeidae": 13,
                      "Procellariidae": 84,
                      "Pelecanoididae": 4,
                      "Hydrobatidae": 21,
                      "Gaviidae": 5,
                      "Podicipedidae": 25,
                      "Phoenicopteridae": 6,
                      "Phaethontidae": 3,
                      "Sulidae": 10,
                      "Phalacrocoracidae": 31,
                      "Anhingidae": 4,
                      "Fregatidae": 5,
                      "Pelecanidae": 8,
                      "Balaenicipitidae": 1,
                      "Scopidae": 1,
                      "Ciconiidae": 19,
                      "Ardeidae": 63,
                      "Threskiornithidae": 34,
                      "Anhimidae": 3,
                      "Anseranatidae": 1,
                      "Anatidae": 160,
                      "Cathartidae": 7,
                      "Sagittariidae": 1,
                      "Pandionidae": 1,
                      "Accipitridae": 240,
                      "Falconidae": 65,
                      "Megapodiidae": 22,
                      "Cracidae": 54,
                      "Odontophoridae": 33, #  bonus
                      "Tetraonidae": 19,
                      "Meleagrididae": 2,
                      "Phasianidae": 179,
                      "Numididae": 6,
                      "Opisthocomidae": 1,
                      "Gruidae": 15,
                      "Aramidae": 1,
                      "Psophiidae": 3,
                      "Rallidae": 149,
                      "Sarothruridae": 9, #  bonus
                      "Heliornithidae": 3,
                      "Otididae": 26,
                      "Rhynochetidae": 1,
                      "Eurypygidae": 1,
                      "Cariamidae": 2,
                      "Mesitornithidae": 3,
                      "Jacanidae": 8,
                      "Rostratulidae": 3,
                      "Haematopodidae": 13,
                      "Ibidorhynchidae": 1,
                      "Recurvirostridae": 10,
                      "Charadriidae": 67,
                      "Pluvianidae": 1,
                      "Burhinidae": 9,
                      "Glareolidae": 17,
                      "Scolopacidae": 94,
                      "Thinocoridae": 4,
                      "Pedionomidae": 1,
                      "Pluvianellidae": 1,
                      "Chionidae": 2,
                      "Dromadidae": 1,
                      "Stercorariidae": 7,
                      "Laridae": 99,
                      "Rynchopidae": 3,
                      "Alcidae": 26,
                      "Turnicidae": 17,
                      "Pteroclidae": 16,
                      "Columbidae": 313,
                      "Strigopidae": 4,
                      "Cacatuidae": 21,
                      "Psittaculidae": 184, # bonus
                      "Psittacidae": 167,
                      "Musophagidae": 23,
                      "Cuculidae": 140,
                      "Tytonidae": 19,
                      "Strigidae": 194,
                      "Caprimulgidae": 92,
                      "Steatornithidae": 1,
                      "Podargidae": 13,
                      "Nyctibiidae": 7,
                      "Aegothelidae": 11,
                      "Apodidae": 95,
                      "Hemiprocnidae": 4,
                      "Trochilidae": 338,
                      "Coliidae": 6,
                      "Trogonidae": 44,
                      "Alcedinidae": 91,
                      "Todidae": 5,
                      "Momotidae": 13,
                      "Meropidae": 27,
                      "Coraciidae": 12,
                      "Brachypteraciidae": 5, #  bonus
                      "Leptosomidae": 1,
                      "Upupidae": 1,
                      "Phoeniculidae": 8,
                      "Bucerotidae": 53,
                      "Galbulidae": 18,
                      "Bucconidae": 35,
                      "Indicatoridae": 16,
                      "Lybiidae": 42,
                      "Megalaimidae": 25,
                      "Capitonidae": 18,
                      "Semnornithidae": 2,
                      "Ramphastidae": 40,
                      "Picidae": 217,
                      "Acanthisittidae": 4,
                      "Eurylaimidae": 8,
                      "Philepittidae": 4,
                      "Calyptomenidae": 6,
                      "Sapayoidae": 1,
                      "Scleruridae": 17,
                      "Dendrocolaptidae": 51,
                      "Furnariidae": 296,
                      "Thamnophilidae": 232,
                      "Formicariidae": 12,
                      "Grallariidae": 53,
                      "Conopophagidae": 10,
                      "Rhinocryptidae": 57,
                      "Melanopareidae": 4,
                      "Cotingidae": 65, #  bonus
                      "Oxyruncidae": 1,
                      "Pipridae": 48,
                      "Tyrannidae": 419,
                      "Tityridae": 35, #  bonus
                      "Pipritidae": 3, #  bonus
                      "Pittidae": 29,
                      "Menuridae": 2,
                      "Atrichornithidae": 2,
                      "Alaudidae": 93,
                      "Hirundinidae": 84,
                      "Campephagidae": 85,
                      "Pycnonotidae": 130,
                      "Nicatoridae": 3,
                      "Maluridae": 32, #  bonus
                      "Acanthizidae": 59, #  bonus
                      "Psophodidae": 5,
                      "Mohouidae": 3, #  bonus
                      "Neosittidae": 3,
                      "Cinclosomatidae": 10, #  bonus
                      "Orthonychidae": 3,
                      "Pomatostomidae": 5, #  bonus
                      "Pachycephalidae": 49,
                      "Falcunculidae": 3,
                      "Oreoicidae": 3, #  not at LSU
                      "Eulacestomatidae": 1, #  not at LSU
                      "Paramythiidae": 2, #  not at LSU
                      "Melanocharitidae": 10, #  not at LSU
                      "Cnemophilidae": 3, #  not at LSU
                      "Pardalotidae": 4,
                      "Meliphagidae": 178,
                      "Petroicidae": 49,
                      "Aegithinidae": 4, #  bonus
                      "Hyliotidae": 3, #  bonus
                      "Panuridae": 1,
                      "Laniidae": 34,
                      "Malacanotidae": 46,
                      "Vangidae": 36, #  bonus
                      "Machaerirhynchidae": 2, #  not at LSU
                      "Elachuridae": 1, #  not at LSU
                      "Dulidae": 1,
                      "Bombycillidae": 3,
                      "Hypocoliidae": 1,
                      "Ptilogonatidae": 4,
                      "Mohoidae": 5, #  not at LSU
                      "Cinclidae": 5,
                      "Troglodytidae": 82,
                      "Polioptilidae": 15,
                      "Buphagidae": 2,
                      "Mimidae": 34,
                      "Sturnidae": 114,
                      "Rhabdornithidae": 3,
                      "Turdidae": 159,
                      "Timaliidae": 46, #  bonus
                      "Pellorneidae": 54, #  bonus
                      "Leiothrichidae": 125, #  bonus
                      "Picathartidae": 2,
                      "Eupetidae": 1, #  not at LSU
                      "Chaetopidae": 2, #  not at LSU
                      "Sylviidae": 62, #  bonus
                      "Donacobiidae": 1,
                      "Macrosphenidae": 18, #  bonus
                      "Locustellidae": 57,
                      "Cisticolidae": 139,
                      "Bernieridae": 11, #  not at LSU
                      "Acrocephalidae": 59, #  bonus
                      "Phylloscopidae": 77, #  bonus
                      "Scotocercidae": 37, #  bonus
                      "Pnoepygidae": 4, #  not at LSU
                      "Regulidae": 6,
                      "Stenostiridae": 9, #  bonus
                      "Muscicapidae": 303, #  bonus
                      "Platysteiridae": 29,
                      "Monarchidae": 96, #  bonus
                      "Rhipiduridae": 46,
                      "Melampittidae": 2, #  not at LSU
                      "Ifritidae": 1, #  not at LSU
                      "Aegithalidae": 10,
                      "Remizidae": 10, #  bonus
                      "Paridae": 59,
                      "Sittidae": 28,
                      "Certhiidae": 9,
                      "Urocynchramidae": 1, # not at LSU
                      "Promeropidae": 5, #  not at LSU
                      "Modulatricidae": 3, #  bonus
                      "Nectariniidae": 136,
                      "Dicaeidae": 45,
                      "Zosteropidae": 122,
                      "Irenidae": 2,
                      "Chloropseidae": 11,  #  bonus
                      "Oriolidae": 35,
                      "Rhagologidae": 1, #  not at LSU
                      "Dicruridae": 22,
                      "Callaeidae": 4,
                      "Notiomystidae": 1, #  not at LSU
                      "Peltopsidae": 2, #  not at LSU
                      "Artamidae": 11,
                      "Cracticidae": 11,
                      "Corcoracidae": 2,
                      "Pityriaseidae": 1, #  not at LSU
                      "Climacteridae": 7,
                      "Ptilonorhynchidae": 19,
                      "Paradisaeidae": 41,
                      "Platylophidae": 1,
                      "Corvidae": 125,
                      "Vireonidae": 62,
                      "Prunellidae": 12,
                      "Motacillidae": 67,
                      "Calcariidae": 6,
                      "Zeledonidae": 1,
                      "Emberizidae": 168, #  bonus
                      "Cardinalidae": 63, #  bonus
                      "Thraupidae": 371, #  bonus
                      "Parulidae": 108,
                      "Peucedramidae": 1,
                      "Icteridae": 105,
                      "Fringillidae": 221,
                      "Estrildidae": 131,
                      "Viduidae": 20,
                      "Passeridae": 38,
                      "Ploceidae": 115
                      }

def number_quiz(stream, rights=[], wrong_f=[]):
    if len(family_number_dict) > 0:
        family = random.choice(list(family_number_dict.keys()))
        answer = input("How many species in {}? ".format(family))
        if answer == "":
            summ = sum(rights)
            return summ, wrong_f
        elif answer in "abcdefghijklmnopqrstuvxwyz.-*/+?!@#$%&()":
            print(Fore.BLUE+"\nOnly integers are valid answers!\n"+Style.RESET_ALL, file=stream)
            number_quiz(stream)
        elif int(answer) != family_number_dict[family]:
            if family_number_dict[family] == 1:
                print(Fore.RED+"\nMonotipic family. There is no buffer\n"+Style.RESET_ALL, file=stream)
                wrong_f.append(family)
                family_number_dict.pop(family)
                rights.append(0)
                number_quiz(stream)
            elif family_number_dict[family] != 1:
                if int(answer) in range(family_number_dict[family]-5,
                                        family_number_dict[family]+5):
                    print(Fore.YELLOW+"\nYou are close!"+Style.RESET_ALL, file=stream)
                    print("The correct is: {}\n".format
                          (family_number_dict[family]))
                    wrong_f.append(family)
                    family_number_dict.pop(family)
                    rights.append(0)
                    number_quiz(stream)
                else:
                    print(Fore.RED+"\nWRONG ANSWER!"+Style.RESET_ALL, file=stream)
                    print("The correct answer is: {}\n".format
                          (family_number_dict[family]))
                    wrong_f.append(family)
                    family_number_dict.pop(family)
                    rights.append(0)
                    number_quiz(stream)
        elif int(answer) == family_number_dict[family]:
            print(Fore.GREEN+"\nYou're correct!\n"+Style.RESET_ALL, file=stream)
            family_number_dict.pop(family)
            #print("Families left in quiz: {}\n".format(len(family_number_dict)))
            rights.append(1)
            number_quiz(stream)
        summ = sum(rights)
        return summ, wrong_f
    else:
        summ = sum(rights)
        return summ, wrong_f


def statistcs(r, w):
    print("\nCongratulations! You finished the quiz.\n")
    print("Your Scores:")
    print("Based on the total number of families: {:04.2f}%"
          .format((100*r)/245))
    print("Based on where the quiz stopped: {:04.2f}%"
          .format((100*r)/(r+len(w))))
    print("You got {} families right and {} families wrong".format(r, len(w)))
    print("Families you got wrong:\n{}".format(w))


def main():
    init(wrap=False)
    stream = AnsiToWin32(sys.stderr).stream
    r, wrong_f = number_quiz(stream)
    statistcs(r, wrong_f)
    deinit()

if __name__ == '__main__':
    main()
