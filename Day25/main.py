import pandas as pd

data = pd.read_csv("Day25/Squirrel_Data.csv")
colors_count = data["Primary Fur Color"].value_counts().reset_index()
colors_count.columns = ["Fur Color", "Count"]

df = pd.DataFrame(colors_count)

df.to_csv("squirrel_count.csv")