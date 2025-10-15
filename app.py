import os
import random
from flask import Flask, jsonify


NAMES = [
    "Alessandro", "Giulia", "Marco", "Francesca", "Luca", "Anna", "Andrea", "Sara", "Matteo", "Elena",
    "Davide", "Chiara", "Francesco", "Martina", "Simone", "Valentina", "Federico", "Alessia", "Roberto", "Silvia",
    "Giovanni", "Federica", "Antonio", "Giorgia", "Michele", "Claudia", "Stefano", "Serena", "Riccardo", "Elisa",
    "Fabio", "Beatrice", "Emanuele", "Cristina", "Nicola", "Roberta", "Daniele", "Paola", "Giuseppe", "Michela",
    "Tommaso", "Camilla", "Lorenzo", "Arianna", "Paolo", "Valeria", "Alberto", "Monica", "Filippo", "Manuela",
    "Vincenzo", "Ilaria", "Gabriele", "Lucia", "Massimo", "Veronica", "Alessandro", "Barbara", "Enrico", "Sabrina",
    "Claudio", "Antonella", "Mario", "Daniela", "Salvatore", "Emanuela", "Pietro", "Patrizia", "Carlo", "Stefania",
    "Gianluca", "Simona", "Franco", "Raffaella", "Mauro", "Catarina", "Diego", "Rosanna", "Giacomo", "Giovanna",
    "Raffaele", "Teresa", "Angelo", "Elisabetta", "Giancarlo", "Alessandra", "Sergio", "Lorenza", "Bruno", "Carla",
    "Valerio", "Greta", "Leonardo", "Nicole", "Enzo", "Diana", "Gianni", "Vittoria", "Umberto", "Noemi",
    "Cristiano", "Miriam", "Gennaro", "Bianca", "Edoardo", "Caterina", "Gianluca", "Donatella", "Ivano", "Franca",
    "Orlando", "Gemma", "Ernesto", "Loredana", "Hugo", "Nadia", "Ignazio", "Ornella", "Ivan", "Daria",
    "Jacopo", "Ester", "Kevin", "Fiorella", "Mirko", "Grazia", "Morgan", "Iris", "Nathan", "Karina",
    "Oscar", "Luna", "Patrick", "Marta", "Rocco", "Niki", "Samuel", "Olimpia", "Silvio", "Penelope",
    "Tiziano", "Petra", "Urban", "Rebecca", "Walter", "Stella", "Xavier", "Tamara", "Yuri", "Ursula",
    "Zeno", "Wanda", "Adam", "Xenia", "Boris", "Yasmin", "Carlos", "Zara", "Dennis", "Alice",
    "Edgar", "Blanca", "Felix", "Celeste", "George", "Delia", "Henry", "Eva", "Igor", "Flavia",
    "James", "Gioia", "Lucas", "Hilda", "Michael", "Ines", "Nicolas", "Jolanda", "Oliver", "Katia",
    "Peter", "Linda", "Quentin", "Margherita", "Ryan", "Norma", "Sebastian", "Olga", "Thomas", "Priscilla",
    "Victor", "Quinta", "William", "Rosa", "Zachary", "Sonia", "Arthur", "Tina", "Benjamin", "Uberta"
]

def get_random_name():
    return random.choice(NAMES)


application = Flask(__name__)
name = os.getenv("USE_NAME", get_random_name())


@application.route("/")
def hello_world():
    return jsonify({
        "message": f"Hello, World! I'm {name}"
    })