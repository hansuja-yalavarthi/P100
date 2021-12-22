class Atm(object):

    def __init__(self, atm_card_num, pin_num):
        self.atm_card_num = atm_card_num
        self.pin_num = pin_num

    def cashWithdrawal(self):
        print('Cash being withdrawed now.')

    def balanceInquiry(self):
        print('Your balance is being inquired right now. Please wait for a few seconds...', 'Your balance is 2000 dollars.')


Card=Atm(1234567890123456,1234)
print(Card.cashWithdrawal())
print(Card.balanceInquiry())