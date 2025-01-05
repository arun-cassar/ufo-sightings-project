import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#before "\complete.csv" input the directory to the file
data = pd.read_csv(r"\complete.csv", delimiter=',')


#in this part of the script, I used dropna() to remove rows which contain missing values.
#Because I was only interested in data from the United States, I then filtered the data. I also filtered out Washington DC and Puerto Rico, because they aren't states.

copy = data.copy()
ufo_data = (copy[['datetime', 'state', 'country']]).dropna()
filtered = ufo_data[ufo_data['country'] == 'us']
filtered = filtered[filtered['state'] != 'dc']
filtered = filtered[filtered['state'] != 'pr']
filtered = filtered.drop_duplicates(subset=['datetime', 'state'])

#I then sorted by date because I wanted to know across which years the dataset spanned.
sorted = filtered.sort_values(by='datetime')

num_by_state = filtered['state'].value_counts().reset_index(name='number of sightings')


plt.figure(figsize=(20,10))
plt.bar(x = num_by_state['state'].str.upper(), 
        height = num_by_state['number of sightings'],
       color = "midnightblue")
plt.xticks(rotation = 45, fontsize = 13)
plt.yticks(fontsize = 13)
plt.title("Number of UFO Sightings by US State (1944 - 2013)", fontsize = 16, fontweight = "bold")
plt.ylabel("Number of Sightings", fontsize = 13)
plt.savefig("UFO Sightings by US State.png")
plt.show()
