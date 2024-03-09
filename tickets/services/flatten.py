def flatten(lol):
    lol = list(lol)

    for item in lol:
        if isinstance(item, tuple):
            for subitem in item:
                yield subitem

        else:
            yield item
