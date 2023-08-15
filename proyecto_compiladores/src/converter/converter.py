from random import randint

class Converter():

    def __init__(self):
        pass

    def convert(self, number, destiny):
        if destiny == "hexadecimal":
            return format(number, "0x")
        
        if destiny == "octal":
            return format(number, "0o")
        
        if destiny == "binary":
            return format(number, "0b")
        
        if destiny == "roman":
            result = self.to_roman(number)
            return result

        if destiny == "alternative":
            result = self.to_alternative(number)
            return result

        if destiny == "random":
            option = self.to_random()
            if(option == 1):
                result = format(number, "0x")
            elif(option == 2):
                result = format(number, "0o")
            elif(option == 3):
                result = format(number, "0b")
            elif(option == 4):
                result = self.to_roman(number)
            elif(option == 5):
                result = self.to_alternative(number)

            return result

    def to_roman(self, number):
        arabic_numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans_numbers = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        r = ''
        i = 0
        
        while number > 0:
            for _ in range(number // arabic_numbers[i]):
                r += romans_numbers[i]
                number -= arabic_numbers[i]  
            i += 1
            
        return r

    def to_alternative(self, number):
        equivalences = {
            "0":"O", 
            "1":"L",
            "2":"Z",
            "3":"E",
            "4":"A",
            "5":"S",
            "6":"G",
            "7":"F",
            "8":"B",
            "9":"P",
        }
        tmp = str(number)
        convertions = []
        
        for digit in tmp:
            for key in equivalences:
                if(digit == key):
                    convertions.append(equivalences[key])
                    
        converted_number = "".join(convertions)
        
        return converted_number

    def to_random(self):
        rand_option = randint(1, 5)
        return rand_option

