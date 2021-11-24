from brownie import FakeHorse01, FakeHorse02, config, network
from .helpful_scripts import get_account

def main():
  account = get_account()
  fakeHorse01 = deploy_fakehorse01(account)
  fakeHorse02 = deploy_fakehorse02(account)



def deploy_fakehorse01(account):
  fakeHorse01 = FakeHorse01.deploy("FakeHorse01", "FH01", {"from": account}, publish_source=config["wallets"][network.show_active()].get("verify"))
  print(f'Factory Contract Deployed in {fakeHorse01.address}')
  return fakeHorse01.address

def deploy_fakehorse02(account):
  fakeHorse02 = FakeHorse02.deploy("FakeHorse02", "FH02", {"from": account}, publish_source=config["wallets"][network.show_active()].get("verify"))
  print(f'Factory Contract Deployed in {fakeHorse02.address}')
  return fakeHorse02.address