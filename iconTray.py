import pystray
import PIL.Image
from delChat import main

image = PIL.Image.open("skeleton.png")


def on_clicked(icon, item):
    if str(item) == "Del_Chat":
        main()
    elif str(item) == "Exit":
        icon.stop()


icon = pystray.Icon("Kerosine_Sl", image, menu=pystray.Menu(
    pystray.MenuItem("Del_Chat", on_clicked),
    pystray.MenuItem("Exit", on_clicked)
))

if __name__ == '__main__':
    icon.run()

# Add Graceful exit
