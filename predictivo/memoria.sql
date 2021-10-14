-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-10-2021 a las 18:24:55
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
-- Base de datos: `memoria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `neuronas`
--

CREATE TABLE `neuronas` (
  `nodo` int(9) NOT NULL,
  `texto` varchar(50) COLLATE utf8_spanish2_ci NOT NULL,
  `pregunta` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `neuronas`
--

INSERT INTO `neuronas` (`nodo`, `texto`, `pregunta`) VALUES
(1, 'animal', 1),
(2, 'da leche', 1),
(3, 'cantante', 1),
(4, 'vaca', 0),
(5, 'es un felino', 1),
(6, 'Rihanna', 0),
(7, 'anime', 1),
(10, 'Rey de la selva', 1),
(11, 'come madera', 1),
(14, 'GOKU', 0),
(15, 'Cartoon Network', 1),
(20, 'leon', 0),
(21, 'el felino mas rápido', 1),
(22, 'castor', 0),
(23, 'nopturno', 1),
(30, 'sooby Doo', 0),
(31, 'German Garmendia', 0),
(42, 'guepardo', 0),
(43, 'domestico', 1),
(46, 'come Ratones', 1),
(47, 'caballo', 0),
(86, 'gato', 0),
(87, 'tigre', 0),
(92, 'Buho', 0),
(93, 'murcielago', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `neuronas`
--
ALTER TABLE `neuronas`
  ADD PRIMARY KEY (`nodo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
