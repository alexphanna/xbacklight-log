# xbacklight-log
According to the [Weber-Fechner law](https://en.wikipedia.org/wiki/Weber%E2%80%93Fechner_law) human perception of brightness is logarithmic not linear. By default xbacklight is linear, so adjustment of brightness seems very uneven. xbacklight-log fixes this by wrapping xbacklight and using two seperate brightness values, measured and perceived.

## Math

$$\hat{\text{perceived brightness}} = {\frac{\log_{10}(\text{measured brightness}) + 2}{2}}$$

## Other Helpful Resources
- [@konradstrack](https://github.com/konradstrack)'s [blog](https://konradstrack.ninja/blog/changing-screen-brightness-in-accordance-with-human-perception/)
- [@ericmurphyxyz](https://github.com/ericmurphyxyz)'s [video](https://youtu.be/pGOaSS8nEQA?si=UsH7o5s1bvsRl6RI)
