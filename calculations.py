def get_species():
    while True:
        species = input('Type "d" for dog, "c" for cat: ').lower()

        if species in ("d", "c"):
            species_name = "dog" if species == "d" else "cat"
            print(f"You selected {species_name}")
            return species

        print("Invalid input, please try again.\n")

def get_weight():
    #TODO: Return the current weight (in lbs)
    pass

def get_bcs():
    #TODO: Return the body condition score (out of 9)
    pass

def calculate_ideal_weight(species, current_weight, bcs):
    #TODO: Calculate ideal weight based on species, current weight, and BCS
    pass

def calculate_daily_calories(ideal_weight, species):
    #TODO: Calculate recommended daily calorie range for the ideal weight
    pass