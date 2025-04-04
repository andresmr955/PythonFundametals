import utils

list_x = [
        {'Country': 'USA', 'Population': 331002651},
        {'Country': 'Canada', 'Population': 37742154},
        {'Country': 'Mexico', 'Population': 128932753},
        {'Country': 'Brazil', 'Population': 212559417},
        {'Country': 'Argentina', 'Population': 45195777},
    ]

def run():
    keys, values =utils.get_population()

    print(keys, values)

    country = input("Enter the country name: ")
    solution = utils.population_by_country(list_x, country)
    print(solution)

if __name__ == "__main__":
    run()