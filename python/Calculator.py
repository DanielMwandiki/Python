class calculator :
      
    def _int_(self ,a ,b):
        self.a = a
        self.b = b
        
    def add(self) :
        return self.a + self.b

    def mull(self) :
        return self.a * self.b

        #################
calc = calculator(10,20)
print(calc.add())
print(calc.mull())
