import curses
import time
import datetime

def draw_logo(stdscr):
    logo = """
    ██████╗ █████╗ ██╗     ██╗   ██╗███████╗
    ██╔══██╗██╔══██╗██║     ██║   ██║██╔════╝
    ██████╔╝███████║██║     ██║   ██║███████╗
    ██╔═══╝ ██╔══██║██║     ██║   ██║╚════██║
    ██║     ██║  ██║███████╗╚██████╔╝███████║
    ╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝
    """
    # Change la couleur du texte en bleu
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(2, 2, logo)
    stdscr.attroff(curses.color_pair(1))

def draw_datetime(stdscr):
    # Obtient la date et l'heure actuelles
    now = datetime.datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    # Affiche la date et l'heure dans le coin inférieur droit de l'écran
    stdscr.addstr(curses.LINES - 2, curses.COLS - len(dt_string) - 2, dt_string)

def main(stdscr):
    # Initialise les couleurs
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLUE, -1)

    # Efface l'écran et affiche une chaîne de bienvenue
    stdscr.clear()
    stdscr.border()
    draw_logo(stdscr)
    stdscr.addstr(10, 2, "TanoraTech")
    stdscr.addstr(14, 2, "Bienvenue dans mon application !")
    stdscr.refresh()

    # Boucle principale pour traiter les entrées utilisateur
    while True:
        # Affiche la date et l'heure
        draw_datetime(stdscr)

        # Attend une entrée utilisateur
        key = stdscr.getch()

        # Si l'utilisateur appuie sur 'q', quitte l'application
        if key == ord('q'):
            break
        else:
            # Affiche la touche pressée par l'utilisateur
            stdscr.addstr(16, 2, f"Touche pressée : {chr(key)}")
            stdscr.refresh()

# Exécute la fonction principale avec l'interface curses
curses.wrapper(main)
