# Profiling
 Comparativa a nivel de profiling de tres generadores de números primos.
 
# Ejecutar la prueba de profiling
```
python -m cProfile main.py
```

## Carga de trabajo 9999999 números primos
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
El tiempo total de ejecución de los tres algorítmos ha sido de 50.661.

| Algorimo      | Tiempo [s]    |
|:-------------:|:-------------:|
| slow_sieve    | 22.516        |
| medium_sieve  | 20.695        |
| fast_sieve    | 6.693         |