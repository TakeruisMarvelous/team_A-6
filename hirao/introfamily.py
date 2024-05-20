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
    def cat_out(self,cat_name):
        self.cat_name = cat_name
        cat_nametxt = "飼い猫の名前は、"+self.cat_name+"です"
        return cat_nametxt

Takeru = Intro("健",22)
print(Takeru.name_out())
print(Takeru.age_out())
print(Takeru.cat_out("縫"))