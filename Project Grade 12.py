import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

print("----------------Airline Reservation System - Employee Table----------------")
print()
df = pd.read_csv ("IP Rare Project.csv")
print(df)
print()
while(True):
    print("----------Please Select an Option------------")
    print("1- Add new Coloumn")
    print("2- Add new Employee")
    print("3- Delete Row")
    print("4- Delete Coloumn")
    print("5- Update Values")
    print("6- Graph comparing salaries of employees")
    print("7- Data Analysis")
    print("8- Exit the Menu")
    print()
    a=int(input("Enter Choice:"))
    
    if a==1:
        l1=[]
        n=input("Enter Column Name:")
        for i in range(1,len(df.index)+1):
            print("Enter Value for",i,"row:",end="")
            h=input()
            l1.append(h)
        df[n] = l1            
            
        print(df)
        print()

    elif a == 2:
        while True:
            ch = input("Add Row [y/n]")
            if ch.lower() == 'y':
                empid = int(input("Emp ID: "))
                name = input("Employee_Name: ")
                dept = input("Department: ")
                deptid =input("DeptNo: ")
                sal = int(input("Salary: "))
                sex = input("Sex (M/F): ")
                Age = int(input("Age: "))
                df = df.append({"EmpID": empid, "Employee_Name":name,
                            "Department": dept, "DeptNo": deptid, "Salary": sal,
                            "Sex": sex, "Age": Age}, ignore_index=True)
                print("The Updated Table is:")
                print(df)
                print()
            else:
                break


    elif a==3:
        print("1. Delete Row by Index")
        print("2. Delete Row by Emp ID.")
        ch = int(input("Select Option: "))
        if ch == 1:
            idx = int(input("Index to delete: "))
            df = df.drop(index = idx)
            print(df)
            print()
        elif ch == 2:
            y = int(input("Emp ID to delete: "))
            df = df.drop(df[df["EmpID"] == y].index)
            print(df)
            print()
        else:
            print("Wrong Option Selected! ")

    elif a==4:
        print("Delete coloumn by coloumn name")
        print("------------------------------")
        na=input("Enter Coloumn Name to be deleted:")
        df = df.drop(na,axis=1)
        print(df)
        print()

    elif a==5:
        while(True):
            ch = input("Update Values [y/n]:")
            if ch.lower() == 'y':
                row=int(input("Enter Index Label:"))
                col=input("Enter Column Name:")
                data1=input("Enter new Data:")
                df.at[row,col]=data1
                print(df)
                print()
            else:
                break
                print()

    elif a==6:
        while(True):
            ch = input("Plot Graphs [y/n]:")
            if ch.lower() == 'y':
                plt.title("Salary Chart")
                plt.xlabel("Names")
                plt.ylabel("Salary")
                plt.xticks(rotation=30)
                plt.grid(True)
                plt.plot(df['Employee_Name'], df['Salary'])
                plt.show()
                
            elif ch.lower() == 'n':
                break

    elif a==7:
        while(True):
            print("--------------Data Analysis Menu---------------")
            print("1- Name Wise Analysis")
            print("2- Department Wise Analysis")
            print("3- Salary Wise Analysis")
            print("4- Exit")
            print()
            ch= int(input("Enter the option: "))
            if ch==1:
                print("--------------------")
                print("1- By Name")
                print("2- Exit")
                print()
                ch2= int(input("Enter your Choice: "))
                if ch2==1:
                    print("-----------------------")
                    da= input("Enter Name: ")
                    print()
                    print(df.loc[df.Employee_Name == da])
                    print()
                else:
                    break
                
            elif ch==2:
                print("-------------------------")
                print("1- By Department Name")
                print("2- Exit")
                print()
                ch3= int(input("Enter choice: "))
                if ch3 == 1:
                    print("--------------------------")
                    ad= input("Enter desired Department Name: ")
                    print()
                    print(df[df.Department == ad])
                    print()
                else:
                    break
            elif ch==3:
                print("----------------------------")
                print("Analysis based on Salary range")
                p1= int(input("Enter lower Salary: "))
                p2= int(input("Enter upper Salary: "))
                print()
                print(df.loc[(df.Salary>p1) & (df.Salary<p2)])
                print()
            else:
                break
            
    else:
        print("Thank You!")
        break
        
   
    
