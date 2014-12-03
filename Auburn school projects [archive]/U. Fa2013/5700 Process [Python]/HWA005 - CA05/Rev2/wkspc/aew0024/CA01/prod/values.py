import math  

class Values:      
    def __init__(self,values = []):
        self.theValues = values
        if(len(self.theValues) < 1):
            raise ValueError("Values.__init__: list is empty")

        
    #function median returns the median of a list.
    def median(self):
        cloned = self.theValues[:]        
        cloned.sort()        
        size = len(cloned)                 
        if (size % 2) > 0:        
            mid = (size / 2) + 1        
            return cloned[mid - 1]        
        else:        
            mid1 = (size / 2)        
            mid2 = mid1 + 1        
            avg = (cloned[mid1 - 1] + cloned[mid2 - 1]) / 2.0        
            return avg        
                
    #function product returns the product of the list            
    def product(self):          
        prod = 1        
        for x in range(len(self.theValues)):        
            prod = prod * self.theValues[x]        
        return prod        
             
    #function produces the second largest element in the list            
    def penultimate(self):        
        if len(self.theValues) < 2 :
            print "RuntimeError "           
            raise ValueError("Values.penultimate: list has no penultimate")  
        elif len(self.theValues) == 2:        
            return self.theValues[1]        
        else :        
            self.theValues.sort()        
            return self.theValues[-2]        
            
    #produces the standard deviation of a list        
    def stdev(self):        
        n = len(self.theValues)        
        if n < 1:        
            raise ValueError("Values.stdev: list has one or fewer values") 
        elif n == 1:        
            return 0        
        else:        
            mean = sum(self.theValues)        
            mean = mean / n         
            dev = self.theValues[:]        
            for j in range(len(self.theValues)):        
                temp = self.theValues[j] - mean        
                dev[j] = pow(temp, 2)        
            devSum = sum(dev)        
            x = devSum / (n - 1)        
            answer = math.sqrt(x)          
            return answer
        
    #returns the original list        
    def getValue(self):        
        return self.theValues
        
