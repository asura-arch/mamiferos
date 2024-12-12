# animalplanet.py
# app.py

class Mamifero:
    def caminar(self):
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    def nadar(self):
        raise NotImplementedError("Este método debe ser implementado por subclases.")


class Perro(Mamifero):
    def caminar(self):
        return "El perro camina."

    def nadar(self):
        return "El perro nada."


class Ballena(Mamifero):
    def caminar(self):
        return "La ballena no camina."

    def nadar(self):
        return "La ballena nada."

 

import tkinter as tk
from mamifero import Perro, Ballena

def mostrar_accion(mamifero, accion):
    if accion == "caminar":
        resultado = mamifero.caminar()
    else:
        resultado = mamifero.nadar()
    
    resultado_label.config(text=resultado)

def ejecutar_perro():
    perro = Perro()
    mostrar_accion(perro, accion_var.get())

def ejecutar_ballena():
    ballena = Ballena()
    mostrar_accion(ballena, accion_var.get())

# Configuración de la ventana principal
root = tk.Tk()
root.title("Mamíferos")

accion_var = tk.StringVar(value="caminar")

tk.Label(root, text="Selecciona un mamífero:").pack()

perro_button = tk.Button(root, text="Perro", command=ejecutar_perro)
perro_button.pack()

ballena_button = tk.Button(root, text="Ballena", command=ejecutar_ballena)
ballena_button.pack()

tk.Radiobutton(root, text="Caminar", variable=accion_var, value="caminar").pack()
tk.Radiobutton(root, text="Nadar", variable=accion_var, value="nadar").pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

root.mainloop()
