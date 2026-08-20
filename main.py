import calculations

def main():
    species = calculations.get_species()
    print(species)  # test

    weight = calculations.get_weight()
    print(weight) # test

    bcs = calculations.get_bcs()
    print(bcs) # test

if __name__ == "__main__":
    main()