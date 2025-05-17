import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('time-complexity.csv')
print(df.head)


#Graphs

plt.figure(figsize=(10,6))
plt.plot(df['n'], df['LOOP'], marker='o', label='LOOP')
plt.plot(df['n'], df['Recursivity'], marker='s', label='Recursivity')
plt.xlabel('n (Quantity of iterations)')
plt.ylabel('Time Seconds')
plt.title('Comparison of times: Loop vs Recursivity')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
