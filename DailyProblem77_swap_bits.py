"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a 32-bit integer, swap the 1st and 2nd bit, 3rd and 4th bit, up til the 31st and 32nd bit.

Here's some starting code and an example:

def swap_bits(num):
  # Fill this in.

print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
# 0b01010101010101010101010101010101
"""
def swap_bits(num):
    # Get all even bits of x 
    even_bits = num & 0xAAAAAAAA
    # Get all odd bits of x 
    odd_bits = num & 0x55555555

    # Right shift even bits 
    even_bits >>= 1
    # Left shift odd bits 
    odd_bits <<= 1

    return (even_bits | odd_bits)

print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
# 0b01010101010101010101010101010101

print("0b" + '{:032b}'.format(swap_bits(5)))