def generate_fibonacci_like_sequence(limit):
    a, b = 3, 4
    sequence = [a, b]
    while a + b <= limit:
        a, b = b, a + b
        sequence.append(b)
    return sequence

def sum_even_numbers(sequence):
    return sum(x for x in sequence if x % 2 == 0)

limit = 7000000
sequence = generate_fibonacci_like_sequence(limit)
result = sum_even_numbers(sequence)
print(result)


