import tkinter as tk
from pathlib import Path

def create_window():
    # Utworzenie głównego okna + canvas:

    window = tk.Tk()
    window.title("SNEP")
    window.resizable(False, False)

    canvas = tk.Canvas(
        window,
        width=650,
        height=550,
        highlightthickness=0
    )

    canvas.pack()


    # Grafika tła:

    current_dir = Path(__file__).resolve().parent

    image_path = current_dir / "img" / "snep.png"

    window.background_screen = tk.PhotoImage(file=str(image_path))

    canvas.create_image(
        0,
        0,
        image=window.background_screen,
        anchor="nw"
    )


    # Tytuł programu:
    canvas.create_text(
        80,
        50,
        text="SNEP",
        font=("Artifakt Element", 18, "bold"),
        fill="white"
    )
    # Podtytuł programu:
    canvas.create_text(
        300,
        70,
        text=("Symulator Niezależnych Elementów Przestrzennych"),
        font=("Artifakt Element", 16, "normal"),
        fill="white"
    )


    # Menu:

    canvas.create_text(
        180,
        370,
        text="Wybierz operację:",
        font=("Artifakt Element", 15, "bold"),
        fill="white"
    )

    return (window, canvas)