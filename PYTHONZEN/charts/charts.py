import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


def generate_pie(labels, values):
    

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.tight_layout()
    plt.show()
    
if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100,200, 80 ]
    generate_pie(labels, values)