#!/usr/bin/env python
# coding: utf-8

# In[26]:


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# Read data from Excel
df = pd.read_excel('C:/Users/firas/Desktop/GDP.xlsx')

# Create the figure
fig, ax = plt.subplots()

# Set initial data for the first year
current_year = 2013
current_data = df[df['Year'] == current_year]

# Create the bar chart 
bars = ax.barh(current_data['Country'], current_data['GDP'], color='lightgreen')
ax.set_xlim(0, 25000)

# Update the bar chart for each year
def update_chart(year):
    current_year = year
    current_data = df[df['Year'] == current_year]
    
    for bar, val in zip(bars, current_data['GDP']):
        bar.set_width(val)
    ax.set_title(f'GDP in billions by Country - Current$ - ({current_year})')

# Create the animation
ani = animation.FuncAnimation(fig, update_chart, frames=df['Year'], repeat=False)
ani.interval = 1000

# Save the animation as a GIF file
ani.save('C:/Users/firas/Desktop/animated_chart.gif', writer='pillow')
print("Animation saved successfully.")


# In[ ]:




