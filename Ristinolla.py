import tkinter as tk
import tkinter.messagebox
import random

napit = []
vuoro = None
voittaja = None

root = tk.Tk()
root.geometry("300x380")
root.title("Ristinolla")


def luoPelialusta():
    rivi = 0
    sarake = 0
    for i in range(9):
        napit.append(tk.Button(fg="black", bg="white", font="Times", height=6,
                               width=10, text=None, command=paivita_teksti))
    for i in napit:
        i.grid(row=rivi, column=sarake)
        i.config(command=lambda current_nappi=i: paivita_teksti(current_nappi))
        sarake += 1

        if (sarake == 3):
            rivi += 1
            sarake = 0

def arvo_vuoro():
    global vuoro
    aloittaja = random.randint(1, 2)
    if (aloittaja == 1):
        vuoro = ("X")
    elif (aloittaja == 2):
        vuoro = ("O")

def set_vuoro():
    global vuoro
    if (vuoro == "X"):
        vuoro = "O"
    elif (vuoro == "O"):
        vuoro = "X"

def paivita_teksti(current_nappi):  # Set button text to 'X' or 'O' and state as disabled after button has been clicked
    current_nappi.config(text=vuoro, state="disabled")
    set_vuoro()
    onko_voittaja()

def onko_voittaja():

    if (napit[0].cget('text') != "" and napit[1].cget('text') != "" and napit[2].cget('text') != ""):
        if (napit[0].cget('text') == napit[1].cget('text') and napit[1].cget('text') == napit[2].cget('text')):
            game_over()

    if (napit[3].cget('text') != "" and napit[4].cget('text') != "" and napit[5].cget('text') != ""):
        if (napit[3].cget('text') == napit[4].cget('text') and napit[4].cget('text') == napit[5].cget('text')):
            game_over()

    if (napit[6].cget('text') != "" and napit[7].cget('text') != "" and napit[8].cget('text') != ""):
        if (napit[6].cget('text') == napit[7].cget('text') and napit[7].cget('text') == napit[8].cget('text')):
            game_over()

    if (napit[0].cget('text') != "" and napit[3].cget('text') != "" and napit[6].cget('text') != ""):
        if (napit[0].cget('text') == napit[3].cget('text') and napit[3].cget('text') == napit[6].cget('text')):
            game_over()


    if (napit[1].cget('text') != "" and napit[4].cget('text') != "" and napit[7].cget('text') != ""):
        if (napit[1].cget('text') == napit[4].cget('text') and napit[4].cget('text') == napit[7].cget('text')):
            game_over()

    if (napit[2].cget('text') != "" and napit[5].cget('text') != "" and napit[8].cget('text') != ""):
        if (napit[2].cget('text') == napit[5].cget('text') and napit[5].cget('text') == napit[8].cget('text')):
            game_over()

    if (napit[0].cget('text') != "" and napit[4].cget('text') != "" and napit[8].cget('text') != ""):
        if (napit[0].cget('text') == napit[4].cget('text') and napit[4].cget('text') == napit[8].cget('text')):
            game_over()

    if (napit[2].cget('text') != "" and napit[4].cget('text') != "" and napit[6].cget('text') != ""):
        if (napit[2].cget('text') == napit[4].cget('text') and napit[4].cget('text') == napit[6].cget('text')):
            game_over()

def game_over():
    global voittaja
    if vuoro == 'X':
        voittaja = 'O'
    else:
        voittaja = 'X'
    tkinter.messagebox.showinfo("Game over", "Peli päättyi!\nVoittaja on: " + voittaja)
    quit()

def kaynnista_peli():
    luoPelialusta()
    arvo_vuoro()

kaynnista_peli()
root.mainloop()
