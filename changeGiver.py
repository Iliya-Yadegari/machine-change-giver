itemPrice = int(input('Enter the price of the item ===>'))

if itemPrice > 100 or itemPrice < 25:
    print('This is the wrong price try again.')
else:
    money_given = int(input('How much woney will u give (must be a dollar) ===> '))
    
    if money_given != 100:
        print('Only give one dollar!')
    else:
        print(f'Your change is {money_given - itemPrice}')