#Signature

def square_and_multiply(base, exponent, N):
    # Convert the exponent to binary
    exponent_binary = "{0:b}".format(exponent)
    #print(exponent_binary)
    
    # Initialize the result
    result = 1
    
    # For each bit in the binary exponent
    for bit in exponent_binary:
        # Square the result
        result = (result ** 2) % N
        if bit == '1':
            # Multiply it by the base
            result = (result * base) % N
    return result
    
# Let's sign the message 
def sign_message(message, d, N):
    signed_chunks = []
    # a. Divide the message into 3-byte chunks
    # b. Convert each chunk into a hexadecimal string
    # c. Convert each chunk into an integer number

    for i in range(0, len(message), 3):
        chunk = message[i:i+3]
        
        chunk = bytes(chunk, 'utf-8')
        print(chunk)
        chunk_hex = chunk.hex()
        chunk_int = int(chunk_hex, 16)
        
        # d. Sign the numbers
        signed_chunk = square_and_multiply(chunk_int, d, N)
        
        # e. Output the list of integers
        signed_chunks.append(signed_chunk)
    return signed_chunks
# Parameters
message = "Tariqul Islam"
d = 2352382571
N = 2568119003
# Using the sign_message function
signed_message = sign_message(message, d, N)
print(f'Signed chunks: {signed_message}')

