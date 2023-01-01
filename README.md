# createdictionarysqlinjection
Create a sql injection dictionary for use in burpsuite intruder. 

The idea of this script is that having 4 files.

1. Union , For the start of the sql injection
2. Query, Queries you want to do
3. comments, end of sql injection
4. spaces, how do you want the spaces to be filled in

Make a dictionary which returns all the possible combinations, it will also make urlencode, doubleurlencode and permutations of all the characters between uppercase and lowercase.

This dictionary and depending on how you fill in the previous files, will result in a txt file, which you can use both in a fuzzing program and in burpsuite intruder. Depending on the response if it is 200 or another code, or seeing the size of the response, you will be able to see which is the sql that matches in each case.

This dictionary is designed to bypass the waf .. but it could be used for any type of sqlinjection, but keep in mind that it will generate a dictionary according to what you have added in the files.

Union + query + comment


La idea de este script es que teniendo 4 archivos.

1. Union , Para el inicio del sql injection
2. Consulta, Consultas que quieres hacer
3. comentarios, final de la sql injection
4. espacios, como quieres que se rellenen los espacios

Realice un diccionario el cual te devuelva todas las combinaciones posibles, además realizará urlencode, doubleurlencode y permutaciones de todas los caracteres entre mayúsculas y minúsculas.

Este dicccionario y según como rellenes los archivos anteriores, te dará como resultado un archivo txt, el cual podrás usar tanto en un programa de fuzzing como en burpsuite intruder. Según la respuesta si es 200 u otro código, o viendo el tamaño de la respuesta, podrás ver cual es el sql que combiene en cada caso. 

Este diccionario está pensado para bypassear el waf .. pero se podría utilizar para cualquier tipo de sqlinjection, eso si, tenga en cuenta que generará un diccionario según lo que hayas añadido en los archivos.

Union + consulta + comentario
