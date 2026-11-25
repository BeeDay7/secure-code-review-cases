import random
from . import vulnerable, fixed

def test_vulnerable_is_reproducible_from_seed():
    assert vulnerable.reset_token(random.Random(42)) == vulnerable.reset_token(random.Random(42))

def test_fixed_tokens_are_unique_and_long():
    tokens = {fixed.reset_token() for _ in range(1000)}
    assert len(tokens) == 1000 and all(len(t) >= 43 for t in tokens)
