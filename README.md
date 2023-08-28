# xbacklight-log
According to the [Weber-Fechner law](https://en.wikipedia.org/wiki/Weber%E2%80%93Fechner_law) human perception of brightness is logarithmic not linear. By default xbacklight is linear, so adjustment of brightness seems very uneven. xbacklight-log fixes this by wrapping xbacklight and using two seperate brightness values, measured and perceived.

## Math

$x =$ measured  brightness

$y =$ perceived brightness

$$y = {\frac{\log_{10} (\frac{x}{100}) + 2}{2} \times 100}$$

## Resources
- [@konradstrack](https://github.com/konradstrack)'s [blog](https://konradstrack.ninja/blog/changing-screen-brightness-in-accordance-with-human-perception/)
