"""Self-contained Morse decode worker for the multiprocessing part of the notebook.

Why a separate module? `ProcessPoolExecutor` on macOS/Windows uses the *spawn*
start method: each worker re-imports the target by module path. Functions defined
inside a Jupyter notebook live in an interactive ``__main__`` that workers cannot
import, so they fail to unpickle. Putting the worker in a real .py file fixes that.
Keep it dependency-free and picklable.
"""

_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
}
_INV = {v: k for k, v in _MORSE.items()}


def decode_stream(bits):
    """A 0/1 time-unit sample stream -> decoded text. Threshold-based, so it
    tolerates moderate clock drift (a dash that arrives as 3-4 units, etc.)."""
    # run-length encode
    runs = []
    for b in bits:
        if runs and runs[-1][0] == b:
            runs[-1][1] += 1
        else:
            runs.append([b, 1])
    symbols = []
    for level, n in runs:
        if level == 1:
            symbols.append('.' if n < 2 else '-')   # midpoint of 1 and 3
        else:
            if n < 2:
                pass                                  # intra-char gap
            elif n < 5:
                symbols.append(' ')                   # letter gap (midpoint 3..7)
            else:
                symbols.append(' / ')                 # word gap
    morse = ''.join(symbols)
    words = morse.split(' / ')
    return ' '.join(
        ''.join(_INV[c] for c in w.split(' ') if c) for w in words
    )
