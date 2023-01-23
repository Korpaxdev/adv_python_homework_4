def flat_list_gen(deep_list):
    cursors = [0]
    old = []
    current = deep_list
    while cursors:
        index = cursors[-1]
        if index >= len(current):
            current = old.pop() if old else []
            cursors.pop()
            continue
        item = current[index]
        if isinstance(item, list):
            cursors[-1] = index + 1
            cursors.append(0)
            old.append(current)
            current = item
            continue
        cursors[-1] = index + 1
        yield item
