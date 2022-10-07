# Función signif en Pyhton
Esta función te permite expresar cualquier número real con una determinada cantidad de cifras significativas de forma sencilla. Está inspirada en la función `signif` de R que realiza la misma tarea y de la cual hereda su nombre.

La función `signif(x, n)` redondea el valor de su primer argumento `x`, al número de cifras significativas especificado en su segundo argumento `n`. Concretamente realiza la operación `round(x, n-int(math.floor(math.log10(abs(x))))-1)`.
## Nota
El argumento `x` debe ser de tipo `int` o `float`.

## Ejemplo de uso
In[&nbsp;]:
```python
from significant_figures import signif

signif(0.00047923, 2)
```
Out[&nbsp;]:
> 0.00048

## Sobre el autor
[GitHub](https://github.com/luisgn98)

[LinkedIn](https://www.linkedin.com/in/luis-garc%C3%ADa-nnomo-b041b51b3/)