a = input('Please enter password:')
has_upper = False
has_lower = False
has_number = False
has_special = False

for i in a : 
    if i.isupper() :
      has_upper =True
      
    if i.islower() :
      has_lower = True
  
    if i.isdigit() :
       has_number = True
     
    if i == '%' or i == '$' or i == '#' or i == '@':
        has_special = True
        
if len(a) >= 8 and has_upper and has_lower and has_number and has_special:
    print('Password is valid')
        
else:
    print('Password is invalid')

    if len(a) < 8:
        print('Password must contain at least 8 characters')

    if has_upper == False:
        print('Password must contain at least one uppercase letter')

    if has_lower == False:
        print('Password must contain at least one lowercase letter')

    if has_number == False:
        print('Password must contain at least one number')

    if has_special == False:
        print('Password must contain a special character')
       
        