from os import access
from brownie import FakeHorse01, Contract
from .helpful_scripts import get_account

def main():
  account = get_account()
  fakeHorse01 = Contract.from_abi("FakeHorse01", "0x61505879BB49caf3fDCb9A3148B75093509Ffc80", FakeHorse01.abi)
  tx = fakeHorse01.approve("0x9Ac64Cc6e4415144C455BD8E4837Fea55603e5c3", 115792089237316195423570985008687907853269984665640564039457584007913129639935, {"from": account})
  tx.wait(1)
  print(f'Approved at: {tx.logs}')