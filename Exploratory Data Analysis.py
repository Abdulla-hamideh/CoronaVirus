import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# read the file
total_cases = pd.read_csv("total_cases_by_la_20201022.csv")

# see the variable
print(total_cases.to_string())

#highest 10 city
modified = total_cases.groupby("CAName")["TotalCases"].sum().sort_values(ascending= False).head(10)
modified.plot.barh(color = "orange")
plt.title("Highest 10 Scottish Cities with Confirmed Cases")
plt.xlabel("Confirmed Cases")
plt.ylabel("City Name")
plt.show()

# Crude rate deaths
portion= total_cases.groupby("CAName").CrudeRateDeaths.sum().sort_values(ascending=False).head(25)
print(portion)
plt.figure(figsize=(40,20))
portion.plot.pie(shadow= True, autopct="%1.1f%%", wedgeprops= {"edgecolor": "black"})
plt.title("Crude Rate Deaths")
plt.axis("equal")
plt.show()

# read the second file
daily = pd.read_csv("monthlycases.csv")
# missing = daily.isnull().any()
# print(missing)
# pp= daily.dropna(axis= "columns")
# print(pp)
daily = daily.drop(columns= ["Unnamed: 4",  "Unnamed: 5", "Unnamed: 6"])
l= daily.Date
x = daily.CumulativeCases
y= daily.Deaths
z= daily.MonthlyCases
plt.plot(l,x, label= "Monthly Cumulative")
plt.plot(l,y, label= "Deaths")
plt.plot(l,z, label= "Monthly Cases")
plt.title("Covid-19 Monthly Cases in Scotland")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.legend()
plt.show()

Monthly_Cases= daily.MonthlyCases
Cumulative_cases= daily.CumulativeCases
Deaths= daily.Deaths
plt.title("Monthly Cases Summary")
plt.ylabel("Cases")

plt.boxplot([Monthly_Cases,Deaths])
plt.xticks([1,2],["Monthly_Cases","Deaths"])
# daily.plot(kind= "box", subplots=True)

plt.show()




# count values
# portion1 = total_cases.CAName.value_counts()
# portion1.plot.pie()
# plt.show()


array = pd.read_csv("trend_agesex_20201023.csv")
score = ["TotalPositive", "TotalDeaths"]
a= array.groupby("AgeGroup")[score].sum()
a= a.drop("Total", axis=0)
a.plot.bar()
plt.title("Confirmed Cases spread between the Age Group")
plt.ylabel("Cases")
plt.show()


# b = []
# for x in a.index:
#     (b.append(x[0:2]))
# b[-1] = 1000
# print(b)
# a = pd.DataFrame(a)
# a["sort"] = np.array(b,dtype=int)
# print((a.sort_values(["sort"])))
# c = a.sort_values(["sort"]).drop("Total", axis=0)
# d = c.sort_values(["sort"]).drop(columns= "sort")
# print(d)
# d.plot.bar()
# plt.show()

sex = array.groupby("Sex")[score].sum()
sex= sex.drop("Total", axis=0)
sex.plot.bar()
plt.ylabel("Cases")
plt.title("Confirmed cases spread between Gender")
plt.show()

#total cases vs total deaths
city= pd.read_csv("trend_ca_20201027.csv")
glasgow= city[city["CAName"]== "Glasgow City"]
glasgow1= glasgow.MonthlyPositive
date= glasgow.Date
Edinbrugh = city[city["CAName"]== "City of Edinburgh"]
Edinbrugh1= Edinbrugh.MonthlyPositive
Nlarak = city[city["CAName"]== "North Lanarkshire"]
nlarak = Nlarak.MonthlyPositive
Slarak = city[city["CAName"]== "South Lanarkshire"]
slarak= Slarak.MonthlyPositive
Dundee = city[city["CAName"]== "Dundee City"]
dundee= Dundee.MonthlyPositive
Renfrewshire = city[city["CAName"]== "Renfrewshire"]
renfrewshire = Renfrewshire.MonthlyPositive
Fife = city[city["CAName"]== "Fife"]
fife = Fife.MonthlyPositive
Aberdeen = city[city["CAName"]== "Aberdeen City"]
aberdeen = Aberdeen.MonthlyPositive
West= city[city["CAName"]== "West Lothian"]
west = West.MonthlyPositive
East= city[city["CAName"]== "East Dunbartonshire"]
east = East.MonthlyPositive
plt.plot(date,glasgow1, label= "Glasgow")
plt.plot(date, Edinbrugh1, label = "City of Edinburgh")
plt.plot(date, nlarak, label= "North Lanarkshire")
plt.plot(date,slarak , label= "South Lanarkshire")
plt.plot(date,renfrewshire , label= "Renfrewshire")
plt.plot(date,dundee , label= "Dundee City")
plt.plot(date,fife , label= "Fife")
plt.plot(date,aberdeen , label= "Aberdeen City")
plt.plot(date,west , label= "West Lothian")
plt.plot(date,east , label= "East Dunbartonshire")
plt.title("Covid-19 Monthly Cases in the top 10 cities in Scotland")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.legend()
plt.show()













