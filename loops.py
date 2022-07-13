#Copyright July 2022 Zainab Jalloh

#while loop uses conditional expression to control the loop
secrete = 'blowfish_twofish_SHA'
pw = ''
count = 0
max_attempts = 3
success = False

while pw !=secrete:
    count +=1
    if count > max_attempts: break
    pw = input(f'{count}/{max_attempts} Password: ')
else:
    success=True

print('Success' if success else 'reset password?')

#continue shortcuts/skips, break leaves loop early, else exits loop

colors = ('red', 'yellow', 'green', 'magenta', 'blue', 'purple')

for i in colors:
    if i == 'green' : continue
    if i == 'blue': break
    print(i)
else:
    print('bye')
