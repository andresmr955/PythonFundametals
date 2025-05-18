import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('time-complexity.csv')
print(df.head)

fig, (ax1, ax2) = plt.subplots(2,1, figsize=(10,8), gridspec_kw={"height_ratios": [3,1]})
#Graphs

ax1.plot(df['n'], df['LOOP'], marker='o', label='LOOP')
ax1.plot(df['n'], df['Recursivity'], marker='s', label='Recursivity')
ax1.set_xlabel('n (Quantity of iterations)')
ax1.set_ylabel('Time Seconds')
ax1.set_title('Comparison of times: Loop vs Recursivity')
ax1.legend()
ax1.grid(True)


ax2.axis('off')

#table

table = ax2.table(
    cellText=df.round(6).values,
    colLabels=df.columns,
    loc='center'
)


table.scale(1, 1.5)
plt.tight_layout()
plt.savefig('graphtimesimg.png')
plt.show()
