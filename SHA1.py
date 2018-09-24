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

    # adding padding so the message
    m_bin += b'\x00' * ((56 - (byte_len + 1) % 64) % 64)
    # the length of the message if printed will show the number of bytes and it is = (448 mod 512)

    # add 64 bits padding
    m_bin += struct.pack(b'>Q', bit_len)
    # the length of the mesage now is equl to (0 mod 512) it will show in bytes so it will show like (0 mod 64)


    # break the method into 512 bit chunks (64 bytes chunks)
    for i in range(0, len(m_bin)-64, 64):
        chunk = m_bin[i:i+64]
        # break each chunk to words of 4 bytes (16 words)
        word = [0] * 80
        for j in range(0, 64-4, 4):
            w = chunk[j:j+4]
            word[j:j+4] = struct.unpack(b'>I', w)[0]

        # extend the 16 words to 80 words
        for k in range(16, 80):
            word[j] = _left_rotate(word[k - 3] ^ word[k - 8] ^ word[k - 14] ^ word[k - 16], 1)


    # after this step, the length of m_bin is = 448 mod 512

    # break into block of 64 bits and (maybe use big endian)??
    # now we apply the function 80 rounds
    #  https://www.youtube.com/watch?v=YCf80-8xhGs

    return m_bin

print(sha1("abffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbbffffffcdbffffffcdbffffffcdbffffffcdffffbffffffcdbffffffcdbffffffcdffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcdbffffffcde"))