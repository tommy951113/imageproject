import pandas as pd
df = pd.read_csv('data.csv', header=0, encoding='gbk')
# print(df.head(6))
breakfast = []
lunch = []
dinner = []
afternoontea = []
nightsnack = []
protein = "蛋白质总量"
co = "碳水总量"
for i in range(5):
    breakfast.append(df.iloc[i])
# print(breakfast)
    lunch.append(df.iloc[i+5])
    dinner.append(df.iloc[i+10])
for i in range(3):
    afternoontea.append(df.iloc[i+15])
    nightsnack.append(df.iloc[i+18])
tonic = df.iloc[21]

# print(breakfast[0]["蛋白质总量"])
resultList = []
result = {}
for i,val in enumerate(breakfast):
    for j,val in enumerate(lunch):
        for k,val in enumerate(dinner):
            for l,val in enumerate(afternoontea):
                for m,val in enumerate(nightsnack):
                    result["name"] = "早餐{}+午餐{}+晚餐{}+下午茶{}+夜宵{}: ".format(i+1,j+1,k+1,l+1,m+1)
                    result["protein"] = breakfast[i]["蛋白质总量"] + lunch[j]["蛋白质总量"] + dinner[k]["蛋白质总量"] + afternoontea[l]["蛋白质总量"] + nightsnack[m]["蛋白质总量"] + 20.25
                    result["co"] = breakfast[i][co] + lunch[j][co] + dinner[k][co] + afternoontea[l][co] + nightsnack[m][co] + 0.675
                    resultList.append(result)
                    result = {}
df = pd.DataFrame(resultList)
df.to_csv('out.csv', index=False, encoding='gbk')