from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    nintendo_history = """
    Nintendo Co., Ltd. es una empresa multinacional japonesa de electrónica de consumo y videojuegos con sede en Kioto. 
    Nintendo fue fundada el 23 de septiembre de 1889 por Fusajiro Yamauchi y comenzó como una empresa que producía naipes japoneses.
    Con el tiempo, Nintendo se transformó en una de las compañías más influyentes en la industria de los videojuegos.
    """

    top_games = [
        {"title": "Mario Kart 8 Deluxe", "sales": "33.41 million"},
        {"title": "Animal Crossing: New Horizons", "sales": "31.18 million"},
        {"title": "Super Smash Bros. Ultimate", "sales": "24.77 million"},
        {"title": "The Legend of Zelda: Breath of the Wild", "sales": "23.20 million"},
        {"title": "Pokémon Sword and Shield", "sales": "21.85 million"},
        {"title": "Super Mario Odyssey", "sales": "21.40 million"},
        {"title": "Pokémon Let's Go, Pikachu! and Let's Go, Eevee!", "sales": "13.57 million"},
        {"title": "Splatoon 2", "sales": "12.45 million"},
        {"title": "Ring Fit Adventure", "sales": "10.11 million"},
        {"title": "New Super Mario Bros. U Deluxe", "sales": "10.44 million"},
    ]
    return render_template('index.html', history=nintendo_history, games=top_games)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
