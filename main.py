from flask import Flask, render_template  # Importa las funciones necesarias de Flask
import os  # Importa el módulo os para manejar variables de entorno

app = Flask(__name__)  # Crea una instancia de la aplicación Flask

@app.route('/')
def index():
    # Historia de Nintendo que se mostrará en la página
    nintendo_history = """
    Nintendo Co., Ltd. es una empresa multinacional japonesa de electrónica de consumo y videojuegos con sede en Kioto. 
    Nintendo fue fundada el 23 de septiembre de 1889 por Fusajiro Yamauchi y comenzó como una empresa que producía naipes japoneses.
    Con el tiempo, Nintendo se transformó en una de las compañías más influyentes en la industria de los videojuegos.
    """

    # Lista de los 6 juegos más vendidos con su título, ventas, resumen y nombre de archivo de imagen
    top_games = [
        {"title": "Mario Kart 8 Deluxe", "sales": "33.41 million", "summary": "Juego de carreras de la serie Mario Kart.", "image": "mario_kart_8_deluxe.jpg"},
        {"title": "Animal Crossing: New Horizons", "sales": "31.18 million", "summary": "Simulación de vida en una isla desierta.", "image": "animal_crossing_new_horizons.jpg"},
        {"title": "Super Smash Bros. Ultimate", "sales": "24.77 million", "summary": "Juego de lucha con personajes de Nintendo.", "image": "super_smash_bros_ultimate.jpg"},
        {"title": "The Legend of Zelda: Breath of the Wild", "sales": "23.20 million", "summary": "Aventura en el mundo abierto de Hyrule.", "image": "zelda_breath_of_the_wild.jpg"},
        {"title": "Pokémon Sword and Shield", "sales": "21.85 million", "summary": "Juego RPG de la serie Pokémon.", "image": "pokemon_sword_shield.jpg"},
        {"title": "Super Mario Odyssey", "sales": "21.40 million", "summary": "Aventura de plataformas con Mario.", "image": "super_mario_odyssey.jpg"},
    ]
    # Renderiza la plantilla HTML y pasa las variables history y games a la plantilla
    return render_template('index.html', history=nintendo_history, games=top_games)

if __name__ == '__main__':
    # Ejecuta la aplicación en modo debug en el puerto especificado
    app.run(debug=True, port=os.getenv("PORT", default=5000))
