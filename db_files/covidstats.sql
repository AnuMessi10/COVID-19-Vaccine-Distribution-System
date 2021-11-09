-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 13, 2021 at 12:12 PM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `covidstats`
--

-- --------------------------------------------------------

--
-- Table structure for table `covidstats`
--

CREATE TABLE IF NOT EXISTS `covidstats` (
  `Total_doses` int(50) NOT NULL,
  `dose_1` int(50) NOT NULL,
  `dose_2` int(50) NOT NULL,
  `male_vaccinated` int(50) NOT NULL,
  `female_vaccinated` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `covidstats`
--

INSERT INTO `covidstats` (`Total_doses`, `dose_1`, `dose_2`, `male_vaccinated`, `female_vaccinated`) VALUES
(150000, 90000, 60000, 65000, 85000),
(150000, 90000, 60000, 65000, 85000);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
