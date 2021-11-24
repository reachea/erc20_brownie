from brownie import FakeHorse01, Contract

def main():
  fakeHorse01 = Contract.from_abi("FakeHorse01", "0x61505879BB49caf3fDCb9A3148B75093509Ffc80", FakeHorse01.abi)
  balance = fakeHorse01.balanceOf("0x42Ba4d31Bb3aFc48af42F9603d3E1C860a2eBb22")
  print(f'This is amount of owner: {balance}')