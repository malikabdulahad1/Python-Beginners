secrets_number =9
i=1;
while i<=3:
    gues=input(f'Guess {i}: ')
    i = i + 1;
    if int(gues)==secrets_number:
        print('your are win')
        break

else:
    print('Sorry you lose')
