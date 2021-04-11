print("1-Residential")
print("2-Commercial")
cat = int ( input ( "Choose Category: " ))
unitsH = int(input(" Please enter Number of Units in Higher Tariff you Consumed : "))
unitsL = int(input(" Please enter Number of Units in Lower Tariff you Consumed : "))

if (cat==1):
    a=5;
elif (cat==2):
    a=10;
if(unitsH < 50 and unitsL<50):
    amount = unitsH * 2.60+unitsL/1.5+a
    surcharge = 25
elif(unitsH <= 100 and unitsL<=100):
    amount = 130 + ((unitsH - 50) * 3.25)+unitsL/1.5+a
    surcharge = 35
elif(unitsH <= 200 and unitsL<=200):
    amount = 130 + 162.50 + ((unitsH - 100) * 5.26)+unitsL/1.5+a
    surcharge = 45
    print("Selected Category: ", c)

elif (cat==2):
    unitsH = int(input(" Please enter Number of Units in Higher Tariff you Consumed : "))
    unitsL = int(input(" Please enter Number of Units in Lower Tariff you Consumed : "))
if(unitsH < 50 and unitsL<50):
    amount = unitsH * 2.60+unitsL/1.5
    surcharge = 25
elif(unitsH <= 100 and unitsL<=100):
    amount = 130 + ((unitsH - 50) * 3.25)+unitsL/1.5
    surcharge = 35
elif(unitsH <= 200 and unitsL<=200):
    amount = 130 + 162.50 + ((unitsH - 100) * 5.26)+unitsL/1.5
    surcharge = 45
    print("Selected Category: ", c)

total = amount + surcharge
print("\nElectricity Bill = %.2f" % total);






