from src.data_service import get_layer

def update_menu(canvas):
    canvas.delete("layer_status")

    if get_layer() is not None:
        canvas.create_text(
            180,
            340,
            text="PLIK ZAŁADOWANY PRAWIDŁOWO",
            fill="#53FF30",
            tags="layer_status"
        )