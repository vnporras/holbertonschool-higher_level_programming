#!/usr/bin/python3
from abc import ABC, abstractmethod


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in the list. No item removed.")

    def pop(self, index=-1):
        try:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
            return item
        except IndexError:
            print(f"Index [{index}] out of range. No item popped.")
            raise
