import pytest

from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds

@pytest.fixture
def zero_bank_account():
    print("Creating empty bank account")
    return BankAccount()

@pytest.fixture
def account():
    return BankAccount(100)

@pytest.mark.parametrize("num1, num2, expected",[(3,2,5), 
                                                (5,7,12),
                                                (10,-2,8),])

def test_add(num1, num2, expected):
    assert add(num1, num2) == expected

def test_subtract():
    
    assert subtract(5, 3) == 2  

def test_multiply():
   
    assert multiply(4, 3) == 12

def test_divide():
    
    assert divide(10, 2) == 5

def test_bank_account_deposit(account):
    assert account.balance == 100

def test_bank_default_amount(zero_bank_account):
    print("Testing default amount")
    assert zero_bank_account.balance == 0

def test_bank_account_withdraw(account):
    account.withdraw(50)
    assert account.balance == 50

def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150

def test_collect_interest(account):
    account.collect_interest()
    assert round(account.balance, 6) == 110.0

@pytest.mark.parametrize("deposited, withdrew, expected", [(100, 50, 50), (500, 100, 400), (600, 300, 300)])
def test_bank_transactions(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(200)