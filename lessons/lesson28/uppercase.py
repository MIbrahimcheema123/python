class UPPER:
    def __init__(self):
        self.key = ""
    def name(self):
        self.key = input("Enter the string yyou want in upper case:")
    def Upper_case(self):
        print("The reult of",self.key,"will be","'",self.key.upper(),"'")
i=UPPER()
i.name()
i.Upper_case()