import numpy as np 

class Integration():
    def __init__ (self, function):
        self.function = function
        
    def formulas(self):
        if "^" in self.function:
            base, power = self.function.split("^")
            if power.isdigit():
                power = int(power)
            if base == "x" or base == "y":
                if power != "-1":
                    power = power + 1
                    base = f"({base} ^ {power})"
                    result = f"{base} / {power} + c"
                    return result 
                else:
                    result = f"ln({base}) + c"   
                    return result    
        
        
def main():
    func = input ("Enter function to be integrated: ")
    integ = Integration(func)
    result = integ.formulas()
    
    print(result)
    
main()