import numpy as np

class FirstEx:
    def __init__(self, n, k, cost):
        self.n = n
        self.k = k
        self.cost = cost
        self.matrix = [[0 for i in range(k)]  for j in range(n+1)]#np.zeros((self.n+1,self.k))
        self.res = self.summation = self.diff = self.prevdiff = 0
        self.matrix1 = self.E1_a()
        self.matrix2 = self.E1_b()
        
    def E1_a(self): # O(N^2 * K)
        for i in range(self.k-1, -1, -1):
            ex_val = 0
            for p in range(0, self.n+1):
                ex_val = 0
                for j in range(0, self.n+1):
                    if j < p:
                        if i == self.k-1: ex_val += p/(self.n+1)
                        else: ex_val += (self.matrix[p][i+1])/(self.n+1)
                    else:
                        if i == self.k-1: ex_val += j/(self.n+1)
                        else: ex_val += (self.matrix[j][i+1])/(self.n+1)
                ex_val -= self.cost[i]
                self.matrix[p][i] = round(max(p - self.cost[i], ex_val),4)
        return self.matrix
        
    def E1_b(self): #   O(N * K)   
        for i in range(self.k-1, -1, -1):
            s = self.summation/(self.n+1)
            self.summation = self.diff = 0
            self.prevdiff = 0
            for p in range(0, self.n+1):
                if i == self.k-1:
                    if p == 0: ex_val = ((self.n*(self.n+1))/2)/(self.n+1)
                    else: ex_val = self.matrix[p-1][i] + (p/(self.n+1)) + self.cost[i]
                else:
                    if p == 0: ex_val = s
                    else:
                        self.diff = (self.matrix[p][i+1]-self.matrix[p-1][i+1])*p + self.prevdiff
                        self.prevdiff = self.diff
                        ex_val = s + (self.diff)/(self.n+1)
                ex_val -= self.cost[i]
                self.matrix[p][i] = round(max(p - self.cost[i] , ex_val),4)
                self.summation += self.matrix[p][i]
        return self.matrix
    
    # Verification of correctness
    def areTheSameMatrix(self):
        a = np.matrix(self.matrix1)
        b = np.matrix(self.matrix2)
        return a == b
    
if __name__ == "__main__":
    FirstEx = FirstEx(n = 20, k = 3, cost = [7,3,5])
    print("--------------------FIRST MATRIX------------------------")
    print(np.matrix(FirstEx.E1_a()))
    print("--------------------------------------------------------\n\n")
    print("--------------------SECOND MATRIX-----------------------")
    print(np.matrix(FirstEx.E1_b()))
    print("--------------------------------------------------------")
    print("\n\nCheck if the two matrices are the same:\n",FirstEx.areTheSameMatrix())
    
    
   
