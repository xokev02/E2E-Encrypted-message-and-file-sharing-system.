// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.4.0 <=0.9.0;

contract testChat {
    event NewMessage(
        string message,
        address user,
        uint256 timestamp,
        string roomName
    );

    address owner;
    // uint userCount=0;

    struct Message {
        string message;
        address user;
        uint256 timestamp;
    }

    mapping(string => Message[]) public roomNameToMessages;
    mapping(address => string) public addressToUsername;

    function construter() public {
        owner = msg.sender;
    }

    // Send a message to a room and fire evant
    function sendMessage(string calldata _msg, string calldata _roomName)
        external
    {
        Message memory message = Message(_msg, msg.sender, block.timestamp);
        roomNameToMessages[_roomName].push(message);
        emit NewMessage(_msg, msg.sender, block.timestamp, _roomName);
    }

    // Functions for creating and fetching custom usernames. If a user updates
    // their username it will update for all of their messages
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

    // for geting lenth of message in room
    function getMessageCountForRoom(string calldata _roomName)
        external
        view
        returns (uint256)
    {
        return roomNameToMessages[_roomName].length;
    }

    // this function is for retrive message by roomname and index
    function getMessageByIndexForRoom(string calldata _roomName, uint256 _index)
        external
        view
        returns (
            string memory,
            address,
            uint256
        )
    {
        Message memory message = roomNameToMessages[_roomName][_index];
        return (message.message, message.user, message.timestamp);
    }
}
