# Signif function in Pyhton
This function allows you to express any real number with a specified number of significant figures easily. It is inspired by the `signif` function from R, which performs the same task and from which it inherits its name.

The function `signif(x, n)` rounds the value of its first argument, `x`, to the number of significant figures specified in its second argument, `n`. Specifically, it performs the operation `round(x, n-int(math.floor(math.log10(abs(x))))-1)`.

The argument `x` must be of type `int` or `float`, while the argument `n` must be of type `int`.

## Installation
```python
pip install significant-figures==0.0.4
```
[Library on PyPI](https://pypi.org/project/significant-figures/0.0.3/)

## Usage example
In[&nbsp;]:
```python
from significant_figures import signif

signif(0.00047923, 2)
```
Out[&nbsp;]:
> 0.00048

## About the author
[GitHub](https://github.com/luisgn98)

[LinkedIn](https://www.linkedin.com/in/luis-garc%C3%ADa-nnomo-b041b51b3/)
