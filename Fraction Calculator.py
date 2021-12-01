
'num Abbreviation of numerator'
'den Abbreviation of denominator'

'function to take input for the fraction from the user'
def get_number(user) -> int:
    while True:
        try:
            userinput: str = input(user)
            return int(userinput)
        except ValueError:
            print("Invalid input. Please enter only numeric values.")
            continue


'function to check input of operator'
def check_operator() -> 'opr':
    while True:
        opr=  input('''Enter the Operation to be performed (+,-,/,==) :''')
        if opr in ['+', '-', '*', '/', '==']:
            return str(opr)
        else:
            print("Invalid input. Enter a valid operator.")
            continue

'class to create fraction by assigning user input to numerator and denominator. Also has arithmetic operations of fractions'
class Fraction:
    def __init__(self, num: int, den: int) -> None:
        self.num: int = num
        if den == 0:
            raise ValueError('''Invalid input. Denominator of a fraction cannot be "0", Enter another number.''')
        self.den: int = den

    'function to add two fractions'
    def plus(self, other: "Fraction") -> "Fraction":
        finalnum: int = (self.num * other.den) +  (self.den * other.num)
        finalden: int = self.den * other.den
        return Fraction(finalnum, finalden)

    'function to subtract two fractions'
    def minus(self, other: "Fraction")-> "Fraction":
        finalnum: int = (self.num * other.den) - (self.den * other.num)
        finalden: int = self.den * other.den
        return Fraction(finalnum, finalden)

    'function to multiply two fractions'
    def times(self, other: "Fraction")-> "Fraction":
        finalnum: int = self.num * other.num
        finalden: int = self.den * other.den
        return Fraction(finalnum, finalden)

    'function to divide two fractions'
    def divide(self, other: "Fraction")-> "Fraction":
        finalnum: int = self.num * other.den
        finalden: int = self.den * other.num
        return Fraction(finalnum, finalden)

    'function to check if the two entered fractions are equal. will return value true or false'
    def equal(self, other: "Fraction") -> bool:
        return self.num * other.den == self.den * other.num

    'function to print the fraction as string'
    def __str__(self) -> str:
        return str(self.num) + "/" + str(self.den)

def get_Fraction():
    num: int = int(input("Enter the value for numerator:"))
    while True:
        den: int = int(input("Enter the value for denominator:"))
        try:
            Fraction(num, den)
        except ValueError:
            print("Invalid input. Denominator of a fraction cannot be 0, Enter another number.")
        else:
            return Fraction(num, den)


def calc(f1: "Fraction", opr: str, other: "Fraction"):
    """In this function, we will call the appropriate operation function based on the user's input choide and print the final result post computation."""
    if opr == "+":
        print(f'{f1.num} / {f1.den} + {other.num} / {other.den} = {str(f1.plus(other))}')
    elif opr == "-":
        print(f'{f1.num} / {f1.den} - {other.num} / {other.den} = {str(f1.minus(other))}')
    elif opr == "*":
        print(f'{f1.num} / {f1.den} * {other.num} / {other.den} = {str(f1.times(other))}')
    elif opr == "/":
        print(f'{f1.num} / {f1.den} / {other.num} / {other.den} = {str(f1.divide(other))}')
    elif opr == "==":
        print(f'{f1.num} / {f1.den} == {other.num} / {other.den} = {str(f1.equal(other))}')

'main functin which runs the program by calling other functions'
def main() -> None:
    print("Welcome to the fraction calculator!")
    print("Enter Fraction 1 :")
    f1: Fraction = get_Fraction()
    print("Enter Fraction 2: ")
    other: Fraction = get_Fraction()
    opr: str= check_operator()

    'function call for calculation which will do all the operations'
    calc(f1, opr , other)

'to have test cases to check if program works correctly'
def test_cases() -> None:
    print("TEST CASES:")
    f12: Fraction = Fraction(1, 2)
    f44: Fraction = Fraction(4, 4)
    f128: Fraction = Fraction(12, 8)
    f32: Fraction = Fraction(3, 2)
    print(f"{f12} + {f12} = {f12.plus(f12)} [4/4]")
    print(f"{f44} - {f12} = {f44.minus(f12)} [4/8]")
    print(f"{f12} + {f44} = {f12.plus(f44)} [12/8]")
    print(f"{f128} == {f32} is {f128.equal(f32)} [True]")

    'test case with 3 operands'
    print(f"{f44} + {f12} + {f32} = {f44.plus(f12).plus(f32)} [48/16]")

if __name__ == '__main__':
    main()
    test_cases()
