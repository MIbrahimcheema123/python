s1 = {12,23,34,45,56,67,78,89,90,0}
s2 = {"hi","why","hello","wsp","iamnotbad","ngl","no cap","cap","ez","ggs"}
result = list(zip(s1,s2))
print(result)
l1 = [0,10,20,30,40,50,60,70,80,90,100]
l2 = [10,9,8,7,6,5,4,3,2,1,0]
for x,y in zip(l1,l2[::-1]):
    print(x,y)
stock = ["read","write","work hard","succed"]
prices = [12,314,346784,365379736563,65349907854]
resulttttttt = {stock : prices for stock,prices in zip(stock,prices)}
print(resulttttttt)