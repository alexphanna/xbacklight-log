# Brightness
According to the [Weber-Fechner law](https://en.wikipedia.org/wiki/Weber%E2%80%93Fechner_law) human perception of brightness is logarithmic. By default xbacklight is linear and not smooth. [brightness.py](brightness.py) wraps xbacklight and uses the logarithmic dimming curve in the figure below.

![grpah](graph.png)

## Resources
- [@konradstrack](https://github.com/konradstrack)'s [blog](https://konradstrack.ninja/blog/changing-screen-brightness-in-accordance-with-human-perception/)
