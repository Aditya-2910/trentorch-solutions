def cache_hit_rate(keys: list[int]) -> tuple[int, int, float]:
    """
    keys: a sequence of request keys in arrival order.

    A request is a hit iff its key has appeared earlier in the sequence
    (the first occurrence of any key is always a miss).

    Return (hits, misses, rate) where rate = hits / len(keys).
    """
    # TODO: track which keys have been seen so far, in order.
    cache = set()
    miss = 0
    hits = 0
    n = len(keys)
    for i in keys:
        if i not in cache:
            cache.add(i)
            miss+=1
        else:
            hits+=1
    rate = round(hits / n, 6)
    return (hits,miss,rate)
    
    pass
