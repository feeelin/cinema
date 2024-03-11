from typing import Iterable, Generator


def get_flatten_collection_generator(collection: Iterable) -> Generator:
    for item in collection:
        if isinstance(item, Iterable):
            for subitem in item:
                yield subitem
        else:
            yield item
