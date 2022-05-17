p=int(input("Enter the prime number p :"))
q=int(input("Enter the prime number q:"))
a=int(input("Enter the assumed number for alice"))
b=int(input("Enter the assumed number for bob"))
A=(q^a)%p
B=(q^b)%p
print("Exchange of Values takes place")
A_key=(B^a)%p
B_key=(A^b)%p
print(" Alice's Private key is:",A_key)
print("Bob's Private key is :",B_key)
