class Pakistan():
    def capital(self):
        print("The capital of Pakitan is Islamabad")
    def language(self):
        print("Punjabi is the widely spoken language in the Pakistan")
    def type(self):
        print("It is a developing country")
class USA():
    def capital(self):
        print("The capital of USA is washington D.C")
    def language(self):
        print("English is the widely spoken language in the USA")
    def type(self):
        print("It is a developed country")
obj_pak = Pakistan()
obj_USA = USA()
for country in (obj_pak,obj_USA):
    country.capital()
    country.language()
    country.type()