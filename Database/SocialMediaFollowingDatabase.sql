-- MySQL Script generated by MySQL Workbench
-- Wed 19 Jul 2017 17:03:29 BST
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`KeyWords`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`KeyWords` ;

CREATE TABLE IF NOT EXISTS `mydb`.`KeyWords` (
  `idKeyWords` INT NOT NULL AUTO_INCREMENT,
  `KeyWord` VARCHAR(160) NULL,
  `IsUserHandle` BINARY NULL,
  `Comment` VARCHAR(500) NULL,
  `DateTime` DATETIME NULL,
  `Following` INT NULL COMMENT '0 -  not following\n1 -  following\n2 - schedulled for deleting\n3 - deleted',
  PRIMARY KEY (`idKeyWords`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TwUsersOfInterest`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`TwUsersOfInterest` ;

CREATE TABLE IF NOT EXISTS `mydb`.`TwUsersOfInterest` (
  `UsersOfInterestId` INT NOT NULL AUTO_INCREMENT,
  `TwitterId` VARCHAR(45) NULL,
  `Name` VARCHAR(100) NULL,
  `ScreenName` VARCHAR(100) NULL,
  `description` VARCHAR(200) NULL,
  `url` VARCHAR(200) NULL,
  `Location` VARCHAR(200) NULL,
  `timezone` VARCHAR(200) NULL,
  `created_at` VARCHAR(200) NULL,
  `statuses_count` INT NULL,
  `followers_count` INT NULL,
  `following_count` INT NULL,
  `fav_count` INT NULL,
  `listed_count` INT NULL,
  `Following` INT NULL COMMENT '0 - not following yet\n1- following\n2 - scheduled for deleting\n3 - deleted\n',
  PRIMARY KEY (`UsersOfInterestId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`tweets`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`tweets` ;

CREATE TABLE IF NOT EXISTS `mydb`.`tweets` (
  `idTweets` INT NOT NULL,
  `recorded` DATETIME NULL,
  `text` VARCHAR(200) NULL,
  `isRetweet` BINARY NULL,
  `twitterID` VARCHAR(45) NULL,
  `userHandle` VARCHAR(100) NULL,
  `Tw_user_id` VARCHAR(45) NULL,
  `UserName` VARCHAR(100) NULL,
  `UserDesc` VARCHAR(200) NULL,
  `in_reply_to_screenname` VARCHAR(45) NULL,
  `in_reply_to_status_id_str` VARCHAR(45) NULL,
  `retweets` INT NULL,
  `fav_count` INT NULL,
  `Location` VARCHAR(200) NULL,
  PRIMARY KEY (`idTweets`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Entities`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Entities` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Entities` (
  `idEntities` INT NOT NULL,
  `Type` VARCHAR(45) NULL,
  `EntityName` VARCHAR(45) NULL,
  `tweets_idTweets` INT NOT NULL,
  `url` VARCHAR(45) NULL,
  PRIMARY KEY (`idEntities`),
  INDEX `fk_Entities_tweets_idx` (`tweets_idTweets` ASC),
  CONSTRAINT `fk_Entities_tweets`
    FOREIGN KEY (`tweets_idTweets`)
    REFERENCES `mydb`.`tweets` (`idTweets`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
