NOL=int(input("Number of Luggage : "))
WOL=0
for i in range(NOL):
    WOL+=int(input("Weight of Luggage "+str(i+1)+" : "))

if WOL>25:
    print("Weight of Luggage Exceeds Allowed Limit of 25 Kgs : ",WOL,"Kgs")
else:
    print("Weight of Luggage is Within Allowed Limit : ",WOL,"Kgs")