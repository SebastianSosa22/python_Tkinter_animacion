import tkinter as tk
import random

# Crear la ventana principal
root = tk.Tk()
root.title("Animación Avanzada con Tkinter")

# Crear el lienzo donde se dibujará la animación
canvas = tk.Canvas(root, width=800, height=600, bg='white')
canvas.pack()

# Crear una lista para almacenar las bolas
balls = []

# Función para crear bolas
def create_ball():
    size = random.randint(20, 50)
    x = random.randint(size, 800 - size)
    y = random.randint(size, 600 - size)
    dx = random.choice([-3, -2, -1, 1, 2, 3])
    dy = random.choice([-3, -2, -1, 1, 2, 3])
    color = random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'orange'])
    ball = canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)
    balls.append((ball, dx, dy))

# Crear varias bolas
for _ in range(10):
    create_ball()

# Función para mover las bolas
def move_balls():
    for i, (ball, dx, dy) in enumerate(balls):
        canvas.move(ball, dx, dy)
        pos = canvas.coords(ball)
        if pos[2] >= 800 or pos[0] <= 0:
            dx = -dx
        if pos[3] >= 600 or pos[1] <= 0:
            dy = -dy
        balls[i] = (ball, dx, dy)
    root.after(20, move_balls)

# Iniciar la animación
move_balls()

# Iniciar el bucle principal de Tkinter
root.mainloop()
