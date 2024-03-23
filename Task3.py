import pandas as pd
import matplotlib.pyplot as plot
#Read the dataset
dataset = pd.read_csv("C:\\Users\\Luzuko\\Downloads\\motor_insure.csv\\motor_data11-14lats.csv")

#Inspects its column by displaying the first 10 records.
print(dataset.head(10))

#Display records for make and usage for sets_num that are more than 40
dataset = pd.read_csv("C:\\Users\\Luzuko\\Downloads\\motor_insure.csv\\motor_data11-14lats.csv")

filter_df= dataset [dataset['SEATS_NUM']>40]
#print(mthozami.columns)
print(filter_df.head(10))

#Plot a basic graph showing effective_yr on y-axes and carrying capacity on x-axes
plot.ylabel('EFFECTIVE_YR')
plot.xlabel("CARRYING CAPACITY")
plot.show()