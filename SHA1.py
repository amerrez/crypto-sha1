import struct

def sha1(m):
    # sha1 constants
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # converting to bytes
    m_bin = m.encode()
    byte_len = len(m_bin)
    bit_len = byte_len * 8
    # appending a bit with padding
    m_bin += b'\x80'
    # adding padding so the mesage satisfies m  = 448 (mod 512) becasue we will be adding 64 bits, the length of the original method.
    # that length will be stored in 64 bits and it will make the total length equal to 512
    m_bin += b'\x00' * ((56 - (byte_len + 1) % 64) % 64)
    print(len(m_bin))

    # add 64 bits padding
    print(struct.pack(b'>Q', bit_len))

    # after this step, the length of m_bin is = 448 mod 512

    # break into block of 64 bits and (maybe use big endian)??
    # now we apply the function 80 rounds
    #  https://www.youtube.com/watch?v=YCf80-8xhGs

    return m_bin

print(sha1("abffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbbffffffcdbffffffcdbffffffcdbffffffcdffffbffffffcdbffffffcdbffffffcdffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcde"))