import pandas
import matplotlib.pyplot as plt

# Prepare data from from csv
data = pandas.read_csv("data.csv")
df = pandas.DataFrame(data)

df["Overall Score"] = df["Overall Score"].astype(int)
df["Auto Score"] = df["Auto Score"].astype(int)
df["Hangar Score"] = df["Hangar Score"].astype(int)
df["Penalty Score"] = df["Penalty Score"].astype(int)
df["Overall Difference"] = df["Overall Difference"].astype(int)
df["Auto Difference"] = df["Auto Difference"].astype(int)
df["Hangar Difference"] = df["Hangar Difference"].astype(int)
df["Penalty Difference"] = df["Penalty Difference"].astype(int)

boxplot = df.boxplot(column="Auto Score", by="Result")
box2 = df.boxplot(column="Hangar Score", by="Result")
box3 = df.boxplot(column="Overall Score", by="Result")
box4 = df.boxplot(column="Overall Difference", by="Result")
box5 = df.boxplot(column="Auto Difference", by="Result")
box6 = df.boxplot(column="Hangar Difference", by="Result")

plt.show()