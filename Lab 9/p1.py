def min_amount(C,A):
        if(A<=0) :
              return 0
        else :
             amount = C[0]*A
             for i in C :
                 amount=min(amount,i+min_amount(C,A-i))
             return amount
                  
       
      



print(min_amount([8,5,5],17))