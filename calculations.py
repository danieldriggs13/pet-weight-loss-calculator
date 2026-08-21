DIVISOR_PER_BCS = {1: 0.7, 2: 0.8, 3: 0.9, 4: 1.0, 5: 1.0, 6: 1.1, 7: 1.2, 8: 1.3, 9: 1.4}
DOG_KCAL_MATH = {"rer_pow": 0.75, "max_kcal_multiplier": 1.6}
CAT_KCAL_MATH = {"rer_pow": 0.67, "max_kcal_multiplier": 1.2}

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


def calculate_ideal_weight(current_weight, bcs):
    """Calculates pet's ideal weight based on current weight and BCS. Returns a float rounded to 1 decimal place."""
    return round(current_weight / DIVISOR_PER_BCS[bcs], 1)


def calculate_daily_calories(current_weight, ideal_weight, species):
    """Calculates recommended daily calorie range for the pet's ideal weight"""
    current_weight_kg = current_weight / 2.2
    ideal_weight_kg = ideal_weight / 2.2

    kcal_math = DOG_KCAL_MATH if species == "dog" else CAT_KCAL_MATH

    rer_kcal_current = 70 * current_weight_kg ** kcal_math["rer_pow"]
    rer_kcal_ideal = 70 * ideal_weight_kg ** kcal_math["rer_pow"]
    min_kcal_weight_loss = rer_kcal_current * 0.8

    min_calories = (rer_kcal_current + rer_kcal_ideal + min_kcal_weight_loss) / 3
    max_calories = rer_kcal_ideal * kcal_math["max_kcal_multiplier"]

    return round(min_calories), round(max_calories)
