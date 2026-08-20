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


if __name__ == "__main__":
    main()