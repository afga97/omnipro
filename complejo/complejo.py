
class Complejo:
    """"
        B. Complejos
        Dado 2 números complejos, A y B, desarrollar un código que imprima los valoresde:
        ◦ A+B
        ◦ A-B
        ◦ A*B
        ◦ A/B
        ◦ Mod(A)
        ◦ Mod(B)
        Para esta parte, deberá utilizar una clase, llamada Complejo, la cual deberá inicializar con una parte real y una 
        parte imaginaria,y tener los métodos antesdescritos.
        Por ejemplo:
            A=Complejo(2,1)
            B=Complejo(5,6)
            A+B -> 7.0+7.0i
            A-B -> -3.0-5.0i 
            A*B -> 4.00+17.00i
            A/B -> 0.26-0.11i
            Mod(A) -> 2.24+0.00i
            Mod(B) -> 7.81+0.00i
    """
    _instances = []
    a = None
    b = None

    
    def __new__(cls, *args, **kwargs):
        obj = super(Complejo,cls).__new__(cls)
        obj._from_base_class = type(obj) == Complejo
        cls._instances.append(obj)
        return obj
    
    def __init__(self, a, b):
        if len(self._instances) == 1:
            self.a = complex(a, b)
        elif len(self._instances) == 2:
            self.b = complex(a, b)

    def __del__(self):
        self._instances = []
        
    def addition(self, a, b):
        """
            Suma A + B
        """
        return a + b

    def subtraction(self, a, b):
        """
            Resta A - B
        """
        return a - b

    def multiplication(self, a, b):
        """
            Multiplicación A * B
        """
        return a * b

    def division(self, a, b):
        """
            Division A / B
        """
        return a / b

    def modulus(self, number):
        """
            MOD a and MOD b
        """
        return abs(number)


text_menu = "Seleccione una opción \n"\
    "1. Sumar \n"\
    "2. Restar \n"\
    "3. Multiplicar \n"\
    "4. Dividir \n"\
    "5. Mod A \n"\
    "6. Mod B \n"\
    "7. Salir \n\n"
option_selected = int(input(text_menu))
A = Complejo(2, 1)
B = Complejo(5, 6)
message = ""
if option_selected == 1:
    result = A.addition(A.a, B.b)
    message = 'El resultado de la suma es: {}'.format(result)
elif option_selected == 2:
    result = A.subtraction(A.a, B.b)
    message = 'El resultado de la resta es: {}'.format(result)
elif option_selected == 3:
    result = A.multiplication(A.a, B.b)
    message = 'El resultado de la multiplicación es: {}'.format(result)
elif option_selected == 4:
    result = A.division(A.a, B.b)
    message = 'El resultado de la division es: {}'.format(result)
elif option_selected == 5:
    result = A.modulus(A.a)
    message = 'El mod de A es: {}'.format(result)
elif option_selected == 6:
    result = A.modulus(B.b)
    message = 'El mod de B es: {}'.format(result)
else:
    message = 'Hasta pronto.'
print(message)
