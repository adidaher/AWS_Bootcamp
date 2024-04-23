import json
import random
import requests

class PokemonApp:
    def __init__(self):
        self.pokemon_data = {}

    def fetch_pokemon_details(self, pokemon_name):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        response = requests.get(url)
        if response.status_code == 200:
            pokemon_info = response.json()
            self.pokemon_data[pokemon_name.lower()] = {
                "name": pokemon_info["name"],
                "id": pokemon_info["id"],
                "types": [t["type"]["name"] for t in pokemon_info["types"]],
                "abilities": [a["ability"]["name"] for a in pokemon_info["abilities"]]
            }
            return self.pokemon_data[pokemon_name.lower()]
        else:
            return None

    def load_pokemon_data(self):
        try:
            with open("pokemon_data.json", "r") as file:
                self.pokemon_data = json.load(file)
        except FileNotFoundError:
            pass

    def save_pokemon_data(self):
        with open("pokemon_data.json", "w") as file:
            json.dump(self.pokemon_data, file, indent=4)

    def draw_pokemon(self):
        pokemon_name = input("Would you like to draw a Pokemon? (yes/no): ").strip().lower()
        if pokemon_name == "yes":
            pokemon_list_url = "https://pokeapi.co/api/v2/pokemon/?limit=1000"
            response = requests.get(pokemon_list_url)
            if response.status_code == 200:
                pokemon_list = response.json()["results"]
                random_pokemon = random.choice(pokemon_list)["name"]
                if random_pokemon in self.pokemon_data:
                    print("Pokemon Details:")
                    self.print_pokemon_details(random_pokemon)
                else:
                    print("Fetching Pokemon details...")
                    pokemon_details = self.fetch_pokemon_details(random_pokemon)
                    if pokemon_details:
                        print("Pokemon Details:")
                        self.print_pokemon_details(random_pokemon)
                    else:
                        print("Failed to fetch Pokemon details.")
            else:
                print("Failed to fetch Pokemon list.")
        else:
            print("Thank you for using the Pokemon App!")
            exit()

    def print_pokemon_details(self, pokemon_name):
        details = self.pokemon_data[pokemon_name]
        print(f"Name: {details['name'].capitalize()}")
        print(f"ID: {details['id']}")
        print("Types:", ", ".join(details['types']))
        print("Abilities:", ", ".join(details['abilities']))


if __name__ == "__main__":
    app = PokemonApp()
    app.load_pokemon_data()
    while True:
        app.draw_pokemon()
        app.save_pokemon_data()
