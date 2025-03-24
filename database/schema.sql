-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2025-03-22 04:30:04.047

-- tables
-- Table: drivers
CREATE TABLE drivers (
    id int IDENTITY(1,1) NOT NULL,
    name varchar(256)  NOT NULL,
    nationality varchar(256)  NOT NULL,
    CONSTRAINT drivers_pk PRIMARY KEY  (id)
);

-- Table: engines
CREATE TABLE engines (
    id int IDENTITY(1,1) NOT NULL,
    manufacturer varchar(256)  NOT NULL,
    CONSTRAINT engines_pk PRIMARY KEY  (id)
);

-- Table: engines_teams
CREATE TABLE engines_teams (
    engines_id int  NOT NULL,
    teams_id int  NOT NULL,
    CONSTRAINT engines_teams_pk PRIMARY KEY  (engines_id,teams_id)
);

-- Table: team_principals
CREATE TABLE team_principals (
    id int IDENTITY(1,1) NOT NULL,
    name varchar(256)  NOT NULL,
    experience int  NOT NULL,
    CONSTRAINT team_principals_pk PRIMARY KEY  (id)
);

-- Table: team_principals_teams
CREATE TABLE team_principals_teams (
    team_principals_id int  NOT NULL,
    teams_id int  NOT NULL,
    CONSTRAINT team_principals_teams_pk PRIMARY KEY  (team_principals_id,teams_id)
);

-- Table: teams
CREATE TABLE teams (
    id int IDENTITY(1,1) NOT NULL,
    name varchar(256)  NOT NULL,
    CONSTRAINT teams_pk PRIMARY KEY  (id)
);

-- Table: teams_drivers
CREATE TABLE teams_drivers (
    teams_id int  NOT NULL,
    drivers_id int  NOT NULL,
    CONSTRAINT teams_drivers_pk PRIMARY KEY  (teams_id,drivers_id)
);

-- foreign keys
-- Reference: engines_teams_engines (table: engines_teams)
ALTER TABLE engines_teams ADD CONSTRAINT engines_teams_engines
    FOREIGN KEY (engines_id)
    REFERENCES engines (id)
    ON DELETE CASCADE;

-- Reference: engines_teams_teams (table: engines_teams)
ALTER TABLE engines_teams ADD CONSTRAINT engines_teams_teams
    FOREIGN KEY (teams_id)
    REFERENCES teams (id)
    ON DELETE CASCADE;

-- Reference: team_principals_teams_team_principals (table: team_principals_teams)
ALTER TABLE team_principals_teams ADD CONSTRAINT team_principals_teams_team_principals
    FOREIGN KEY (team_principals_id)
    REFERENCES team_principals (id)
    ON DELETE CASCADE;

-- Reference: team_principals_teams_teams (table: team_principals_teams)
ALTER TABLE team_principals_teams ADD CONSTRAINT team_principals_teams_teams
    FOREIGN KEY (teams_id)
    REFERENCES teams (id)
    ON DELETE CASCADE;

-- Reference: teams_drivers_drivers (table: teams_drivers)
ALTER TABLE teams_drivers ADD CONSTRAINT teams_drivers_drivers
    FOREIGN KEY (drivers_id)
    REFERENCES drivers (id)
    ON DELETE CASCADE;

-- Reference: teams_drivers_teams (table: teams_drivers)
ALTER TABLE teams_drivers ADD CONSTRAINT teams_drivers_teams
    FOREIGN KEY (teams_id)
    REFERENCES teams (id)
    ON DELETE CASCADE;

-- End of file.

