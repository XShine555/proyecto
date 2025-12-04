-- Horarios DAM2B - Diciembre 2025
-- Base de datos: proyecto

USE `proyecto`;

-- ============================================
-- 1. INSERTAR CLASES
-- ============================================

INSERT INTO `CLASSES` (`nom`, `planta`) VALUES
('A01', 0),
('A02', 0),
('A03', 0),
('A04', 0),
('A11', 1),
('A12', 1),
('A13', 1),
('A14', 1),
('A15', 1),
('A16', 1),
('A17', 1);

-- ============================================
-- 2. INSERTAR ASIGNATURAS
-- ============================================

-- Asignaturas en A01
INSERT INTO `ASSIGNATURES` (`nom`, `classe_id`) VALUES
('OPT Cloud', (SELECT id FROM CLASSES WHERE nom = 'A01')),
('Accés a dades', (SELECT id FROM CLASSES WHERE nom = 'A01')),
('TUT', (SELECT id FROM CLASSES WHERE nom = 'A01'));

-- Asignaturas en A02
INSERT INTO `ASSIGNATURES` (`nom`, `classe_id`) VALUES
('OPT Big Data', (SELECT id FROM CLASSES WHERE nom = 'A02')),
('Programació de serveis i processos', (SELECT id FROM CLASSES WHERE nom = 'A02'));

-- Asignaturas en A03
INSERT INTO `ASSIGNATURES` (`nom`, `classe_id`) VALUES
('OPT Machine Learning', (SELECT id FROM CLASSES WHERE nom = 'A03'));

-- Asignaturas en A04
INSERT INTO `ASSIGNATURES` (`nom`, `classe_id`) VALUES
('OPT IoT', (SELECT id FROM CLASSES WHERE nom = 'A04')),
('Interfícies + Programació MM + SOST', (SELECT id FROM CLASSES WHERE nom = 'A04')),
('IPOII', (SELECT id FROM CLASSES WHERE nom = 'A04'));

-- Asignaturas en A11
INSERT INTO `ASSIGNATURES` (`nom`, `classe_id`) VALUES
('OPT IA', (SELECT id FROM CLASSES WHERE nom = 'A11'));

-- ============================================
-- 3. INSERTAR HORARIOS DE DICIEMBRE 2025
-- ============================================

-- Variables para facilitar las referencias (usar en queries posteriores)
-- SET @opt_cloud_id = (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Cloud');
-- ...etc

-- SEMANA 1: 1-5 Diciembre 2025
-- Lunes 1 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-01 16:00:00', '2025-12-01 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-01 18:15:00', '2025-12-01 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'IPOII')),
('2025-12-01 16:10:00', '2025-12-01 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Cloud'));

-- Martes 2 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-02 16:00:00', '2025-12-02 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-02 18:15:00', '2025-12-02 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-02 16:10:00', '2025-12-02 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Big Data'));

-- Miércoles 3 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-03 16:00:00', '2025-12-03 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Accés a dades')),
('2025-12-03 18:15:00', '2025-12-03 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Accés a dades')),
('2025-12-03 16:10:00', '2025-12-03 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Machine Learning')),
('2025-12-03 16:10:00', '2025-12-03 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IoT'));

-- Jueves 4 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-04 16:00:00', '2025-12-04 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Programació de serveis i processos')),
('2025-12-04 18:15:00', '2025-12-04 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Programació de serveis i processos')),
('2025-12-04 20:00:00', '2025-12-04 21:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'TUT')),
('2025-12-04 16:10:00', '2025-12-04 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IA'));

-- Viernes 5 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-05 16:00:00', '2025-12-05 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-05 18:15:00', '2025-12-05 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-05 16:10:00', '2025-12-05 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Cloud')),
('2025-12-05 16:10:00', '2025-12-05 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Big Data')),
('2025-12-05 16:10:00', '2025-12-05 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Machine Learning')),
('2025-12-05 16:10:00', '2025-12-05 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IoT')),
('2025-12-05 16:10:00', '2025-12-05 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IA'));

-- SEMANA 2: 8-12 Diciembre 2025
-- Lunes 8 Diciembre (FESTIVO: Inmaculada Concepción - puede que no haya clase)
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-08 16:00:00', '2025-12-08 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-08 18:15:00', '2025-12-08 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'IPOII')),
('2025-12-08 16:10:00', '2025-12-08 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Cloud'));

-- Martes 9 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-09 16:00:00', '2025-12-09 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-09 18:15:00', '2025-12-09 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-09 16:10:00', '2025-12-09 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Big Data'));

-- Miércoles 10 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-10 16:00:00', '2025-12-10 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Accés a dades')),
('2025-12-10 18:15:00', '2025-12-10 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Accés a dades')),
('2025-12-10 16:10:00', '2025-12-10 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Machine Learning')),
('2025-12-10 16:10:00', '2025-12-10 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IoT'));

-- Jueves 11 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-11 16:00:00', '2025-12-11 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Programació de serveis i processos')),
('2025-12-11 18:15:00', '2025-12-11 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Programació de serveis i processos')),
('2025-12-11 20:00:00', '2025-12-11 21:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'TUT')),
('2025-12-11 16:10:00', '2025-12-11 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IA'));

-- Viernes 12 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-12 16:00:00', '2025-12-12 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-12 18:15:00', '2025-12-12 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-12 16:10:00', '2025-12-12 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Cloud')),
('2025-12-12 16:10:00', '2025-12-12 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Big Data')),
('2025-12-12 16:10:00', '2025-12-12 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Machine Learning')),
('2025-12-12 16:10:00', '2025-12-12 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IoT')),
('2025-12-12 16:10:00', '2025-12-12 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IA'));

-- SEMANA 3: 15-19 Diciembre 2025
-- Lunes 15 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-15 16:00:00', '2025-12-15 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-15 18:15:00', '2025-12-15 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'IPOII')),
('2025-12-15 16:10:00', '2025-12-15 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Cloud'));

-- Martes 16 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-16 16:00:00', '2025-12-16 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-16 18:15:00', '2025-12-16 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-16 16:10:00', '2025-12-16 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Big Data'));

-- Miércoles 17 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-17 16:00:00', '2025-12-17 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Accés a dades')),
('2025-12-17 18:15:00', '2025-12-17 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Accés a dades')),
('2025-12-17 16:10:00', '2025-12-17 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Machine Learning')),
('2025-12-17 16:10:00', '2025-12-17 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IoT'));

-- Jueves 18 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-18 16:00:00', '2025-12-18 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Programació de serveis i processos')),
('2025-12-18 18:15:00', '2025-12-18 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Programació de serveis i processos')),
('2025-12-18 20:00:00', '2025-12-18 21:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'TUT')),
('2025-12-18 16:10:00', '2025-12-18 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IA'));

-- Viernes 19 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-19 16:00:00', '2025-12-19 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-19 18:15:00', '2025-12-19 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-19 16:10:00', '2025-12-19 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Cloud')),
('2025-12-19 16:10:00', '2025-12-19 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Big Data')),
('2025-12-19 16:10:00', '2025-12-19 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Machine Learning')),
('2025-12-19 16:10:00', '2025-12-19 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IoT')),
('2025-12-19 16:10:00', '2025-12-19 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IA'));

-- SEMANA 4: 22-26 Diciembre 2025
-- Lunes 22 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-22 16:00:00', '2025-12-22 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-22 18:15:00', '2025-12-22 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'IPOII')),
('2025-12-22 16:10:00', '2025-12-22 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Cloud'));

-- Martes 23 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-23 16:00:00', '2025-12-23 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-23 18:15:00', '2025-12-23 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-23 16:10:00', '2025-12-23 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Big Data'));

-- Miércoles 24 Diciembre (Nochebuena - probablemente no haya clase)
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-24 16:00:00', '2025-12-24 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Accés a dades')),
('2025-12-24 18:15:00', '2025-12-24 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Accés a dades')),
('2025-12-24 16:10:00', '2025-12-24 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Machine Learning')),
('2025-12-24 16:10:00', '2025-12-24 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IoT'));

-- Jueves 25 Diciembre (Navidad - FESTIVO)
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-25 16:00:00', '2025-12-25 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Programació de serveis i processos')),
('2025-12-25 18:15:00', '2025-12-25 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Programació de serveis i processos')),
('2025-12-25 20:00:00', '2025-12-25 21:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'TUT')),
('2025-12-25 16:10:00', '2025-12-25 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IA'));

-- Viernes 26 Diciembre (San Esteban - FESTIVO en Cataluña)
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-26 16:00:00', '2025-12-26 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-26 18:15:00', '2025-12-26 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-26 16:10:00', '2025-12-26 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Cloud')),
('2025-12-26 16:10:00', '2025-12-26 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Big Data')),
('2025-12-26 16:10:00', '2025-12-26 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Machine Learning')),
('2025-12-26 16:10:00', '2025-12-26 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IoT')),
('2025-12-26 16:10:00', '2025-12-26 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IA'));

-- SEMANA 5: 29-31 Diciembre 2025
-- Lunes 29 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-29 16:00:00', '2025-12-29 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-29 18:15:00', '2025-12-29 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'IPOII')),
('2025-12-29 16:10:00', '2025-12-29 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Cloud'));

-- Martes 30 Diciembre
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-30 16:00:00', '2025-12-30 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-30 18:15:00', '2025-12-30 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST')),
('2025-12-30 16:10:00', '2025-12-30 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Big Data'));

-- Miércoles 31 Diciembre (Nochevieja - probablemente no haya clase)
INSERT INTO `HORARIS` (`timestamp_inici`, `timestamp_fi`, `assignatura_id`) VALUES
('2025-12-31 16:00:00', '2025-12-31 17:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Accés a dades')),
('2025-12-31 18:15:00', '2025-12-31 20:00:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'Accés a dades')),
('2025-12-31 16:10:00', '2025-12-31 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Machine Learning')),
('2025-12-31 16:10:00', '2025-12-31 17:45:00', (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT IoT'));

-- Dispositivo
INSERT INTO `DISPOSITIUS` (`device_id`, `actiu`, `classe_id`) VALUES
    ('78EECC20691C', '1', (SELECT id FROM CLASSES WHERE nom = 'A01')), -- A01
    ('A02', '1', (SELECT id FROM CLASSES WHERE nom = 'A02')), -- A02
    ('A03', '1', (SELECT id FROM CLASSES WHERE nom = 'A03')), -- A03
    ('A04', '1', (SELECT id FROM CLASSES WHERE nom = 'A04')), -- A04
    ('A11', '1', (SELECT id FROM CLASSES WHERE nom = 'A11')); -- A11
-- Usuarios
INSERT INTO `USUARIS` (`nom`, `cognoms`, `tipus`, `targeta_rfid`, `actiu`) VALUES
    ('Sergio', 'Herruzo', 'professor', '03C7EA0E', '1'), -- Tarjeta azul
    ('Ian', 'Ordoñez', 'alumne', '83848F18', '1'), -- Tarjeta blanca
    ('Carlos', 'Sánchez', 'admin', '93C1870D', '1'); -- Tarjeta azul_

-- Assignaturas a las que están inscritos los alumnos
INSERT INTO `USUARIS_ASSIGNATURES` (`usuari_id`, `assignatura_id`) VALUES
    ((SELECT id FROM USUARIS WHERE nom = 'Sergio' AND cognoms = 'Herruzo'), (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Cloud')),
    ((SELECT id FROM USUARIS WHERE nom = 'Sergio' AND cognoms = 'Herruzo'), (SELECT id FROM ASSIGNATURES WHERE nom = 'Accés a dades')),
    ((SELECT id FROM USUARIS WHERE nom = 'Sergio' AND cognoms = 'Herruzo'), (SELECT id FROM ASSIGNATURES WHERE nom = 'TUT')),
    ((SELECT id FROM USUARIS WHERE nom = 'Sergio' AND cognoms = 'Herruzo'), (SELECT id FROM ASSIGNATURES WHERE nom = 'Programació de serveis i processos')),
    ((SELECT id FROM USUARIS WHERE nom = 'Sergio' AND cognoms = 'Herruzo'), (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST'));

INSERT INTO `USUARIS_ASSIGNATURES` (`usuari_id`, `assignatura_id`) VALUES
    ((SELECT id FROM USUARIS WHERE nom = 'Ian' AND cognoms = 'Ordoñez'), (SELECT id FROM ASSIGNATURES WHERE nom = 'OPT Cloud')),
    ((SELECT id FROM USUARIS WHERE nom = 'Ian' AND cognoms = 'Ordoñez'), (SELECT id FROM ASSIGNATURES WHERE nom = 'Accés a dades')),
    ((SELECT id FROM USUARIS WHERE nom = 'Ian' AND cognoms = 'Ordoñez'), (SELECT id FROM ASSIGNATURES WHERE nom = 'Programació de serveis i processos')),
    ((SELECT id FROM USUARIS WHERE nom = 'Ian' AND cognoms = 'Ordoñez'), (SELECT id FROM ASSIGNATURES WHERE nom = 'Interfícies + Programació MM + SOST'));