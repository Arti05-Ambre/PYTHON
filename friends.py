file=open("Friends1.txt","w")
for i in range(1,6):
    print(f"\nEnter details of Friends{i}")
    first=input("First Name:")
    middle=input("Middle Name:")
    last=input("Last Name:")
    file.write(first+ " " +middle+ " " +last+"\n")
file.close()
print("\nNames Successfully stored in Friends1.txt")




output
Enter details of Friends1
First Name:Ambre
Middle Name:Arti
Last Name:Dipak

Enter details of Friends2
First Name:Dere
Middle Name:Prachi
Last Name:Jayran

Enter details of Friends3
First Name:Bhoknal
Middle Name:Divya
Last Name:Uttam

Enter details of Friends4
First Name:Deshmukh
Middle Name:Viashnavi
Last Name:Datta

Enter details of Friends5
First Name:Ambre
Middle Name:Shruti
Last Name:Dipak

Names Successfully stored in Friends1.txt
