def get_species():
    """Get and return the pet's species via console input. Returns a string - "dog" or "cat"."""
    while True:
        species = input('Type "d" for dog, "c" for cat: ').lower()

        if species in ("d", "c"):
            species_name = "dog" if species == "d" else "cat"
            print(f"You selected {species_name}")
            return species_name

        print("Invalid input, please try again.\n")


def get_weight():
    """Get and return the pet's current weight in lbs via console input. Returns a float."""
    while True:
        try:
            weight = float(input('Enter weight in lbs: '))

            if 0 < weight < 300:
                return weight

            print("Invalid input: Impossible weight! Please try again.")

        except ValueError:
            print("That is not a valid number! Weight must be a whole number or decimal.\nPlease try again.")


def get_bcs():
    """Get and return the pet's Body Condition Score (1-9, whole number) via console input. Returns an integer."""
    while True:
        try:
            bcs = int(input('Enter Body Condition Score (whole number 1-9): '))

            if 0 < bcs <= 9:
                return bcs

            print("Invalid input! BCS must be a whole number between 1 and 9.\nPlease try again.")

        except ValueError:
            print("That is not a valid number! Please try again.")


def calculate_ideal_weight(species, current_weight, bcs):
    #TODO: Calculate ideal weight based on species, current weight, and BCS
    pass


def calculate_daily_calories(ideal_weight, species):
    #TODO: Calculate recommended daily calorie range for the ideal weight
    pass