import calculations

def main():
    species = calculations.get_species()
    print(f'Species: {species}')  # test

    weight = calculations.get_weight()
    print(f'Current weight: {weight} lbs') # test

    bcs = calculations.get_bcs()
    print(f'BCS: {bcs} out of 9') # test

    ideal_weight = calculations.calculate_ideal_weight(weight, bcs)
    print(f'Ideal weight: {ideal_weight} lbs') # test

    rec_kcal = calculations.calculate_daily_calories(ideal_weight, species)
    print(f'Recommended kcal/day for goal weight: {rec_kcal} ')   # test

if __name__ == "__main__":
    main()