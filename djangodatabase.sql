-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 23, 2021 at 10:36 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `djangodatabase`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add orders', 7, 'add_orders'),
(26, 'Can change orders', 7, 'change_orders'),
(27, 'Can delete orders', 7, 'delete_orders'),
(28, 'Can view orders', 7, 'view_orders'),
(29, 'Can add packs', 8, 'add_packs'),
(30, 'Can change packs', 8, 'change_packs'),
(31, 'Can delete packs', 8, 'delete_packs'),
(32, 'Can view packs', 8, 'view_packs'),
(33, 'Can add ticket', 9, 'add_ticket'),
(34, 'Can change ticket', 9, 'change_ticket'),
(35, 'Can delete ticket', 9, 'delete_ticket'),
(36, 'Can view ticket', 9, 'view_ticket'),
(37, 'Can add ticketpm', 10, 'add_ticketpm'),
(38, 'Can change ticketpm', 10, 'change_ticketpm'),
(39, 'Can delete ticketpm', 10, 'delete_ticketpm'),
(40, 'Can view ticketpm', 10, 'view_ticketpm');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(7, 'paneluser', 'orders'),
(8, 'paneluser', 'packs'),
(9, 'paneluser', 'ticket'),
(10, 'paneluser', 'ticketpm'),
(6, 'paneluser', 'user'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-11-23 09:36:38.162586'),
(2, 'contenttypes', '0002_remove_content_type_name', '2021-11-23 09:36:38.266948'),
(3, 'auth', '0001_initial', '2021-11-23 09:36:38.437493'),
(4, 'auth', '0002_alter_permission_name_max_length', '2021-11-23 09:36:39.285133'),
(5, 'auth', '0003_alter_user_email_max_length', '2021-11-23 09:36:39.294110'),
(6, 'auth', '0004_alter_user_username_opts', '2021-11-23 09:36:39.305081'),
(7, 'auth', '0005_alter_user_last_login_null', '2021-11-23 09:36:39.318048'),
(8, 'auth', '0006_require_contenttypes_0002', '2021-11-23 09:36:39.339988'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2021-11-23 09:36:39.349962'),
(10, 'auth', '0008_alter_user_username_max_length', '2021-11-23 09:36:39.359942'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2021-11-23 09:36:39.369909'),
(12, 'auth', '0010_alter_group_name_max_length', '2021-11-23 09:36:39.458669'),
(13, 'auth', '0011_update_proxy_permissions', '2021-11-23 09:36:39.467647'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2021-11-23 09:36:39.476622'),
(15, 'paneluser', '0001_initial', '2021-11-23 09:36:40.113918'),
(16, 'admin', '0001_initial', '2021-11-23 09:36:41.343215'),
(17, 'admin', '0002_logentry_remove_auto_add', '2021-11-23 09:36:41.681312'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2021-11-23 09:36:41.697270'),
(19, 'paneluser', '0002_auto_20211114_1814', '2021-11-23 09:36:41.714224'),
(20, 'paneluser', '0003_auto_20211114_2252', '2021-11-23 09:36:41.733175'),
(21, 'paneluser', '0004_auto_20211120_1139', '2021-11-23 09:36:44.640576'),
(22, 'paneluser', '0005_auto_20211120_1142', '2021-11-23 09:36:44.704194'),
(23, 'paneluser', '0006_auto_20211120_1211', '2021-11-23 09:36:45.591857'),
(24, 'paneluser', '0007_alter_orders_attachment', '2021-11-23 09:36:45.608839'),
(25, 'paneluser', '0008_alter_orders_attachment', '2021-11-23 09:36:45.624019'),
(26, 'paneluser', '0009_auto_20211120_1336', '2021-11-23 09:36:45.669521'),
(27, 'paneluser', '0010_alter_ticketpm_ticket', '2021-11-23 09:36:45.824996'),
(28, 'paneluser', '0011_delete_payment', '2021-11-23 09:36:45.846937'),
(29, 'paneluser', '0012_auto_20211122_2336', '2021-11-23 09:36:46.191093'),
(30, 'paneluser', '0013_auto_20211123_0838', '2021-11-23 09:36:48.553775'),
(31, 'sessions', '0001_initial', '2021-11-23 09:36:48.597636');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `paneluser_orders`
--

CREATE TABLE `paneluser_orders` (
  `id` int(11) NOT NULL,
  `status` varchar(256) DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  `attachment` varchar(100) DEFAULT NULL,
  `packs_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `paneluser_packs`
--

CREATE TABLE `paneluser_packs` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `enable_check` tinyint(1) NOT NULL,
  `price` int(11) DEFAULT NULL,
  `short_desc` longtext DEFAULT NULL,
  `full_desc` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `paneluser_ticket`
--

CREATE TABLE `paneluser_ticket` (
  `id` int(11) NOT NULL,
  `depertment` varchar(256) DEFAULT NULL,
  `priority` varchar(256) DEFAULT NULL,
  `status` varchar(256) DEFAULT NULL,
  `subject` varchar(256) DEFAULT NULL,
  `text` longtext DEFAULT NULL,
  `attachment` varchar(100) DEFAULT NULL,
  `order_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `paneluser_ticketpm`
--

CREATE TABLE `paneluser_ticketpm` (
  `id` int(11) NOT NULL,
  `text` longtext DEFAULT NULL,
  `attachment` varchar(100) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `ticketid_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `paneluser_user`
--

CREATE TABLE `paneluser_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `phonenumber` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `paneluser_user_groups`
--

CREATE TABLE `paneluser_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `paneluser_user_user_permissions`
--

CREATE TABLE `paneluser_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `paneluser_orders`
--
ALTER TABLE `paneluser_orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `paneluser_orders_packs_id_c671b3c9_fk` (`packs_id`),
  ADD KEY `paneluser_orders_user_id_eb06b92e_fk` (`user_id`);

--
-- Indexes for table `paneluser_packs`
--
ALTER TABLE `paneluser_packs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `paneluser_ticket`
--
ALTER TABLE `paneluser_ticket`
  ADD PRIMARY KEY (`id`),
  ADD KEY `paneluser_ticket_order_id_75bfbbec_fk` (`order_id`),
  ADD KEY `paneluser_ticket_user_id_96555a29_fk` (`user_id`);

--
-- Indexes for table `paneluser_ticketpm`
--
ALTER TABLE `paneluser_ticketpm`
  ADD PRIMARY KEY (`id`),
  ADD KEY `paneluser_ticketpm_ticketid_id_dd452fed_fk` (`ticketid_id`),
  ADD KEY `paneluser_ticketpm_user_id_8ef85a7a_fk` (`user_id`);

--
-- Indexes for table `paneluser_user`
--
ALTER TABLE `paneluser_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `paneluser_user_groups`
--
ALTER TABLE `paneluser_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `paneluser_user_groups_user_id_group_id_db7a92ca_uniq` (`user_id`,`group_id`),
  ADD KEY `paneluser_user_groups_group_id_eeea64cf_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `paneluser_user_user_permissions`
--
ALTER TABLE `paneluser_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `paneluser_user_user_perm_user_id_permission_id_2eda581a_uniq` (`user_id`,`permission_id`),
  ADD KEY `paneluser_user_user__permission_id_fc81276c_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `paneluser_orders`
--
ALTER TABLE `paneluser_orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `paneluser_packs`
--
ALTER TABLE `paneluser_packs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `paneluser_ticket`
--
ALTER TABLE `paneluser_ticket`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `paneluser_ticketpm`
--
ALTER TABLE `paneluser_ticketpm`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `paneluser_user`
--
ALTER TABLE `paneluser_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `paneluser_user_groups`
--
ALTER TABLE `paneluser_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `paneluser_user_user_permissions`
--
ALTER TABLE `paneluser_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `paneluser_user` (`id`);

--
-- Constraints for table `paneluser_orders`
--
ALTER TABLE `paneluser_orders`
  ADD CONSTRAINT `paneluser_orders_packs_id_c671b3c9_fk` FOREIGN KEY (`packs_id`) REFERENCES `paneluser_packs` (`id`),
  ADD CONSTRAINT `paneluser_orders_user_id_eb06b92e_fk` FOREIGN KEY (`user_id`) REFERENCES `paneluser_user` (`id`);

--
-- Constraints for table `paneluser_ticket`
--
ALTER TABLE `paneluser_ticket`
  ADD CONSTRAINT `paneluser_ticket_order_id_75bfbbec_fk` FOREIGN KEY (`order_id`) REFERENCES `paneluser_orders` (`id`),
  ADD CONSTRAINT `paneluser_ticket_user_id_96555a29_fk` FOREIGN KEY (`user_id`) REFERENCES `paneluser_user` (`id`);

--
-- Constraints for table `paneluser_ticketpm`
--
ALTER TABLE `paneluser_ticketpm`
  ADD CONSTRAINT `paneluser_ticketpm_ticketid_id_dd452fed_fk` FOREIGN KEY (`ticketid_id`) REFERENCES `paneluser_ticket` (`id`),
  ADD CONSTRAINT `paneluser_ticketpm_user_id_8ef85a7a_fk` FOREIGN KEY (`user_id`) REFERENCES `paneluser_user` (`id`);

--
-- Constraints for table `paneluser_user_groups`
--
ALTER TABLE `paneluser_user_groups`
  ADD CONSTRAINT `paneluser_user_groups_group_id_eeea64cf_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `paneluser_user_user_permissions`
--
ALTER TABLE `paneluser_user_user_permissions`
  ADD CONSTRAINT `paneluser_user_user__permission_id_fc81276c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
