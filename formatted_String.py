first = 'abdul'
last = 'ahad'
# abdul [ahad] is a coder

message = first + ' [' + last + '] is a coder'
print(message)

# but this is not good approch

msg = f'{first} [{last}] is a coder'
print(msg)