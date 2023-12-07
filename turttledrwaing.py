import turtle

def dibujar_letra(letra, color):
    turtle.color(color)
    turtle.write(letra, font=("Arial", 50, "normal"))
    turtle.forward(30)  # Espacio entre letras

def dibujar_palabra(palabra, color):
    for letra in palabra:
        dibujar_letra(letra, color)

def dibujarcorazon():
    t = turtle.Turtle()
   
    # Dibujar el corazón
    t.begin_fill()
    t.color('red')
    t.left(45)
    t.forward(100)
    t.circle(50, 180)
    t.right(90)
    t.circle(50, 180)
    t.forward(100)
    t.end_fill()
   

def main():
    turtle.speed(1)  # Velocidad baja
    turtle.penup()
    turtle.goto(-300, 200)  # Posición inicial

    palabra = "internet"
    color = "red"
    dibujarcorazon()
    dibujar_palabra(palabra, color)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
