class Numbers:

    def sum(self, num1, num2):
        if(num1 == 0 or num2 == 0 ):
            raise ValueError('ningun numero puede ser cero')
        return num1 + num2;


