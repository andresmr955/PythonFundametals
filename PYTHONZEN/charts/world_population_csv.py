import csv
import matplotlib.pyplot as plt

def read_csv(path, country_user):
    with open(path, mode='r+') as file:
        reader = csv.DictReader(file)
        
        
        for row in reader:
            #print('***' * 6)
            #print(row['Country/Territory'])
            if country_user == row['Country/Territory']:
                #'country': row['Country/Territory'],
                print(f'Your country is {country_user}')
                # list with keys an value
                labels = ['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population']
                values = [int(row[label]) for label in labels]

                #crate a dictionary comprehension

                country_dict = {label: values for label, values in zip(labels, values)}
                print('******' * 6)
                print(country_dict)
                print('******' * 6)
                generate_bar_chart(labels, values)
                
def generate_bar_chart(labels, values):
    #create the figure and axis
    fig, ax = plt.subplots()
    #create graphic and bars
    ax.bar(labels, values)

     # Rotate the X-axis labels to improve readability.
    plt.xticks(rotation=45, ha='right')

    plt.show()


original_file = './world_population.csv'
country_user = input("Which country do you want to se the population?")

title_case = country_user.title()
if __name__ == '__main__':
    read_csv(original_file, title_case)
    