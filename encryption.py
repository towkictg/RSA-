## Encryption


import binascii
def square_and_multiply(base, exponent, modulus):
    binary_exponent = bin(exponent)[2:]
    result = 1
    for i in binary_exponent:
        result = (result ** 2) % modulus
        if i == '1':
            result = (base * result) % modulus
    return result
def encrypt_chunks(hex_chunks, N, e):
    return [square_and_multiply(int(chunk, 16), e, N) for chunk in hex_chunks]
def main(): 
    message = "Hello INSE 6110"
    N = 2251665769
    e = 251
    
    # Convert message to bytes, split into 3-byte chunks, then convert to hexadecimal
    message_bytes = message.encode('utf-8')
    #print(message_bytes)
    byte_chunks = [message_bytes[i:i+3] for i in range(0, len(message_bytes), 3)]
    hex_chunks = [binascii.hexlify(chunk).decode('utf-8') for chunk in byte_chunks]
   
    print(byte_chunks)
   
    
    encrypted_message = encrypt_chunks(hex_chunks, N, e)
    print(encrypted_message)
main()

