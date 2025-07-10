Maths = int(input("enter the number obtained in math :"))
English = int(input("enter the number obtained in english :"))
Science = int(input("enter the number obtained in science :"))
Urdu = int(input("enter the number obtained in urdu :"))
Islamicstudies = int(input("enter the number obtained in islamiat :"))
Quranictranslation = int(input("enter the number obtained in quranic translation :"))
Sst = int(input("enter the number obtained in sst :"))
Ict = int(input("enter the number obtained in ict :"))

# next step is to add your marks you have obtained in papers
sum = int(Maths + English + Science + Urdu + Islamicstudies + Quranictranslation + Sst + Ict )
sum = Maths + English + Science + Urdu + Islamicstudies + Quranictranslation + Sst + Ict 
print ("sum of  Maths,English,Science,Urdu,Islamicstudies,Quranictranslation,Ict,sst are", sum)
perc = (sum/800)*100
print("The percentage you obtained in your exams are :",(perc))