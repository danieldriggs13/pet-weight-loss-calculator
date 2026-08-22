DIVISOR_PER_BCS = {1: 0.7, 2: 0.8, 3: 0.9, 4: 1.0, 5: 1.0, 6: 1.1, 7: 1.2, 8: 1.3, 9: 1.4}

DOG_KCAL_MATH = {"rer_pow": 0.75, "max_kcal_multiplier": 1.4}
CAT_KCAL_MATH = {"rer_pow": 0.67, "max_kcal_multiplier": 1.1}

"""
TODO: Come up with better rounding factors, taking into consideration varience in dog sizes - need to break dogs into weight ranges.
ROUNDING_FACTOR = {"dog": 100, "cat": 10}
"""

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

    # Convert weights from lbs to kg for calculations
    current_weight_kg = current_weight / 2.2
    ideal_weight_kg = ideal_weight / 2.2

    kcal_math = DOG_KCAL_MATH if species == "dog" else CAT_KCAL_MATH

    # Calculate RER (Resting Energy Requirement) for current and ideal weights
    rer_kcal_current = 70 * current_weight_kg ** kcal_math["rer_pow"]
    rer_kcal_ideal = 70 * ideal_weight_kg ** kcal_math["rer_pow"]

    # Current weight's RER with a 20% reduction in calories
    min_kcal_weight_loss = rer_kcal_current * 0.8

    # Calculate min/max daily calories for the ideal weight
    min_calories = (rer_kcal_current + rer_kcal_ideal + min_kcal_weight_loss) / 3
    max_calories = rer_kcal_ideal * kcal_math["max_kcal_multiplier"]

    #TODO: Finalize and implement ROUNDING_FACTOR on return values
    return round(min_calories), round(max_calories)

"""

Test patient:
Species: dog
Weight: 102.8
BCS: 7

Hand-calculated results:
Ideal weight: 85.7
Recommended kcal/day for goal weight: 1,100 - 1,500

How I got these results:
    Minimum: RER of ideal weight: 1,091 (rounded up to 1,100 for min kcal/day)
    Maximum: 
        Senior kcal of ideal weight: 1,528 (calc: RER * 1.4, rounded down to 1,500 for max kcal/day)
            and
        Obese prone kcal of current weight: 1,501 (calc: RER * 1.2, rounded down to 1,500 for max kcal/day)

Current program results:
Ideal weight: 85.7 lbs
Recommended kcal/day for goal weight: 1114-1528 (close to hand-calculated, but will it work across all species and weights?)


Thoughts:
Too big of a range for min and max kcal/day. Max kcal/day also seems high for a weight loss plan. 
I will need to adjust the calculations to make the range smaller and more appropriate for weight loss.

Ideally the results should also be rounded to nearest appropriate number for owner ease of use while maintaining acceptable accuracy.
Cat ranges for example can be rounded (by 10s) much less than a large dog range (by 100s).

Per Dr. B, she doesn't even give owners a range, she calculates the RER of ideal weight and that is the kcal/day she recommends for the pet. If this amount is not working,
can decrease by 10% and if still not working they need to switch to a weight loss diet, as decreaseing further on normal food can lead to nutritional deficiencies.

Other measurements to consider:

    Ideal Weight (85.7):
        Obese Prone: 1,310 (calc: RER * 1.2)
        
    Current Weight (102.8):
        RER: 1,251
        Weight Loss: 1,001 (min, calc: RER * 0.8) - 1,251 (max, calc: RER * 1.0)
        Obese prone: 1,501 (calc: RER * 1.2)

"""
