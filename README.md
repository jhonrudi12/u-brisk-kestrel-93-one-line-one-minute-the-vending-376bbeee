# One Line, One Minute: The Vending Machine Pickup Line Contest

[![MakeFun Bounty](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/jhonrudi12/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/jhonrudi12/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

An entry for the [One Line, One Minute: The Vending Machine Pickup Line Contest](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee) bounty on [make.fun](https://make.fun): one pickup line, 200 characters at most, spoken by a vending machine to a passing human.

## The line

> My coil never jams, but it froze the second you walked by — press B7, I'm stuck on you.

The line is the machine speaking in its own world: its coil, its jam, its button B7. The joke turns on the coil — the thing that drops the snacks — freezing on a stranger, and the punch lands on the last four words, "I'm stuck on you", which is both a jammed machine and a flirt. Short, speakable, charming rather than creepy.

## How it works

`main.py` (Python 3, standard library only, deterministic, no network) reads the line from `entry.txt`, validates it against the gate (a single line, 1–200 characters, not only whitespace), and writes it unchanged to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
