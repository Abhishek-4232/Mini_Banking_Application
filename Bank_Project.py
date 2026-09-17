def total_balance():
    print(f"Your Balance is {balance} ")
    
    
    
def deposit(amt):
    global balance
    if amt>0:
        balance+=amt
        print("---Amount Added Successfully---")
    else:
        print("Unable To Add Money")




def withdrawal(amt):
    global balance
    
    if amt>balance:
        print("Low Balance !!!!")
    elif amt<=0:
        print("Can't Withdrawal Amount")
    else:
        balance-=amt
        print("---Withdrawal Successful---")
    
    


balance=0.0
if __name__=="__main__":
    while True:
        print("Enter '1' for Balance Check")
        print("Enter '2' for Add Money")
        print("Enter '3' for Withdrawal Money")
        print("Enter '4' for Quit")
        choice=input("Enter You choice (1-4):")
        
        
        
        
        if choice=="1":
            print("=============================")
            total_balance()
            print("=============================")
            
            
        elif choice=="2":
            print("=============================")
            amt=float(input("Enter the Amount to Add:"))
            deposit(amt)
            print("=============================")
            
            
            
        elif choice=="3":
            print("=============================")
            amt=float(input("Enter Amount to Withdrawal:"))
            withdrawal(amt)
            print("=============================")
            
            
            
        elif choice =="4":
            print("=============================")
            print("---Thank You For Banking--- ")
            print("=============================")
            break
        
        
        else:
            print("=============================")
            print("Invalid Input!!!  Re-Try")
            print("=============================")
            
            
        