# Profiling
 Este repositorio contiene un estudio de profiling sobre diferentes algoritmos de búsqueda de números primos.


 El estudio consiste en comparar el tiempo que tardan en ejecutarse los diferentes algoritmos con la misma carga de trabajo.
 
# Ejecutar la prueba de profiling
```
python -m cProfile main.py
```

### Carga de trabajo, 9999999 números primos
```
         48543302 function calls in 50.661 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   50.661   50.661 main.py:1(<module>)
        1    0.756    0.756   50.660   50.660 main.py:5(main)
        1    0.001    0.001    0.001    0.001 sieve.py:1(<module>)
        1   10.255   10.255   20.695   20.695 sieve.py:35(medium_sieve)
        1    2.488    2.488    6.693    6.693 sieve.py:54(fast_sieve)
        1   21.746   21.746   22.516   22.516 sieve.py:6(slow_sieve)
 17075909    2.885    0.000    2.885    0.000 sieve.py:67(<genexpr>)
        1    0.121    0.121    0.121    0.121 {filter}
     3164    0.007    0.000    0.007    0.000 {math.sqrt}
 29465736    8.320    0.000    8.320    0.000 {method 'add' of 'set' objects}
  1329158    0.157    0.000    0.157    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   669327    3.928    0.000    3.928    0.000 {range}
```
El tiempo total de ejecución de los tres algorítmos ha sido de 50.661 s.

| Algorimo      | Tiempo [s]    |
|:-------------:|:-------------:|
| slow_sieve    | 22.516        |
| medium_sieve  | 20.695        |
| fast_sieve    | 6.693         |


### Carga de trabajo, 999999 números primos

```
         4433511 function calls in 3.142 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.142    3.142 main.py:1(<module>)
        1    0.041    0.041    3.140    3.140 main.py:5(main)
        1    0.002    0.002    0.002    0.002 sieve.py:1(<module>)
        1    0.607    0.607    1.243    1.243 sieve.py:35(medium_sieve)
        1    0.197    0.197    0.456    0.456 sieve.py:54(fast_sieve)
        1    1.351    1.351    1.400    1.400 sieve.py:6(slow_sieve)
  1420296    0.187    0.000    0.187    0.000 sieve.py:67(<genexpr>)
        1    0.011    0.011    0.011    0.011 {filter}
     1001    0.000    0.000    0.000    0.000 {math.sqrt}
  2775208    0.516    0.000    0.516    0.000 {method 'add' of 'set' objects}
   156996    0.012    0.000    0.012    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    80002    0.218    0.000    0.218    0.000 {range}
``` 

El tiempo total de ejecución de los tres algorítmos ha sido de 3.142 s.

| Algorimo      | Tiempo [s]    |
|:-------------:|:-------------:|
| slow_sieve    | 1.400         |
| medium_sieve  | 1.243         |
| fast_sieve    | 0.456         |

### Carga de trabajo, 9999 números primos

```
         35531 function calls in 0.025 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.025    0.025 main.py:1(<module>)
        1    0.000    0.000    0.024    0.024 main.py:5(main)
        1    0.001    0.001    0.001    0.001 sieve.py:1(<module>)
        1    0.005    0.005    0.008    0.008 sieve.py:35(medium_sieve)
        1    0.001    0.001    0.002    0.002 sieve.py:54(fast_sieve)
        1    0.013    0.013    0.014    0.014 sieve.py:6(slow_sieve)
     8512    0.001    0.000    0.001    0.000 sieve.py:67(<genexpr>)
        1    0.000    0.000    0.000    0.000 {filter}
      101    0.000    0.000    0.000    0.000 {math.sqrt}
    23069    0.002    0.000    0.002    0.000 {method 'add' of 'set' objects}
     2458    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1383    0.001    0.000    0.001    0.000 {range}

``` 

El tiempo total de ejecución de los tres algorítmos ha sido de 0.025 s.

| Algorimo      | Tiempo [s]    |
|:-------------:|:-------------:|
| slow_sieve    | 0.014         |
| medium_sieve  | 0.008         |
| fast_sieve    | 0.002         |