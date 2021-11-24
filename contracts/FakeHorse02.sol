// SPDX-License-Identifier: MIT 

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FakeHorse02 is ERC20, Ownable {
    uint256 public initialSupply = 1000 * 10**9 * 10**18;
    
    constructor(string memory _name, string memory _symbol) ERC20(_name, _symbol) {
        mint(_msgSender(), initialSupply);
    }
    
    function mint(address _to, uint256 _amount) public onlyOwner {
        _mint(_to, _amount);
    }
    
    function burn(address _from, uint256 _amount) public onlyOwner {
        _burn(_from, _amount);
    }
}