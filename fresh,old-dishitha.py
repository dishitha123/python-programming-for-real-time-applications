fresh=int(input("enter the number of fresh loves purchased"))
old=int(input("enter the number of day old loaves purchased"))
print("Regular price: Rs.185.00")
fresh_amount = 185.00*float(fresh)
old_amount = (185*0.4)*float(old)
Total=fresh_amount+old_amount
print("Amount of the new loaves:Rs " ,fresh_amount)
print("Amount of the day old loaves: Rs" ,old_amount)
print("Total amount: Rs",Total)
