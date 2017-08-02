-- MySQL Script generated by MySQL Workbench
-- 08/02/17 12:18:46
-- Model: New Model    Version: 1.0
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';


-- -----------------------------------------------------
-- Table `KeyWords`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `KeyWords` ;

CREATE TABLE IF NOT EXISTS `KeyWords` (
  `idKeyWords` INT NOT NULL AUTO_INCREMENT,
  `KeyWord` VARCHAR(160) NULL,
  `IsUserHandle` BINARY NULL,
  `Comment` VARCHAR(500) NULL,
  `DateTime` DATETIME NULL,
  `Following` INT NULL COMMENT '0 -  not following' /* comment truncated */ /*1 -  following
2 - schedulled for deleting
3 - deleted*/,
  PRIMARY KEY (`idKeyWords`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TwUsersOfInterest`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `TwUsersOfInterest` ;

CREATE TABLE IF NOT EXISTS `TwUsersOfInterest` (
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
  `Following` INT NULL COMMENT '0 - not following yet' /* comment truncated */ /*1- following
2 - scheduled for deleting
3 - deleted
*/,
  PRIMARY KEY (`UsersOfInterestId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tweets`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tweets` ;

CREATE TABLE IF NOT EXISTS `tweets` (
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
-- Table `Entities`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Entities` ;

CREATE TABLE IF NOT EXISTS `Entities` (
  `idEntities` INT NOT NULL,
  `Type` VARCHAR(45) NULL,
  `EntityName` VARCHAR(45) NULL,
  `tweets_idTweets` INT NOT NULL,
  `url` VARCHAR(45) NULL,
  PRIMARY KEY (`idEntities`),
  INDEX `fk_Entities_tweets_idx` (`tweets_idTweets` ASC),
  CONSTRAINT `fk_Entities_tweets`
    FOREIGN KEY (`tweets_idTweets`)
    REFERENCES `tweets` (`idTweets`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `UserTweets`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `UserTweets` ;

CREATE TABLE IF NOT EXISTS `UserTweets` (
  `idUserTweets` INT NOT NULL AUTO_INCREMENT,
  `recorded` DATETIME NULL,
  `text` VARCHAR(200) NULL,
  `isRetweeted` INT NULL,
  `in_reply_to_screenname` VARCHAR(100) NULL,
  `in_reply_to_status_id` VARCHAR(100) NULL,
  `twitter_id` VARCHAR(200) NULL,
  `retweets` INT NULL,
  `fav_count` INT NULL,
  `TwUsersOfInterest_UsersOfInterestId` INT NOT NULL,
  PRIMARY KEY (`idUserTweets`),
  INDEX `fk_UserTweets_TwUsersOfInterest1_idx` (`TwUsersOfInterest_UsersOfInterestId` ASC),
  CONSTRAINT `fk_UserTweets_TwUsersOfInterest1`
    FOREIGN KEY (`TwUsersOfInterest_UsersOfInterestId`)
    REFERENCES `TwUsersOfInterest` (`UsersOfInterestId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `UserTweetEntities`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `UserTweetEntities` ;

CREATE TABLE IF NOT EXISTS `UserTweetEntities` (
  `idEntities` INT NOT NULL,
  `Type` VARCHAR(45) NULL,
  `EntityName` VARCHAR(45) NULL,
  `url` VARCHAR(45) NULL,
  `UserTweets_idUserTweets` INT NOT NULL,
  PRIMARY KEY (`idEntities`),
  INDEX `fk_Entities_copy1_UserTweets1_idx` (`UserTweets_idUserTweets` ASC),
  CONSTRAINT `fk_Entities_copy1_UserTweets1`
    FOREIGN KEY (`UserTweets_idUserTweets`)
    REFERENCES `UserTweets` (`idUserTweets`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;