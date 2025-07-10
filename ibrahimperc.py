Maths = int(input("enter the number obtained in math :"))
English = int(input("enter the number obtained in english :"))
Science = int(input("enter the number obtained in science :"))
Urdu = int(input("enter the number obtained in urdu :"))
Islamicstudies = int(input("enter the number obtained in islamiat :"))
Quranictranslation = int(input("enter the number obtained in quranic translation :"))
Geography = int(input("enter the number obtained in geogarphy :"))
History = int(input("enter the number obtained in history :"))
Ict = int(input("enter the number obtained in ict :"))
Art = int(input("enter the number obtained in art :"))

# next step is to add your marks you have obtained in papers
sum = int(Maths + English + Science + Urdu + Islamicstudies + Quranictranslation + Geography + History + Ict + Art)
sum = Maths + English + Science + Urdu + Islamicstudies + Quranictranslation + Geography + History + Ict + Art
print ("sum of  Maths,English,Science,Urdu,Islamicstudies,Quranictranslation,Geography,History,Ict,Art", sum)
perc = (sum/700)*100
print("The percentage you obtained in your exams are :",(perc))