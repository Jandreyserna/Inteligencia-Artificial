<?php
require_once('header.php');

?>
<body>
	<main>
<?php
		//CONECTAMOS CON LA BD
		require "conexion.php";

		//RECOGEMOS LA RESPUESTA
		$respuesta = $_GET["r"];
		$nodo = $_GET["n"];
		$nombreAnterior = $_GET["p"];


//----------------------------------------------
function formularioRespuesta($n,$p){
?>
			<div class='contenedorPregunta'>

					<textarea id='nodo' name='nodo' form='formulario' placeholder='nombre' style='display:none;'><?=$n?></textarea>
					<textarea id='nombreAnterior' name='nombreAnterior' form='formulario' placeholder='nombre' style='display:none;'><?=$p?></textarea>
					<h2>¿En quién habías pensado?</h2>
					<textarea id='nombre' name='nombre' form='formulario' placeholder='nombre'></textarea>
					<h2>¿Qué característica tiene este personaje que no tenga <?=$p?>?</h2>
					<textarea id='caracteristicas' name='caracteristicas' form='formulario' placeholder='caracteristicas'></textarea>

					<form action='crear.php' id='formulario' method='POST' >
						<button type='submit' name='ENVIAR'>ENVIAR</button>
					</form>

			</div>
<?php
}
//----------------------------------------------


//SI HA FALLADO
if($respuesta == 0)
{
		formularioRespuesta($nodo,$nombreAnterior);
} else{		//SI HA ACERTADO

		$consulta = "INSERT INTO partida (personaje,acierto) VALUES('".$nombreAnterior."',TRUE);";
		mysqli_query($enlace, $consulta); //GUARDAMOS EL ACIERTO EN EL LOG DE LA BD (TABLA PARTIDA)

?>
	<h2>¡FUE UN PLACER ADIVINAR!</h2>
<?php
}
?>
</main>

<br>
<br>
<?php
require_once('footer.php');
?>
