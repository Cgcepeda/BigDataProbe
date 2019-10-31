Big Data Points:

Este repositorio contiene 3 archivos llamado ChessMovement.py, PolinomialClass.py y BigData.py.

El archivo ChessMovement.py resuelve el ejercicio del movimiento del caballo de ajedrez y la reina. Si se desea mirar el movimiento del caballo ingresar "Caballo". En caso contrario, ingresar "Reina". El ejercicio se encuentra realizado para cualquier matriz cuadrada. Por ende, solo se debe ingresar el tamaño de una dimensión y se asume la restante de igual valor. El tamaño por defecto de un tablero de ajedrez es 8. Lo cual implica 64 posiciones. 

El archivo PolinomialClass.py ejecuta la clase polinomio descrita. Para llamar a la clase se deben ingresar los coeficientes de menor a mayor del polinomio. Por ejemplo, para obtener el polinomio 1+2x+3x^2 se debe ingresar [1,2,3] como lista.

Las funciones presentes por la clase Polinomio son:
-addition: Para realizar la suma de 2 polinomios. Se debe ingresar otro polinomio para su ejecución.
-substraction: Para realizar la resta de 2 polinomios. Se debe ingresar otro polinomio para su ejecución.
-multiplication: Para realizar la multiplicación de 2 polinomios. Se debe ingresar otro polinomio para su ejecución.
-scalarproduct: Para multiplicar un polinomio por una constante. Se debe ingresar la constante a multiplicar.
-evaluate: Para evaluar una constante enel polinomio. Se debe ingresar la constante a evaluar.

Finalmente, el archivo BigData.py resuelve el problema de Spark implementando PandasDataFrames como un bonus, el ejercicio pedido implementando spark se encuentra en el siguiente Notebook:
https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/990941138329084/2679426951326563/3385015214621116/latest.html
