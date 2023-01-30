num = int(input('Enter number of the day of the week: ' ))
while num < 1 or num > 7:
    num = int(input('Wrong! Enter the day of the week: ' ))
if num <= 5:
    print('No Holiday. I need go to work(.')
else:
    print('Holiday!!!')