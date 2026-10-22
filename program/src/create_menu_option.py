import tkinter as tk
from collections.abc import Callable

def create_menu_option(
    canvas: tk.Canvas,
    height: int,
    text: str,
    operation: Callable[[], None],
    on_complete: Callable[[], None] | None = None
):
    def handle_click(_event: tk.Event) -> None:
        operation()
        if on_complete is not None:
            on_complete()

    text_id = canvas.create_text(
        180,
        height,
        text=text,
        font=("Artifakt Element", 11, "bold"),
        fill="white"
    )

    canvas.tag_bind(
        text_id,
        "<Button-1>",
        handle_click
    )

    canvas.tag_bind(
        text_id,
        "<Enter>",
        lambda event: canvas.itemconfig(
            text_id,
            fill="#90E0EF"
        )
    )

    canvas.tag_bind(
        text_id,
        "<Leave>",
        lambda event: canvas.itemconfig(
            text_id,
            fill="white"
        )
    )