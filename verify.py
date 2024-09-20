## Verify Signature

def square_and_multiply(base, exponent, modulus):
    # Convert the exponent to binary format
    exponent_binary = bin(exponent)[2:]
    # Initialize result to 1
    result = 1
    # Traverse through each bit in the binary exponent
    for bit in exponent_binary:
        result = (result ** 2) % modulus  # Square the result
        if bit == '1':
            result = (result * base) % modulus  # Multiply by base if this bit is 1
    return result
def decrypt_signed_message(signed_message, e, N):
    decrypted_message = ""
    for signed_chunk in signed_message:
        # Decrypt each chunk of the signed message
        decrypted_chunk = square_and_multiply(signed_chunk, e, N)
        # Conversion of the decrypted integer to hexadecimal
        decrypted_chunk_hex = hex(decrypted_chunk)[2:]
        # Treat two hexadecimal characters as one byte (8 bits)
        decrypted_chunk_string = "".join(chr(int(decrypted_chunk_hex[i:i+2], 16)) for i in range(0, len(decrypted_chunk_hex), 2))
        # Append the decrypted chunk to the full message
        decrypted_message += decrypted_chunk_string
    return decrypted_message
# Provided parameters    
e = 251
N = 2251665769
signed_message = [995493001, 1041023700, 2058502926, 1399360676]
# Using the decrypt_signed_message function
message = decrypt_signed_message(signed_message, e, N)
print("Decrypted message: ", message)