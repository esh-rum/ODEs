import numpy as np 

class Integration():
    def __init__ (self, function):
        self.function = function
        
    def formulas(self):
        if "^" in self.function:
            
            
        
        
def main():
    func = input ("Enter function to be integrated: ")
    result = Integration(func)
    
    print(result)
    
main()