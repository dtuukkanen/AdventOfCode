signals = {}

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        parts = line.split(' -> ')
        signals[parts[1]] = parts[0]

signal_cache = {}

def get_signal(signal):
    if signal in signal_cache:
        return signal_cache[signal]
    
    try:
        value = int(signal)
    except ValueError:
        if signal in signals:
            parts = signals[signal].split()
            if len(parts) == 1:
                value = get_signal(parts[0])
            elif len(parts) == 2 and parts[0] == 'NOT':
                value = ~get_signal(parts[1])
            elif len(parts) == 3:
                if parts[1] == 'AND':
                    value = get_signal(parts[0]) & get_signal(parts[2])
                elif parts[1] == 'OR':
                    value = get_signal(parts[0]) | get_signal(parts[2])
                elif parts[1] == 'LSHIFT':
                    value = get_signal(parts[0]) << get_signal(parts[2])
                elif parts[1] == 'RSHIFT':
                    value = get_signal(parts[0]) >> get_signal(parts[2])
                else:
                    raise ValueError(f"Unknown operation '{parts[1]}'")
            else:
                raise ValueError(f"Invalid instruction '{signals[signal]}'")
        else:
            raise ValueError(f"Signal '{signal}' not found")

    signal_cache[signal] = value
    return value

print(get_signal('a'))