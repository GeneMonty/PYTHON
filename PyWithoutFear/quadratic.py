def quadratic(a,b,c):
        #determinant is the part under the root
        determinant = (b*b - 4 * a * c)**0.5 # **0.5 = sqrt(2)= x^1/2
        x1 = (-b + determinant) / (2 * a)
        x2 = (-b - determinant) / (2 * a)
        print ("X=",x1,"\n","X=",x2)

quadratic (1,-1,-1)

