i = int(input('enter your purchase amount in Tomans : '))

if i > 1000000 :
    discount = i * 15 / 100
    finalprice =  i - discount
    print('The final amount payable is : ',int(finalprice), 'Tomans.')
elif 500000 < i < 1000000 :
    discount = i * 10 / 100
    finalprice =  i - discount
    print('The final amount payable is : ',int(finalprice), 'Tomans.')
elif i < 500000:
    print('Without discount : The final amount payable is : ',i,'Tomans.')
    