import pandas as pd
file=pd.read_csv("/home/student/suhas/data.csv")
print("\n DATA SET VALUE")
print("-------------\n")
print(file)
dframe=pd.Dataframe(file)
print("freq distrubution")
orint("-----------\n")
data=dframe.groupby(['gender','result']).size().unstuk().reset_index()
data['total']=(data['p']+data['f'])
data['pass-percent']=data['p']/data['toatl']
data['fail_percent']=data['f'] / data['total']
print(data[:5])