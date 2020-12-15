# def distance(strand_a, strand_b):
#     if len(strand_a) != len(strand_b):
#         raise ValueError(f"{strand_a} and {strand_b} dont have the same length")
    
#     hamming_dist = 0
#     for i in range(len(strand_a)):
#         if strand_a[i] != strand_b[i]:
#             hamming_dist += 1
    
#     return hamming_dist




# def distance(strand_a, strand_b):
#     # Raise an error if sequences are not equal length
#     if len(strand_a) != len(strand_b):
#         raise ValueError(f"{strand_a} and {strand_b} dont have the same length")
    
#     hamming_dist = 0
#     for letter_a, letter_b in zip(strand_a, strand_b):  # Compare each letter in sequence_A with its corresponding in the sequence_B
#         if letter_a != letter_b:
#             hamming_dist += 1
    
#     return hamming_dist


def distance(strand_a, strand_b):
    # Raise an error if sequences are not equal length
    if len(strand_a) != len(strand_b):
        raise ValueError(f"{strand_a} and {strand_b} dont have the same length")
    
    hamming_dist = 0
    l= list(zip(strand_a, strand_b))
    print(l)

    x = map(lambda a : (hamming_dist += 1) if a[0] == a[1], zip(strand_a, strand_b))


    return hamming_dist


print(distance("CATCGTAATGACGGCCT", "GAGCCTACTAACGGGAT"))