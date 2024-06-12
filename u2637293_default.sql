-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Июн 12 2024 г., 09:06
-- Версия сервера: 5.7.27-30
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `u2637293_default`
--

-- --------------------------------------------------------

--
-- Структура таблицы `Chats`
--

CREATE TABLE `Chats` (
  `chat_id` int(11) UNSIGNED NOT NULL,
  `user_one_id` int(11) UNSIGNED NOT NULL,
  `user_two_id` int(11) UNSIGNED NOT NULL,
  `chat_time` varchar(10) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `Comments`
--

CREATE TABLE `Comments` (
  `comment_id` int(11) UNSIGNED NOT NULL,
  `post_id` int(11) UNSIGNED NOT NULL,
  `user_id` int(11) UNSIGNED NOT NULL,
  `comment_time` varchar(1119) NOT NULL DEFAULT '',
  `comment_text` text,
  `likes` int(11) DEFAULT NULL,
  `dislikes` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Comments`
--

INSERT INTO `Comments` (`comment_id`, `post_id`, `user_id`, `comment_time`, `comment_text`, `likes`, `dislikes`) VALUES
(1, 2, 1, '2024-06-09 11:37:49', 'yoyoyoyo', 0, 0),
(2, 2, 1, '2024-06-09 11:38:06', 'assalamuallykum', 0, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `Followers`
--

CREATE TABLE `Followers` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `follower_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `Images`
--

CREATE TABLE `Images` (
  `image_id` int(11) UNSIGNED NOT NULL,
  `path` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Images`
--

INSERT INTO `Images` (`image_id`, `path`) VALUES
(1, 'fee14908-c8b3-46f0-ae9f-31d8e384e08b.png'),
(2, '7875df87-eaeb-4bdd-8233-7b69dc75c575.png');

-- --------------------------------------------------------

--
-- Структура таблицы `Messages`
--

CREATE TABLE `Messages` (
  `message_id` int(11) UNSIGNED NOT NULL,
  `chat_id` int(11) UNSIGNED NOT NULL,
  `user_from_id` int(11) UNSIGNED NOT NULL,
  `user_to_id` int(11) UNSIGNED NOT NULL,
  `message_text` text,
  `message_time` varchar(19) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `Online`
--

CREATE TABLE `Online` (
  `user_id` int(11) UNSIGNED NOT NULL,
  `time` varchar(20) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Online`
--

INSERT INTO `Online` (`user_id`, `time`) VALUES
(1, '2024-06-12 03:59:33'),
(2, '2024-06-12 05:57:39');

-- --------------------------------------------------------

--
-- Структура таблицы `Posts`
--

CREATE TABLE `Posts` (
  `post_id` int(11) UNSIGNED NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `image_id` int(11) UNSIGNED DEFAULT NULL,
  `video_id` int(11) UNSIGNED DEFAULT NULL,
  `post_text` text,
  `likes` int(11) DEFAULT NULL,
  `dislikes` int(11) DEFAULT NULL,
  `post_time` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Posts`
--

INSERT INTO `Posts` (`post_id`, `user_id`, `image_id`, `video_id`, `post_text`, `likes`, `dislikes`, `post_time`) VALUES
(1, 2, 1, 1, 'всем хай', 1, 0, '2024-06-09 06:34:50'),
(2, 1, NULL, NULL, 'wassupski', 0, 1, '2024-06-09 11:37:16'),
(3, 1, NULL, NULL, 'че я тут забыл ваще', 0, 1, '2024-06-10 01:58:40'),
(4, 1, NULL, NULL, 'вау, это типа твиттер лол', 1, 0, '2024-06-10 01:58:43'),
(5, 1, NULL, NULL, 'че за разрабы, бездарный проект какой-то', 0, 0, '2024-06-10 01:58:46'),
(6, 1, NULL, NULL, 'типа импортозамещение, да? путин заблокал твиттер и это наш ответ хвпхахпа', 1, 0, '2024-06-10 01:58:49'),
(7, 1, NULL, NULL, 'сука, разрабы слили мою почту фсб и меня закрывают на пару лет. уёбища', 0, 1, '2024-06-10 01:58:52');

-- --------------------------------------------------------

--
-- Структура таблицы `Reactions`
--

CREATE TABLE `Reactions` (
  `reaction_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `post_id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  `reaction` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Reactions`
--

INSERT INTO `Reactions` (`reaction_id`, `user_id`, `post_id`, `comment_id`, `reaction`) VALUES
(4, 2, 6, 0, 'like'),
(5, 2, 2, 0, 'dislike'),
(7, 2, 7, 0, 'dislike'),
(8, 2, 4, 0, 'like'),
(9, 2, 1, 0, 'like'),
(10, 2, 3, 0, 'dislike');

-- --------------------------------------------------------

--
-- Структура таблицы `Users`
--

CREATE TABLE `Users` (
  `user_id` int(11) UNSIGNED NOT NULL,
  `email` varchar(100) NOT NULL,
  `username` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `name` varchar(15) NOT NULL DEFAULT '',
  `access` varchar(11) NOT NULL,
  `image_id` int(11) UNSIGNED DEFAULT '1',
  `about` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Users`
--

INSERT INTO `Users` (`user_id`, `email`, `username`, `password`, `name`, `access`, `image_id`, `about`) VALUES
(1, 'kutorgin2002@gmail.com', 'skyskyksyksy', '4457b43477faab6de1b620a20122ced5', 'xx00sky00xx', 'Admin', 1, ''),
(2, 'romansokolv209@gmail.com', 'sokolovsky', '7d1a71c82250fcc9313d80f2f32a0f90', 'r0manch1k', 'Admin', 2, 'if you ain\'t left yeah you can go ahead');

-- --------------------------------------------------------

--
-- Структура таблицы `Verifications`
--

CREATE TABLE `Verifications` (
  `verification_id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `username` varchar(32) NOT NULL,
  `name` varchar(15) NOT NULL,
  `code` int(11) NOT NULL,
  `time` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `Videos`
--

CREATE TABLE `Videos` (
  `video_id` int(11) UNSIGNED NOT NULL,
  `path` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `Chats`
--
ALTER TABLE `Chats`
  ADD PRIMARY KEY (`chat_id`),
  ADD KEY `user_one_id` (`user_one_id`),
  ADD KEY `user_two_id` (`user_two_id`);

--
-- Индексы таблицы `Comments`
--
ALTER TABLE `Comments`
  ADD PRIMARY KEY (`comment_id`),
  ADD KEY `post_id` (`post_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Индексы таблицы `Followers`
--
ALTER TABLE `Followers`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `Images`
--
ALTER TABLE `Images`
  ADD PRIMARY KEY (`image_id`) USING BTREE;

--
-- Индексы таблицы `Messages`
--
ALTER TABLE `Messages`
  ADD PRIMARY KEY (`message_id`),
  ADD KEY `chat_id` (`chat_id`);

--
-- Индексы таблицы `Online`
--
ALTER TABLE `Online`
  ADD PRIMARY KEY (`user_id`);

--
-- Индексы таблицы `Posts`
--
ALTER TABLE `Posts`
  ADD PRIMARY KEY (`post_id`);

--
-- Индексы таблицы `Reactions`
--
ALTER TABLE `Reactions`
  ADD PRIMARY KEY (`reaction_id`);

--
-- Индексы таблицы `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `image_id` (`image_id`);

--
-- Индексы таблицы `Verifications`
--
ALTER TABLE `Verifications`
  ADD PRIMARY KEY (`verification_id`);

--
-- Индексы таблицы `Videos`
--
ALTER TABLE `Videos`
  ADD PRIMARY KEY (`video_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `Chats`
--
ALTER TABLE `Chats`
  MODIFY `chat_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Comments`
--
ALTER TABLE `Comments`
  MODIFY `comment_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `Followers`
--
ALTER TABLE `Followers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `Images`
--
ALTER TABLE `Images`
  MODIFY `image_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `Messages`
--
ALTER TABLE `Messages`
  MODIFY `message_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Online`
--
ALTER TABLE `Online`
  MODIFY `user_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `Posts`
--
ALTER TABLE `Posts`
  MODIFY `post_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT для таблицы `Reactions`
--
ALTER TABLE `Reactions`
  MODIFY `reaction_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT для таблицы `Users`
--
ALTER TABLE `Users`
  MODIFY `user_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `Verifications`
--
ALTER TABLE `Verifications`
  MODIFY `verification_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `Videos`
--
ALTER TABLE `Videos`
  MODIFY `video_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `Chats`
--
ALTER TABLE `Chats`
  ADD CONSTRAINT `Chats_ibfk_1` FOREIGN KEY (`user_one_id`) REFERENCES `Users` (`user_id`),
  ADD CONSTRAINT `Chats_ibfk_2` FOREIGN KEY (`user_two_id`) REFERENCES `Users` (`user_id`);

--
-- Ограничения внешнего ключа таблицы `Comments`
--
ALTER TABLE `Comments`
  ADD CONSTRAINT `Comments_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `Posts` (`post_id`);

--
-- Ограничения внешнего ключа таблицы `Messages`
--
ALTER TABLE `Messages`
  ADD CONSTRAINT `Messages_ibfk_1` FOREIGN KEY (`chat_id`) REFERENCES `Chats` (`chat_id`);

--
-- Ограничения внешнего ключа таблицы `Online`
--
ALTER TABLE `Online`
  ADD CONSTRAINT `Online_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`);

--
-- Ограничения внешнего ключа таблицы `Users`
--
ALTER TABLE `Users`
  ADD CONSTRAINT `Users_ibfk_1` FOREIGN KEY (`image_id`) REFERENCES `Images` (`image_id`) ON DELETE SET NULL ON UPDATE CASCADE;

DELIMITER $$
--
-- События
--
CREATE DEFINER=`u2637293_default`@`localhost` EVENT `CLEAN_REQUESTS` ON SCHEDULE EVERY 10 MINUTE STARTS '2024-06-08 16:52:00' ON COMPLETION PRESERVE ENABLE DO DELETE FROM `Verifications` WHERE time < NOW() - INTERVAL 90 SECOND$$

DELIMITER ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
