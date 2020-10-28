import numpy as np
import matplotlib.pyplot as plt

g = 100
N = 160

pause = True
def iniciar(click):
    global pause
    pause ^= True

#tablero
tablero = np.zeros((N, N), dtype=int)


#celulas de configuracion inicial, esto va a cambiar con el archivo pm2
tablero[1, 5:9] = 1
tablero[2, 4] = 1
tablero[3, 7] = 1


def generar_config_aleatoria(click):
    for i in range(1, N):
        for j in range(1, N):
            tablero[i, j] = random.randint(0, 1)
    global b
    b = tablero
    imagen.set_data(b)


fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
b = tablero
imagen = ax.imshow(b, interpolation="none", aspect="equal", cmap=cm.gray_r)
plt.tick_params(
    axis='x',  #se cambiara el eje x
    which='both',  #ticks
    bottom=False,
    top=False,
    labelbottom=False)  #borde del boton


def animacion(n):
    global b
    if not pause:  #siempre que no haya pausa
        b = paso(b)  #ir cambiando poco a poco la animacion
        imagen.set_data(b)
        print('va')

    return imagen,

def contador_turnos(juego):
    global pause
    i = 0
    while not pause:
        contador = np.array([i])
        i = i + 1

jugar_pausa = fig.add_axes((0.7875, 0.5, 0.12, 0.04), anchor = 'SE')       #x,y,largo, ancho
pause_button = Button(jugar_pausa, 'Jugar/Pausa', hovercolor='0.975')    #se aclara cuando uno se posiciona encima
pause_button.on_clicked(iniciar)

guardar = fig.add_axes((0.8, 0.4, 0.1, 0.04), anchor = 'SW')
random_button = Button(guardar, 'Guardar', hovercolor='0.975')     #se aclara cuando encima
random_button.on_clicked(generar_config_aleatoria)


anim = animation.FuncAnimation(fig, animacion, frames=g, blit=True, interval = 200, repeat = True)

plt.show()
