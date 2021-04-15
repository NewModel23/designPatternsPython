# -*- coding: utf-8 -*-
"""
Spyder Edit
"""

from abc import ABCMeta, abstractstaticmethod


class ITypePayment(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_payment_type():
        """ Type of payments """


class Paypayl(ITypePayment):
    def __init__(self):
        self.message="The payment method selected is paypal"
    
    def get_payment_type(self):
        return self.message
    
    def __str__(self):
        return self.message
    
    
class DebitCard(ITypePayment):
    def __init__(self):
        self.message="The payment method selected is debit card..."
    
    def get_payment_type(self):
        return self.message
    
    def __str__(self):
        return self.message
    
    
class MethodFactory:
    @staticmethod
    def get_payment(payment_type):
        try:
            if payment_type=="Paypal":
                return Paypayl()
            
            if payment_type=="DebitCard":
                return DebitCard()
            
            raise AssertionError("Payment method not found")
        except AssertionError as _e:
            print(_e)
            


if __name__ == "__main__":
    PAYMENT = MethodFactory.get_payment("Paypal")
    print(PAYMENT)
            
    
    PAYMENT = MethodFactory.get_payment("DebitCard")
    print(PAYMENT)