# Proyecto de Compiladores

## Objetivo

Elaborar un traductor básico en Python, que pueda recibir una entrada de cadenas y elaborar un análisis léxico y sintáctico para entregar una salida de acorde a una gramática elaborada.

## Indicaciones

1. Recibir una entrada, ya sea a través de un txt o dentro del programa tener las cadenas, la última cadena debe reconocer el `$` que ha llegado a su fin. Haga uso de bibliotecas como `PLY` o `LARK`, `RE` entre otras más.

2. Mostrar una salida que contenga un cuadro con el detalle del analizador léxico y sintáctico.

   - Analizador Léxico:

     - Línea del token encontrado.
     - Tipo de token.
     - Valor o elemento de operación.
     - Otros que considere importante de mostrar.

   - Analizador Sintáctico:

     - Genera la salida de la operación.
     - Construir el árbol (esto es opcional y solo si logra mostrarlo de forma clara). `LARK`

3. Elaborar un informe final con los siguientes elementos:

   - Detalle de los tokens, patrones y lexemas elaborados para el proyecto.

   - Detalle de las reglas de producción y la gramática elaborada para el proyecto.

   - Detalle del nombre de las funciones (reglas semánticas) utilizadas para el proyecto.

   - Capturas del programa en ejecución.

   - Hoja de desempeño de los integrantes de grupo con él % de trabajo.

   - Bibliografía base utilizada.

4. Seleccione de los proyectos descritos únicamente uno por grupo.

5. Fecha de presentación será el próximo sábado 29 de abril.

6. Se habilitará un link de subida del informe para ese sábado, no del código, porque será lo que va a explicar y mostrar en día de la presentación.

7. La presentación será según el horario asignado y tendrá 25 minutos para explicarlo, en este día solo será entre el grupo y el docente la demostración.

8. La(s) persona(s) que exponga(n) podrá(n) ser elegida(s) por el grupo, pero todos deben dar su punto de vista sobre el proyecto.

## Proyecto seleccionado: Convertidor de números

Cadenas de números enteros con base decimal (base 10) seguidas de un identificador de conversión de destino los cuales pueden ser:

1. Hexadecimal.
2. Octal.
3. Binario.
4. Romano.
5. Alternativo (uno inventado o agregado por el grupo).
6. Aleatorio (toma uno de los destinos de forma aleatoria).

### Ejemplo:

    Cadena: 525Romano => Salida: DXXV || Cadena: 525Hexadecimal => Salida: 20D || Cadena: 525Octal => Salida: 1015 || Cadena: 525Alternativo => Salida: “la salida de conversión” || Cadena: 525Aleatorio => Salida: 20D || Cadena: 525Aleatorio => Salida: DXXV

    Tokens: serian identificar el destino.
    Funciones: Convertir según el destino
    Resultado: según la salida del ejemplo.

Recuerde que esto es un ejemplo de una línea del txt, el grupo tiene la libertar de trabajar con diferentes nombres y formas de identificar los elementos.
