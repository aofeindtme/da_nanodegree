#### DO NOT MODIFY ###

import pandas as pd
import numpy as np

seeding = 0

R_mu, R_sig = (16.0, 0.5)
B_mu, B_sig = (16.0, 0.2)
G_mu, G_sig = (16.4, 0.4)
P_mu, P_sig = (16.0, 0.3)
O_mu, O_sig = (16.8, 0.8)

df_config = pd.DataFrame({
    "Colour_raw":['RED','R','Red','red','BLUE','Bleu','Blue','B','G','Green','GREEN','green','O','Orang','Orange','PURP','Purpal','Purple'],
    "Colour_True" : ['Red','Red','Red','Red','Blue','Blue','Blue','Blue','Green','Green','Green','Green','Orange','Orange','Orange','Purple','Purple','Purple'],
    "N_parts" : [2301,5325,6003,8002,1200,490,4450,1151,1990,9012,342,153,5515,23,6351,741,698,4900],
    "Mu": [R_mu,R_mu,R_mu,R_mu,B_mu,B_mu,B_mu,B_mu,G_mu,G_mu,G_mu,G_mu,O_mu,O_mu,O_mu,P_mu,P_mu,P_mu],
    "Sig": [R_sig,R_sig,R_sig,R_sig,B_sig,B_sig,B_sig,B_sig,G_sig,G_sig,G_sig,G_sig,O_sig,O_sig,O_sig,P_sig,P_sig,P_sig]

})

df_mast = pd.DataFrame()
for n1 in range(0,len(df_config)):
    np.random.seed(seeding)
    df_local = pd.DataFrame(
        {'Colour':df_config.loc[n1,'Colour_raw'],
        'Length':np.round(np.random.normal(df_config.loc[n1,'Mu'],df_config.loc[n1,'Sig'],df_config.loc[n1,'N_parts']),3)})
    df_mast = pd.concat([df_mast,df_local])

Measurements = df_mast.sample(frac=1).reset_index(drop=True)
    
Tolerences = pd.DataFrame({'Colour':['Red','Blue','Green','Orange','Purple'],
                       'Lower Tolerence':[14.50,15.625,15.60,14.15,15.25],
                       'Upper Tolerence':[19.150,17.755,18.25,17.95,17.25]})


print("Basis aus der Aufgabenstellung\n\n")


print("df_config\n")
print(df_config)
print("------")

print("df_mast\n")
print(df_mast)
print("------")

print("Measurements\n")
print(Measurements)
print("------")

print("Tolerences\n")
print(Tolerences)
print("------")
    
print("df_mast_new\n")
print(df_mast)
print("------")
print("------")

print("Vorbereitung der Daten\n\n")

true_colour = {
    'RED': 'Red',
    'R': 'Red',
    'red':'Red',
    'Red':'Red',
    'BLUE': 'Blue',
    'Bleu': 'Blue',
    'Blue': 'Blue',
    'B': 'Blue',
    'G': 'Green',
    'Green': 'Green',
    'GREEN': 'Green',
    'green': 'Green',
    'O': 'Orange',
    'Orang': 'Orange',
    'Orange': 'Orange',
    'PURP': 'Purple',
    'Purpal': 'Purple',
    'Purple': 'Purple'
}

df_mast["True_Colour"] = df_mast["Colour"].map(true_colour)

print(df_mast)
print("------")
print("------")



#2. What is the percentage of parts that passed the tolerance bands in the blue category?
# 
print("\n2. What is the percentage of parts that passed the tolerance bands in the blue category?\n")

#   A = parts of blue cat
#   B = parts that passed the tolerance
#   Passed parts is equal to B / A

arr = np.array(df_mast)
blue_sum = np.sum(arr[:, 2]=='Blue', axis=0)
print("\nThe number of parts in the red category is: " + str(blue_sum) + "\n")

print(arr)


#3. What is the percentage of parts that passed the tolerance bands in the green category?

print("\n3. What is the percentage of parts that passed the tolerance bands in the green category?\n")

#   A = parts of blue cat
#   B = parts that passed the tolerance
#   Passed parts is equal to B / A

arr = np.array(df_mast)
green_sum = np.sum(arr[:, 2]=='Green', axis=0)
print("\nThe number of parts in the red category is: " + str(green_sum) + "\n")



#4. What is the interquartile range of lengths in the green category?

print("\n4. What is the interquartile range of lengths in the green category?\n")

arr = np.array(df_mast)
green_sum = np.sum(arr[:, 2]=='Green', axis=0)
print("\nThe number of parts in the red category is: " + str(green_sum) + "\n")

lenghts = np.array(df_mast['Length'])
print(lenghts)


#5. What is the interquartile range of lengths in the orange category?

print("\n5. What is the interquartile range of lengths in the orange category?\n")

arr = np.array(df_mast)
orange_sum = np.sum(arr[:, 2]=='Orange', axis=0)
print("\nThe number of parts in the red category is: " + str(orange_sum) + "\n")



#6. What is the median length in the orange category?

print("\n6. What is the median length in the orange category?\n")

arr = np.array(df_mast)
orange_sum = np.sum(arr[:, 2]=='Orange', axis=0)
print("\nThe number of parts in the red category is: " + str(orange_sum) + "\n")



#7. What is the median length in the purple category?

print("\n7. What is the median length in the purple category?\n")

arr = np.array(df_mast)
purple_sum = np.sum(arr[:, 2]=='Purple', axis=0)
print("\nThe number of parts in the red category is: " + str(purple_sum) + "\n")



#8. What is the number of parts in the purple category?

print("\n8. What is the number of parts in the purple category?\n")

arr = np.array(df_mast)
purple_sum = np.sum(arr[:, 2]=='Purple', axis=0)
print("\nThe number of parts in the Purple category is: " + str(purple_sum) + "\n")



#9. What is the number of parts in the red category?

print("9. What is the number of parts in the red category?\n")

arr = np.array(df_mast)
red_sum = np.sum(arr[:, 2]=='Red', axis=0)
print("\nThe number of parts in the red category is: " + str(red_sum) + "\n")

#df_config.describe()
#print("#####")
#print("")
#print("Measurements.median(axis = 0)")
#Measurements = Measurements[Measurements['Colour'] == 'Red']
#print(Measurements)
#Measurements.median(axis = 0)
