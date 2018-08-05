#convert to fahrenheit

def ctof(deg):
    fah=((deg*9)/5) +32;
    return fah;

#convert to celcius

def ftoc(deg):
    cel=(5*deg-160)/9;
    return cel; 

temp=''

#temp=input("What Temperature Scale 'Write the first letter in BLOCK' e.g. C for celsius: ");

while temp != 'F' or temp != 'C':
    temp=input("What Temperature Scale 'Write the first letter in BLOCK' e.g. C for celsius: ");
    if(temp.lower()=='f'):
        deg=float(input("Enter temperature value: "));
        print(ftoc(deg));
    elif(temp.lower()=='c'):
        deg=float(input("Enter temperature value: "));
        print(ctof(deg));
    else:
        print("Please Insert a valid Temperature Scale");







