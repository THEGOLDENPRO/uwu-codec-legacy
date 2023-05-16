<div align="center">

  # 🐱 The UwU Codec
  
  <sub>Have you ever wanted to encode your shit into UwU Bytes, well now you can.</sub>
  
  [![Pypi Badge](https://img.shields.io/pypi/v/uwu-codec?style=flat)](https://pypi.org/project/devgoldyutils "We're on pypi!")
  [![Python Badge](https://img.shields.io/pypi/pyversions/uwu-codec?style=flat)](https://pypi.org/project/devgoldyutils "Supported python versions.")
  
</div>

> #### ❗ *btw this project is kind of a work in progress so don't expect much but if you want something added just open an issue.*

## 🛠 *Install/Usage*
1. **Install package from pypi.**
```sh
# Windows/Linux

pip install uwu-codec
```

2. **Now create a script.**
Here's a simple example.

First you're going to want to import this crap and run the enable function which should allow you to use the uwu encoder and decoder on strings.
```python
import uwu_codec
uwu_codec.enable()

data = "What have I done!"

uwu_bytes = data.encode("uwu")
print(f"UwU Bytes: {uwu_bytes}")

string = uwu_bytes.decode("uwu")
print(f"String: {string}")
```
Then tadaaaa now you have this fucking mess.

**``RESULT:``**
```python
UwU Bytes: b'UwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwUOwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwOUwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwUOwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwOOwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwOOwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwOUwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwUOwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwOUwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwUOwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwOUwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwUOwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwOOwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwOUwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwUOwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwOUwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwUUwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwU'
String: What have I done!
```

> ### Why did I make this 💀