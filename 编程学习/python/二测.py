shen=input("请输入您的身份证：")
year=int(shen[6:10])
month=int(shen[10:12])
day=int(shen[12:14])
if year<=2005:
    if month<=11:
        if day<=26:
           print("是")
        else:print("否")
    else:print("否")
else:print("否")

