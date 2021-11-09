-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 22, 2021 at 06:12 PM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `registration`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE IF NOT EXISTS `admin` (
  `username` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('miniproject', '2021');

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE IF NOT EXISTS `appointment` (
  `username` varchar(15) NOT NULL,
  `hospital` varchar(50) NOT NULL,
  `date_vac` date NOT NULL,
  `dose` varchar(15) NOT NULL,
  `vaccine` varchar(15) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`username`, `hospital`, `date_vac`, `dose`, `vaccine`) VALUES
('anurag', 'Kokilaben Hospital', '2021-05-27', 'Dose 2', 'Covishield'),
('Gamma', 'JJ Hospital', '2021-05-04', 'Dose 1', 'Covishield'),
('nihar100', 'Four Care Hospital', '2021-05-25', 'Dose 2', 'Sputnik-V'),
('nihar1020', 'Seven Hills', '2021-06-23', 'Dose 1', 'Covishield');

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

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE IF NOT EXISTS `details` (
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `contact_no` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `Login` varchar(50) NOT NULL,
  `password` varchar(40) NOT NULL,
  `aadhar_no` varchar(50) NOT NULL,
  `Gender` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`Login`),
  UNIQUE KEY `aadhar_no` (`aadhar_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `details`
--

INSERT INTO `details` (`fname`, `lname`, `contact_no`, `age`, `email`, `Login`, `password`, `aadhar_no`, `Gender`) VALUES
('Dilip', 'Shetty', '9102349167', 69, 'dilip@shetty.com', 'anurag', 'getvaccine2021', '102420484096', 'Male'),
('Anurag', 'Yadav', '9757424500', 20, 'anurag@yadav.com', 'anurag123', 'admin10', '102367891023', 'Male'),
('Nihar', 'Vira', '9869123400', 23, 'nihar@example.com', 'nihar100', 'miniproject', '123490126897', 'Male'),
('Siddharth', 'Yennuwar', '9137258710', 19, 'sid@xie.com', 'sid2021', 'covid_reg**', '102450962032', 'Male');

-- --------------------------------------------------------

--
-- Table structure for table `username`
--

CREATE TABLE IF NOT EXISTS `username` (
  `entry` varchar(15) NOT NULL,
  PRIMARY KEY (`entry`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `vaccine`
--

CREATE TABLE IF NOT EXISTS `vaccine` (
  `vaccines` int(10) DEFAULT NULL,
  `hospital` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`hospital`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vaccine`
--

INSERT INTO `vaccine` (`vaccines`, `hospital`) VALUES
(144, 'Alphine Life Solutions'),
(365, 'Atlantis Hospital'),
(150, 'Fortis Hospital'),
(455, 'Four Care Hospital'),
(245, 'Hinduja Healthcare'),
(388, 'Holy Spirit Hospital'),
(500, 'JJ Hospital'),
(50, 'KEM Hospital'),
(355, 'Lifeline Hospital'),
(100, 'Lilavati Hospital'),
(455, 'Phoenix Hospital'),
(259, 'Saraswati Hospital'),
(550, 'Seven Hills Hospital'),
(475, 'Shatabdi Hospital'),
(344, 'Silverline Hospital'),
(265, 'Suchak Hospital'),
(175, 'Zenith Hospital');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
