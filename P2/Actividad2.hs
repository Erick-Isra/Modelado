{-
Ejercicio 1:Funcion potencia que recibe como argumentos dos parametros una lista y un valor n.
La funcion potencia elevara a la ‘n’ cada elemento contenido en la lista, para resolver esto
decidi usar listas por comprension.
-}
potencia :: [Int] -> Int -> [Int]
potencia lista n = [x^n | x <- lista]


{-
Ejercicio 2:Funcion que dado un valor ‘k’ calcule e imprime la serie de collatz.
Parac resolver esto fui restando un a n hasta que llegue a 0,
despues solo calcule el modulo de cada elemento para saber si es par o 
impar dependiendo de eso se hace la operacion correspondiente, el caso base es cuando se vuelva 1.
-}
collatz :: Int -> [Int]
collatz 1 = []
collatz n = if n `mod` 2 == 0 then (n `div` 2) : collatz (n `div` 2) else ((3*n)+1) : collatz ((3*n)+1)

{-
Ejercicio 3:Escribe una funcion que reciba una lista L y un entero x.
Esta funcion debera regresar otra lista que contenga a los elementos de L tal que son multiplos de x.
Para resolver esto use listas por comprension checando cada elemento de la lista con modulo x, si es 0 lo
agrega a la lista(es decir es multiplo de x).
-}
multiplos :: [Int] -> Int -> [Int]
multiplos lista n = [x | x <- lista, x `mod` n == 0]


{-
Ejercicio 4:Escribe una funcion que reciba un arreglo de 1 y 0 revueltos 
y simule una compresion de espacio, es decir, la lista debe tener todos los 1’s al inicio
y todos los 0’s al final.Para resolver esto saque la cabeza de la lista y fui viendo si es 1 o 0
si es 1 se agrega la cabeza x a la cabeza de una nueva lista y se llame a la funcion con la cola en la cola de 
la nueva lista, si es 0 llamamos la funcion con la cola de la lista original en la cabeza(por asi decirlo) de la nueva lista
y al final agregamos al elemento x en la cola.
-}
compresion :: [Int] -> [Int]
compresion [] = []
compresion (x:xs) = if x == 1 then x : compresion xs else compresion xs ++ [x]