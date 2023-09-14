import sqlite3
import matplotlib.pyplot as plt

#Connecting database
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

#get data form database
cursor.execute('SELECT year, co2, temp FROM your_table_name')
data = cursor.fetchall()

conn.close()

#add data in datalist
years = []
co2 = []
temp = []

for row in data:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

#drawing graph
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)")

#save graph
plt.savefig("co2_temp_1.png") 

plt.show()