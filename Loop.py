#a = list(range(1,1000))
#even_num = list()
#odd_num = list()
#multiple_of_6 = list()
#for n in a:
    #if n % 6 == 0:
        #multiple_of_6.append(n)
    #elif n % 2 == 0:
        #even_num.append(n)
    #else:
        #odd_num.append(n)
#print("Even Numbers:", even_num)
#print("Odd Numbers:", odd_num)
#print("Multiples of 6:", multiple_of_6)


import pandas as pd

res = {
    "Q1": ["yes", "no", "yes", "yes"],
    "Q2": [5, 3, 4, 5],
    "Q3": ["M", "F", "M", "F"]
}
df = pd.DataFrame(res)
print(df)

count = res["Q1"].count("yes")
print(count)

avg = sum(res["Q2"]) / len(res["Q2"])
print(avg)

count_male = res["Q3"].count("M")
print(count_male)       
count_female = res["Q3"].count("F")
print(count_female)

df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "Experience": [5, 3, 4, 5],
    "Score": [90, 85, 88, 92]
})
print(df)
import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "Experience": [5, 3, 2, 5],
    "Score": [79, 85, 88, 92]
})

# Filter condition
filtered_df = df[(df["Experience"] >= 3) & (df["Score"] >= 80)]

print(filtered_df)
