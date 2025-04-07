'''
import csv

def read_population(path):
    with open(path, mode="r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        
       
        for row in reader:
            print('***' * 6)
            result = list(zip(header, row))
            print(result)
if __name__ == '__main__':            
    read_population('./world_population.csv')

'''
import csv

def read_population(path):
    with open(path, mode="r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict)
            print(data)
if __name__ == '__main__':            
    read_population('./world_population.csv')