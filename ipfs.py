import ipfshttpclient
import pyipfs

file_path = r'C:\Users\kevin\PycharmProjects\E2E Message and File Sharing System\Actions.py'
output_path = r'C:\Users\kevin\PycharmProjects\E2E Message and File Sharing System\E2E files'


def send_file_to_ipfs(file_path):
    # Initialize IPFS client and add the file
    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
    response = client.add(file_path)
    file_hash = response['Hash']

    # Return the IPFS hash of the file
    return file_hash


def receive_file_from_ipfs(file_hash, output_path):
    # Initialize IPFS client and retrieve the file
    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
    with client.cat(file_hash) as stream:
        with open(output_path, 'wb') as file:
            for chunk in stream:
                file.write(chunk)


# print(ipfshttpclient.__version__)
# print(pyipfs.__version__)

# Send the file to IPFS and retrieve its hash
file_hash = send_file_to_ipfs(file_path)

# Retrieve the file using its hash and save it to a local file
# receive_file_from_ipfs(file_hash, output_path)
