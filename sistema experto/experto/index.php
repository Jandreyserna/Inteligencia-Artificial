<?php
require_once('header.php');

$sintoma = 1;
$enfermedad = 1;
$x = 0;

if(isset($_GET['s']))
 {
	$sintoma = $_GET['s'];
  $enfermedad = $_GET['e'];
}
$consulta = "SELECT * FROM sintomas WHERE IdEnfermedad = ". $enfermedad;

if ($resultado = mysqli_query($enlace, $consulta))
{

	if($resultado->num_rows === 0)
    {
        echo 'No Hay mas enfermedades registradas "Lo Siento" ';
    }

	else{
		while ($fila = mysqli_fetch_row($resultado))
    {
      $sint[$x] =  $fila[1];
      $x++;
		}
  }
}

if( $sintoma == sizeof($sint) + 1 )
{
  $consulta = "SELECT * FROM enfermedades WHERE IdEnfermedad = ". $enfermedad;
  if ( $resultado = mysqli_query( $enlace, $consulta ))
  {
    $datos = mysqli_fetch_row( $resultado );
    $enf['nombre'] = $datos[1];
    $enf['descripcion'] = $datos[2];
  }
?>
    <div class="container">
      

      <div class="contenedorTitulo">
        <h2>Tú enfermedad es: <?=$enf['nombre']?></h2>


      </div>
      <div class='contenedorRespuestas'>

        <h3><?=$enf['descripcion']?></h3>
        <div class='limpiar'></div>

      </div>
    </div>
<?php
}else{
?>
    <div class="container">


      <div class="contenedorTitulo">
        <h2>¿Tienes este sintoma?</h2>
        <h3><?=$sint[$sintoma - 1]?></h3>

      </div>
      <div class='contenedorRespuestas'>

    		<a class='boton' href="index.php?s=<?=$sintoma+1?>&e=<?=$enfermedad?>">SÍ</a>
    		<a class='boton' href="index.php?s=1&e=<?=$enfermedad+1?>">NO</a>
    		<div class='limpiar'></div>

    	</div>
    </div>
<?php
}
require_once 'footer.php';
?>
