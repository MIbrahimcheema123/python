def totalcalc(billamount,tipperc):
    total = billamount*(1+0.01*tipperc)
    total = round(total,0)
    print("ok so your bill is:",total)
totalcalc(150,20)