class Intro:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def name_out(self):
        nametxt = "私の名前は、"+self.name+"です"
        return nametxt
    
    def age_out(self):
        agetxt = "年齢は、" + str(self.age) + "です"
        return agetxt

Takeru = Intro("健",22)
print(Takeru.name_out())
print(Takeru.age_out())