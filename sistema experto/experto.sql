-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-10-2021 a las 06:26:37
-- Versión del servidor: 10.4.19-MariaDB
-- Versión de PHP: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `experto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `enfermedades`
--

CREATE TABLE `enfermedades` (
  `IdEnfermedad` int(9) NOT NULL,
  `Nombre` varchar(30) COLLATE utf8_spanish2_ci NOT NULL,
  `Descripción` text COLLATE utf8_spanish2_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `enfermedades`
--

INSERT INTO `enfermedades` (`IdEnfermedad`, `Nombre`, `Descripción`) VALUES
(1, 'Bronquitis aguda', 'La bronquitis aguda ocurre cuando se inflaman las vías respiratorias de los pulmones y producen mucosidad en los pulmones. Eso es lo que lo hace toser. La bronquitis aguda, con frecuencia llamada resfriado de pecho, dura menos de 3 semanas y es el tipo más común de bronquitis.'),
(2, 'Resfriado común', 'Los resfriados son una de las razones más frecuentes de ausencias escolares y laborales. Cada año, los adultos tienen un promedio de 2 a 3 resfriados y los niños tienen aún más.'),
(3, 'Infección de oído', 'Existen distintos tipos de infecciones de oído. La infección del oído medio (otitis media aguda) es una infección en el oído medio.\r\n\r\nOtra afección que afecta el oído medio se llama otitis media exudativa. Se presenta cuando se acumula líquido en el oído medio sin estar infectado y sin provocar fiebre, dolor de oído o acumulación de pus en el oído medio.'),
(4, 'Sinusitis', 'inflamación de los senos del cráneo situados en la frente sobre los dos lados de la nariz, que es debida a una infección de las fosas nasales o de los alvéolos dentarios; suele producir obstrucción nasal y dolor de cabeza.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sintomas`
--

CREATE TABLE `sintomas` (
  `IdSintoma` int(9) NOT NULL,
  `Sintoma` varchar(50) COLLATE utf8_spanish2_ci NOT NULL,
  `IdEnfermedad` int(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `sintomas`
--

INSERT INTO `sintomas` (`IdSintoma`, `Sintoma`, `IdEnfermedad`) VALUES
(1, 'Tos con o sin mucosidad', 1),
(2, 'Dolor en el pecho', 1),
(3, 'Cansancio (fatiga)', 1),
(4, 'Dolor de cabeza leve', 1),
(5, 'Dolores corporales leves', 1),
(7, 'Congestión nasal', 2),
(8, 'Estornudos', 2),
(9, 'Moqueo', 2),
(10, 'Dolor de garganta', 2),
(11, 'Goteo de mucosidad en la garganta (goteo posnasal)', 2),
(12, 'Lagrimeo', 2),
(15, 'Dolor de oído', 3),
(16, 'Fiebre', 3),
(17, 'Nerviosismo o irritabilidad', 3),
(18, 'Frotarse o jalarse una oreja', 3),
(19, 'Dificultad para dormir', 3),
(28, 'Moqueo', 4),
(29, 'Congestión nasal', 4),
(30, 'Dolor o presión en la cara', 4),
(31, 'Dolor de cabeza', 4),
(32, 'Goteo de mucosidad en la garganta (goteo posnasal)', 4),
(33, 'Dolor de garganta', 4),
(34, 'Tos', 4),
(35, 'Mal aliento', 4);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `enfermedades`
--
ALTER TABLE `enfermedades`
  ADD PRIMARY KEY (`IdEnfermedad`);

--
-- Indices de la tabla `sintomas`
--
ALTER TABLE `sintomas`
  ADD PRIMARY KEY (`IdSintoma`),
  ADD KEY `relacion` (`IdEnfermedad`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `enfermedades`
--
ALTER TABLE `enfermedades`
  MODIFY `IdEnfermedad` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `sintomas`
--
ALTER TABLE `sintomas`
  MODIFY `IdSintoma` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `sintomas`
--
ALTER TABLE `sintomas`
  ADD CONSTRAINT `sintomas_ibfk_1` FOREIGN KEY (`IdEnfermedad`) REFERENCES `enfermedades` (`IdEnfermedad`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
