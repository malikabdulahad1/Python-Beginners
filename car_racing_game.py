i=0;
choose = ''
st= 'stop'
s='start'
e = 'exit'
h = 'help'


while i<=i:
    choose=input(">")
    if choose== s or choose == s.upper():
        print('Car started...Ready to go')
    elif choose==st or choose==st.upper():
        print('Car game Stop')
    elif choose==e or choose==e.upper():
        print('Car game exit')
        break
    elif choose==h or choose==h.upper():
        print("start - to start the car")
        print("stop - to stop the car")
        print("exit - to exit")
    else:
        print("I don't understand")
    i=i+1


