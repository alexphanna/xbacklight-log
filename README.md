# xbacklight-log
According to the [Weber-Fechner law](https://en.wikipedia.org/wiki/Weber%E2%80%93Fechner_law) human perception of brightness is logarithmic not linear. By default xbacklight is linear, so adjustment of brightness seems very uneven. xbacklight-log fixes this by wrapping xbacklight and using two seperate brightness values. The figure below shows the logarithmic dimming curve (log<sub>10</sub>x).

![](graph.png)

## Resources
- [@konradstrack](https://github.com/konradstrack)'s [blog](https://konradstrack.ninja/blog/changing-screen-brightness-in-accordance-with-human-perception/)
