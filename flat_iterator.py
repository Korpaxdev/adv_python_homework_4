class FlatListIterator:
    def __init__(self, deep_list):
        self._cursors = [0]
        self._current = deep_list
        self._old = []

    def __iter__(self):
        return self

    def __next__(self):
        while self._cursors:
            index = self._cursors[-1]
            if index >= len(self._current):
                self._current = self._old.pop() if self._old else []
                self._cursors.pop()
                continue
            item = self._current[index]
            if isinstance(item, list):
                self._cursors[-1] = index + 1
                self._cursors.append(0)
                self._old.append(self._current)
                self._current = item
                continue
            self._cursors[-1] = index + 1
            return item
        raise StopIteration
