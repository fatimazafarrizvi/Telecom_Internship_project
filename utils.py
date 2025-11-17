def status(val, invert=False):
    if invert:  # RLF: lower is better
        return "Improved" if val < 0 else "Degraded"
    return "Improved" if val > 0 else "Degraded"
