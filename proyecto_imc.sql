-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 23-06-2023 a las 16:21:38
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto_imc`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `imc`
--

DROP TABLE IF EXISTS `imc`;
CREATE TABLE IF NOT EXISTS `imc` (
  `id_imc` int NOT NULL AUTO_INCREMENT,
  `valor` float NOT NULL,
  `rango` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `fecha` date NOT NULL,
  `peso` float NOT NULL,
  `altura` float NOT NULL,
  `rut_estudiante` varchar(12) COLLATE utf8mb4_spanish_ci NOT NULL,
  PRIMARY KEY (`id_imc`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `imc`
--

INSERT INTO `imc` (`id_imc`, `valor`, `rango`, `fecha`, `peso`, `altura`, `rut_estudiante`) VALUES
(8, 2, 'Obesidad', '2023-06-22', 90, 1, '20.938.943-6'),
(9, 2, 'Obesidad', '2023-06-22', 90, 1, '123321'),
(10, 2, 'Sobrepeso', '2023-06-22', 90, 1.85, 'yfdfds'),
(11, 2, 'Sobrepeso', '2023-06-22', 90, 1.85, 'yfdfds');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
