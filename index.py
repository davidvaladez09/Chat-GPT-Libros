import tkinter as tk
from tensorflow.keras.models import load_model
import numpy as np

# Función para preprocesar la entrada de texto
def preprocess_text(text):
    # Aquí podrías agregar tu propio preprocesamiento, como tokenización, eliminación de stopwords, etc.
    return text

# Función para cargar el modelo de red neuronal
def load_neural_network_model(model_path):
    model = load_model(model_path)  # Carga el modelo pre-entrenado
    return model

# Función para generar una respuesta utilizando el modelo de red neuronal
def generate_response(question, model):
    question = preprocess_text(question)
    # Convertir la pregunta en una secuencia numérica utilizando el mismo preprocesamiento que se utilizó durante el entrenamiento
    # Aquí deberías adaptar este paso según cómo hayas preprocesado tus datos durante el entrenamiento
    question_sequence = np.array([...])  # Transforma la pregunta en una secuencia numérica utilizando tu método de preprocesamiento
    # Realiza la predicción con el modelo
    predicted_answer_sequence = model.predict(question_sequence)
    # Convierte la secuencia predicha en texto
    # Aquí también debes tener un paso inverso que convierta la secuencia numérica en texto
    generated_answer = "..."  # Aquí deberías utilizar tu método para convertir la secuencia numérica en texto
    return generated_answer

# Función para manejar la interacción del usuario
def submit_question():
    question = entry.get()  # Obtiene la pregunta ingresada por el usuario
    answer = generate_response(question, model)  # Genera la respuesta utilizando el modelo
    response.config(text=answer)  # Muestra la respuesta en la interfaz

# Cargar el modelo pre-entrenado
model_path = 'ruta/a/tu/modelo.h5'
model = load_neural_network_model(model_path)

# Crear la interfaz de usuario
window = tk.Tk()
window.title("Chatbot")
frame = tk.Frame(window)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Pregunta:")
label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(frame, width=50)
entry.grid(row=0, column=1)

submit_button = tk.Button(frame, text="Enviar", command=submit_question)
submit_button.grid(row=0, column=2)

response = tk.Label(frame, text="")
response.grid(row=1, column=0, columnspan=3)

window.mainloop()
