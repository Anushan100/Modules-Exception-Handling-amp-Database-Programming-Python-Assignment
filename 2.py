subject=["Americans","Indians"]
verb=["play","watch"]
objects=["Baseball","Cricket"]

list = [(Sub+' '+vrb+' '+Objct+".") for Sub in subject for vrb in verb for Objct in objects]

print("Output:")

for syn in list:    
    print(syn)