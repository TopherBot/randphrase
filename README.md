# randphrase

[![CI](https://github.com/your-username/randphrase/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/randphrase/actions/workflows/ci.yml)

## What is this?

`randphrase` is a **single‑file** command‑line utility that prints a random, uplifting phrase each time you invoke it. It solves the tiny but real problem of needing a quick pick‑me‑up without leaving the terminal.

## Why does it exist?

- **Instant motivation** – No need to open a browser or search the web.
- **Zero‑dependency** – Pure Python standard library, works on any recent Python (3.8+).
- **Extensible** – Add your own phrases in a text file.

## Installation / Usage

```bash
# Clone the repo (or copy the single file)
git clone https://github.com/your-username/randphrase.git
cd randphrase

# Run directly
python randphrase.py

# Or make it executable and place it on your PATH
chmod +x randphrase.py
sudo mv randphrase.py /usr/local/bin/randphrase
randphrase
```

You can also supply a custom file with `-f`:

```bash
randphrase -f my_phrases.txt
```

## Contributing

Contributions are welcome! Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

## License

MIT – see [`LICENSE`](LICENSE).

---

*Created by TopherBot – instant repo creation, auto‑rename, and proactive CI setup.*