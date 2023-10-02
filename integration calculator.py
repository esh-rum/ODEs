import numpy as np 

class Integration():
    def __init__ (self, function):
        self.function = function
        
    def formulas(self):
        if "^" in self.function:                    #integrates the eqs with powers
            base, power = self.function.split("^")  #splits and stores the base and power
            #print(base, ", ", power)
            
            if power.isdigit():
                power = int(power)                  #sees if power is integer or not
            else:
                if "x" in power:                    
                    var = "x"
                    pow2 = power[0]
                    print(pow2)
                elif "y" in power:
                    var = "y"
                    pow2 = power[0]

            if base == "x" or base == "y":          #implements power rule
                if power != "-1":
                    power = power + 1
                    base = f"({base} ^ {power})"
                    result = f"{base} / {power} + c"
                    return result 
                else:
                    result = f"ln({base}) + c"      #implements this log rule something
                    return result    
            elif "cos" in base:                     #trying to implement some cos rules somehow
                if pow2 == "1":
                    result = f"sin{var} + c"
                    return result
                elif pow2 == "2":
                    result = f"{var}/2 + (sin2{var})/4 + c"
                    return result
                elif pow2 == "3":
                    result = f"((2 + cos^2{var})sin{var})/3 + c"
                    return result
            elif "sin" in base:                     #trying to implement some sin rules somehow
                if pow2 == "1":
                    result = f"-cos{var} + c"
                    return result
                elif pow2 == "2":
                    result = f"{var}/2 - (sin2{var})/4 + c"
                    return result
                elif pow2 == "3":
                    result = f"-((2 + sin^2{var})cos{var})/3 + c"
                    return result
            elif "tan" in base:                     #trying to implement some tan rules somehow
                if pow2 == "1":
                    result = f"-ln|cos{var}| + c"
                    return result
                elif pow2 == "2":
                    result = f"tan{var} - {var} + c"
                    return result
                elif pow2 == "3":
                    result = f"(tan^2{var})/2 + ln|cos{var}| + c"
                    return result
               
        
        
def main():
    func = input ("Enter function to be integrated: ")
    
    if func == "cosx":                      #converts these simple functions into this form for solving
        func = "cos^1x"
    elif func == "cosy":
        func = "cos^1y"
    elif func == "sinx":                      
        func = "sin^1x"
    elif func == "siny":
        func = "sin^1y"
    elif func == "tanx":                      
        func = "tan^1x"
    elif func == "tany":
        func = "tan^1y"
        
        
    integ = Integration(func)
    result = integ.formulas()
    
    print(result)
    
main()