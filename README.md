##  ParcialHerramientasComputacionales
El desarrollo se ha realizado en el lenguaje *Python* que es bastante fácil de usar y entender.
Este proyecto tiene como objetivo **automatizar el cobro de almuerzos** de la universidad teniendo en cuenta los diferentes casos que pueden ser brindados a la comunidad estudiantil.

### Desarrollo
Para el desarrollo del problema primero se ha hecho un *procedimiento* llamado **precioFinal** que toma las variantes de:

•	Lis

•	Rol

•	Beca

•	Cedula
***
El *ciclo for* es utilizado para leer **lis** y así leer y calcular cada valor guardado en la* lista.*
A la variante de **pF** se le suma el valor de **precio * unidad** y se agrega el *código a la lista códigos.*

Se colocan los **condicionales** para definir los descuentos otorgados por la universidad que son:

|                |Est. becado|Est. corriente|Profesor|
|---------------|----------------|------------------|-------------|
|Descuento|      50%     |       30%     |    20%    |

El primero nos indica, si es *estudiante y becado* se multiplica el precio **final anterior * 0.5** que es el equivalente al 50% y se imprime el resumen con la información completa de la compra, los datos mostrados son:

•	Rol

•	Cedula

•	Precio final

•	Código de productos

Este mismo procedimiento aplica para los otros 2 casos de *estudiante corriente y profesor.*

---

En un *segundo procedimiento* se realiza toda la *recolección de datos* para poder llevar a cabo el primer procedimiento.

Se pide ingresar *el número* de **cedula** y se guarda el valor ingresado, una vez ingresada se solicita seleccionar el **rol** del cliente, dependiendo del **rol** se realiza *el condicional.*

Se inicia *un condicional* donde si la opción de **estudiante** es escogida se pregunta si es **becado** y así asignar el *descuento correspondiente*, sino el programa asigna la *beca como 0*. 

El programa nos pregunta el *número de productos a cancelar* y lo guarda en la variable **numProductos.**

Inicia un *ciclo while* que se debe repetir hasta que sea igual a **numProductos** y se inicia con el proceso de recolección de datos.

Se agregan unos *Brackets ( [ ] )* para crear una *lista dentro de la lista* y así recolectar la información de las *3 variables* necesarias para calcular el **precioFinal**, estas son:

•	Código

•	Unidades

•	Precio

En cada una pide *ingresar un valor* para ser guardado respectivamente en la lista, se *imprime un espacio de línea y se suma 1* a la variable **i** que ayuda a continuar con el *ciclo while*.

Para terminar, se llama a *el primer procedimiento* para llevar a cabo con todos los datos recogidos y generar el *reporte final*.
