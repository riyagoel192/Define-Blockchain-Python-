#Building Blockchain using functions
blockchain=[]

def get_last_val(): #return last value of the blockchain
    return blockchain[-1]


def add_value(name,last_transaction=[1]):
    blockchain.append([last_transaction, name])  #-1 refers to last value item and last value item is a nested list too

def get_user_input():
    return float(input('Your transaction amount please: '))


tx_amount= get_user_input()
add_value(tx_amount)

tx_amount= get_user_input()
add_value(last_transaction=get_last_val(), name=tx_amount)    #keyword arguments

tx_amount= get_user_input()
add_value(tx_amount,get_last_val())

print(blockchain)