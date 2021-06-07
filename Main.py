def Newworld():
    key='abcdefghijklmnopqrstuvwxyz123456789 !'
    value=key[-1]+key[0:-1]

    EncryptDic=dict(zip(key,value))
    DecryptDic=dict(zip(value,key))

    message=input('Enter a message: ')
    Choice=input('Enter in which type you want to send a message ("E" & "D"): ')

    if Choice.upper() == 'E':
        new= ''.join([EncryptDic[log] for log in message.lower()]) 
    elif Choice.upper() == 'D':
        new= ''.join([DecryptDic[log] for log in message.lower()])
    else:
        print('Enter a write choice')
    
    return new

print(Newworld())
