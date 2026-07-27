import random
import pandas as pd
names=["ahmed","mohamed","khaled","abdullah","mohammad", "mohsen", "mohsin", "mohd", "abdul", "abdelaziz", "abdel", "abdelrahman", "abdel-rahman", "abdel-rahmoun", "abdel-rahmoun", "abdel-rahmoun", "abdel-rahmoun", "abdel-rahmoun", "abdel-rahmoun", "abdel-rahmoun", "abdel-rahmoun", "abdel-rahmoun", "abdel-rahmoun", "abdel-rahmoun"]
subjects=["math","science","english","history","geography","computer science","physics","chemistry","biology","economics","politics","law","art","music","sports","business","psychology","religion","philosophy","literature","language","geography","history","mathematics","physics","chemistry","biology","economics","politics","law","art","music","sports","business","psychology","religion","philosophy","literature","language"]
def stream():
    dic={
        "name":random.choice(names),
        "age":random.randint(18,100),
        "gender":random.choice(["male","female"]),
        "subject":random.choice(subjects),
        "marks":random.randint(0,100),
    }
    return dic

gen= (stream() for i in range(50))
genlist=[]
finallist=[]
faild=set()
for i in gen:
    genlist.append(i)
for i in genlist:
    if i["marks"]>=90:
        i["grade"]="A"
        finallist.append(i)
    elif i["marks"]>=80:
        i["grade"]="B"
        finallist.append(i)
    elif i["marks"]>=70:
        i["grade"]="C"
        finallist.append(i)
    elif i["marks"]>=60:
        i["grade"]="D"
        finallist.append(i)
    else:
        i["grade"]="F" 
        faild.add(i["name"])  
data = pd.DataFrame(finallist)
total       = len(genlist)
passed      = len(finallist)
pass_rate   = round((passed / total) * 100, 1)
print(f"success rate: {pass_rate}%{total}")
print("\nmax marks:")
print(data.groupby("subject")["marks"].max().sort_values(ascending=False).to_string())
print("GRAdes:")
print(data["grade"].value_counts().to_string())
print(f"students not passed names: {faild}")
print(f"students failed count: {len(faild)}")