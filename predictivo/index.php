<?php

require_once('header.php');
?>

<main>

<?php

//CONECTAMOS CON LA BD
require "conexion.php";

//OBTENEMOS EL NÚMERO DEL NODO DENTRO DEL ÁRBOL (PARA SABER QUÉ CAMINO HEMOS TOMADO)

$nodo = 1;
$nodoRepuesto = 0;
$numPregunta = 1;
$proxPregunta = 2;

if(isset($_GET['n'])) {
	$nodo = $_GET["n"];
}

if(isset($_GET['r'])) {
	$nodoRepuesto = $_GET["r"];
}

//------------------------------------------------------
//CALCULAMOS LO SIGUIENTES PASOS A SEGUIR

$nodoSi = $nodo * 2;
$nodoNo = $nodo * 2 + 1;

//-----------------------------------------------------


//HACEMOS LA CONSULTA A LA BD
$consulta = "SELECT texto,pregunta FROM neuronas WHERE nodo = ".$nodo.";";

$texto = '';
$pregunta = true;

if ($resultado = mysqli_query($enlace, $consulta)) {

	if($resultado->num_rows === 0)
    {
        echo 'No existe el nodo';
    }

	else{
		while ($fila = mysqli_fetch_row($resultado)) {
			$texto 	  = $fila[0];
			$pregunta = $fila[1];
		}


		//SI NO ES UNA PREGUNTA ES UN RESULTADO FINAL (predictivo DA UNA RESPUESTA)
?>
		<h2>PREGUNTA <?=$numPregunta?></h2>
<?php
		if($pregunta == 0){
?>
			<div class='contenedorPregunta'>
				<h2>¿Has pensado en <?=$texto ?> ?</h2>
			</div>


			<div class='contenedorRespuestas'>
				<a class='boton' href="respuesta.php?r=1&n=<?=$nodo?>&p=<?=$texto?>&np=<?=$proxPregunta?>">SÍ</a>
				<a class='boton' href="respuesta.php?r=0&n=<?=$nodo?>&p=<?=$texto?>&np=<?=$proxPregunta?>">NO</a>
			</div>
<?php
		}

		//SI ES UNA PREGUNTA, PREGUNTAMOS (SI DUDAMOS, EN EL PARÁMETRO "R" GUARDAMOS LA RAMA ALTERNATIVA, SINO VALE CERO)
		else{
?>
			<div class='contenedorPregunta'>
				<h2>¿Tu personaje es "<?=$texto?>"?</h2>
			</div>

			<div class='contenedorRespuestas'>

				<a class='boton' href="index.php?n=<?=$nodoSi?>&r=0&np=<?=$proxPregunta?>">SÍ</a>
				<a class='boton' href="index.php?n=<?=$nodoNo?>&r=0&np=<?=$proxPregunta?>">NO</a>
				<div class='limpiar'></div>

			</div>
<?php
		}
	}
    mysqli_free_result($resultado);
}

?>

</main>

<br>
<br>
<?php
require_once('footer.php');
?>
