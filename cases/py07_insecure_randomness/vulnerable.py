import random, string

def reset_token(rng: random.Random = random.Random()) -> str:
    # Flaw: non-cryptographic PRNG.
    return "".join(rng.choice(string.ascii_letters + string.digits) for _ in range(20))
