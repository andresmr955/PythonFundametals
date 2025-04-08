import csv
import matplotlib.pyplot as plt
import charts 

original_file = './world_population.csv'


def read_csv(path):
    with open(path, mode='r+') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        data = list(filter(lambda item: item['Continent'] == 'South America', data))

        values = list(map(lambda x: x['World Population Percentage'], data))
        labels = list(map(lambda x: x['Country/Territory'], data))
        
        #print( labels, values)

        charts.generate_pie(labels, values)


if __name__ == '__main__':
    read_csv(original_file)
            