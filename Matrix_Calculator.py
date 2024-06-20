n=int(input("Enter your row of the matrix: "))
n1=int(input("Enter your column of the matrix: "))
class Input_Matrix():
    def __init__(self,n,n1):
        self.A=[]
        self.B=[]
        self.mat=[]
        for i in range(n):
            mat1=[]
            for j in range(n1):
                mat1.append(0)
            self.mat.append(mat1)

        
        print("Enter the numbers of matrix A")
        for i in range(n):
            mat2=[] 
            for j in range(n1):
                num=int(input("Enter your number: "))
                mat2.append(num)
            self.A.append(mat2)
        print("Enter the numbers of matrix B")
        for i in range(n):
            mat2=[] 
            for j in range(n1):
                num=int(input("Enter your number: "))
                mat2.append(num)
            self.B.append(mat2)
        print("Matrix A\t=",self.A)
        print("Matrix B\t=",self.B)
       
    def add(self):
        print("ADD")
        mat=[]
        for i in range(n):
            mat4=[]
            for j in range(n1):
                c=self.A[i][j]+self.B[i][j]
                mat4.append(c)
            mat.append(mat4)
        print(mat)
        
    def sub(self):
        print("Subraction")
        mat=[]
        for i in range(n):
            mat4=[]
            for j in range(n1):
                c=self.A[i][j]-self.B[i][j]
                mat4.append(c)
            mat.append(mat4)
        print(mat)
 
    def multiply(self):
        print("Multiplication")
        for i in range(n):
            for j in range(n1):
                for k in range(n):
                    self.mat[i][j]+=self.A[i][k]*self.B[j][i]
        print(self.mat)

    def transpose(self):
        print("transpose")
        for i in range(n):
            for j in range(n1):
                self.mat[j][i]=self.A[i][j]
        print(self.mat)


cal=Input_Matrix(n,n1)
matrix=str(input("Enter your choice of matrix(+,-,*): "))
if matrix=="+":
    cal.add()
elif matrix=="-":
    cal.sub()
elif matrix=="*":
    cal.multiply()
else:
    cal.transpose()