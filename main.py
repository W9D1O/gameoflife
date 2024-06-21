from raylibpy import *
import copy
pixel = 20
dimen = 25


def init_m():
    tab = []
    for i in range(0, dimen):
        tab.append([0])
        tab[i] = [0] * dimen
    return tab


def mouse(tab):
    Mposi = get_mouse_position()
    if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
        x = int(Mposi.x) // pixel
        y = int(Mposi.y) // pixel
        tab[y][x] = 1
    elif is_mouse_button_pressed(MOUSE_BUTTON_RIGHT):
        x = int(Mposi.x) // pixel
        y = int(Mposi.y) // pixel
        tab[y][x] = 0
    elif is_mouse_button_down(MOUSE_BUTTON_LEFT):
        x = int(Mposi.x) // pixel
        y = int(Mposi.y) // pixel
        tab[y][x] = 1


def vecinos(tab, y, x):

    vec = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            vec = vec + tab[(y + i) % dimen][(x + j) % dimen]

    vec -= tab[y][x]
    return vec


def act_tab(tab):
    act = copy.deepcopy(tab)
    for i in range(dimen):
        for j in range(dimen):
            veci = vecinos(tab, i, j)

            if tab[i][j] == 1 and (veci < 2 or veci > 3):
                act[i][j] = 0

            elif (tab[i][j] == 0 and veci == 3):
                act[i][j] = 1
    return act


def colorear(tab):
    for i in range(dimen):
        for j in range(dimen):

            mouse(tab)
            if tab[i][j] == 1:
                draw_rectangle(j*pixel, i*pixel, pixel *
                               dimen, pixel*dimen, WHITE)
            elif tab[i][j] == 0:
                draw_rectangle(j*pixel, i*pixel, pixel *
                               dimen, pixel*dimen, BLACK)
            draw_rectangle_lines(j*pixel, i*pixel, pixel *
                                 dimen, pixel*dimen, GRAY)


def main():
    tab = init_m()

    ashanca = False

    init_window(pixel * (dimen), pixel*(dimen),
                "Game of life en Raylib Python")
    set_target_fps(60)
    while not window_should_close():
        begin_drawing()
        clear_background(BLACK)
        colorear(tab)

        if is_mouse_button_down(MOUSE_BUTTON_LEFT):
            ashanca = False
        elif is_mouse_button_up(MOUSE_BUTTON_LEFT):
            ashanca = True
        elif is_key_buttom_pressed(KEY_SPACE):
            ashanca = False
        if ashanca:
            tab = act_tab(tab)
        end_drawing()
    close_window()


if __name__ == "__main__":
    main()
