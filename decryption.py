
## Decryption

def square_and_multiply(base, exponent, modulus):
    binary_exponent = bin(exponent)[2:]
    result = 1
    for i in binary_exponent:
        result = (result ** 2) % modulus
        if i == '1':
            result = (result * base) % modulus
    return result
def decrypt(encrypted_message, d, N):
    decrypted_message = []
    for chunk in encrypted_message:
        msg_int = square_and_multiply(chunk, d, N)  # Use square and multiply algorithm to decrypt
        hex_msg = hex(msg_int)[2:]  # Convert integer to hex (strip the "0x" part)
        if len(hex_msg) % 2 != 0:  # If it's odd number, prepend '0' to make it even
            hex_msg = '0' + hex_msg
        chunk_msg = bytearray.fromhex(hex_msg).decode()  # Convert hex to bytes then bytes to string
        decrypted_message.append(chunk_msg)
    print(decrypted_message)
    return ''.join(decrypted_message)  # Combine all chunks to get full message
# Provided parameters
d = 2352382571
N = 2568119003
encrypted_message = [1936121606, 1854494117, 1584870285, 382602404]
# Decrypt the encrypted message with the provided private exponent 'd' and modulus 'N'
message = decrypt(encrypted_message, d, N)
print("Decrypted message: ", message)