// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.4.0 <=0.9.0;

contract testChat {
    event NewMessage(
        string message,
        address user,
        uint256 timestamp
    );

    address owner;
    // uint userCount=0;

    struct Message {
        string message;
        address user;
        uint256 timestamp;
    }

    mapping(address => string) public addressToUsername;

    function construter() public {
        owner = msg.sender;
    }

    function sendMessage(string calldata _msg, string calldata _roomName)
        external
    {
        Message memory message = Message(_msg, msg.sender, block.timestamp);
        roomNameToMessages[_roomName].push(message);
        emit NewMessage(_msg, msg.sender, block.timestamp, _roomName);
    }

    function createUser(string calldata _name) external {
        addressToUsername[msg.sender] = _name;
        // userCount = userCount+1;
    }

    function getUsernameForAddress(address _user)
        external
        view
        returns (string memory)
    {
        return addressToUsername[_user];
    }
}
