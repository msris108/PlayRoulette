# Database Schema

#### CasinoUser

| email* | user_name | password | first_name | last_name | is_active | is_staff | is_superuser | balance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### RouletteGame

| gameID* | start_time | end_time | is_active | dealerID# | bet_limit | amount_limit | is_superuser |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### RouletteNumber

| id* | gameID# | number |
| --- | --- | --- |

#### RouletteBet

| id* | bet_number | is_active | dealerID# | playerID# | gameID# | amount |
| --- | --- | --- | --- | --- | --- | --- |

\* - Primary Key  
\# - Foriegn Key

**Description of associations & indices:**

1. RouletteGame.dealerID -> CasinoUser.email
2. RouletteNumber.gameID -> RouletteGame.gameID
3. RouletteBet.dealerID -> CasinoUser.email
4. RouletteBet.playerID -> CasinoUser.email
5. RouletteBet.gameID -> RouletteGame.gameID

**NOTE** :  

- CasinoUser.password and RouletteNumber.number are encrypted with SECRET_KEY.
- A Sample Populated Database (sqllite.db) is provided for testing. 
- The database can be migrated to a postgreSQL instance by uncommenting the driver in settings.py. (tested fot postgreSQL, can migrate to other DB instances as well).
- Minimized raw SQL queries in to prevent SQL injection attacks and easy migration to other databases.  
#### DDL
```
---
# CasinoUser:
CREATE TABLE IF NOT EXISTS "user_casinouser" ("password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "email" varchar(254) NOT NULL PRIMARY KEY, "user_name" varchar(50) NOT NULL, "first_name" varchar(50) NOT NULL, "last_name" varchar(50) NOT NULL, "balance" integer NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL);
---
# RoultteGame:
CREATE TABLE IF NOT EXISTS "roulette_roulettegame" ("gameID" varchar(10) NOT NULL PRIMARY KEY, "start_time" datetime NOT NULL, "end_time" datetime NOT NULL, "is_active" bool NOT NULL, "dealerID_id" varchar(254) NOT NULL REFERENCES "user_casinouser" ("email") DEFERRABLE INITIALLY DEFERRED, "bet_limit" integer NOT NULL, "amount_limit" integer NOT NULL);
CREATE INDEX "roulette_roulettegame_dealerID_id_c4ff398a" ON "roulette_roulettegame" ("dealerID_id");
---
# RouletteNumber
CREATE TABLE IF NOT EXISTS "roulette_roulettenumber" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "number" text NOT NULL, "gameID_id" varchar(10) NOT NULL REFERENCES "roulette_roulettegame" ("gameID") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "roulette_roulettenumber_gameID_id_eb0dc014" ON "roulette_roulettenumber" ("gameID_id")
---
# RouletteBet
CREATE TABLE IF NOT EXISTS "roulette_roulettebet" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "bet_number" integer NOT NULL, "amount" integer NOT NULL, "is_active" bool NOT NULL, "dealerID_id" varchar(254) NOT NULL REFERENCES "user_casinouser" ("email") DEFERRABLE INITIALLY DEFERRED, "gameID_id" varchar(10) NOT NULL REFERENCES "roulette_roulettegame" ("gameID") DEFERRABLE INITIALLY DEFERRED, "playerID_id" varchar(254) NOT NULL REFERENCES "user_casinouser" ("email") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "roulette_roulettebet_dealerID_id_6f408570" ON "roulette_roulettebet" ("dealerID_id");
CREATE INDEX "roulette_roulettebet_gameID_id_a86a3446" ON "roulette_roulettebet" ("gameID_id");
CREATE INDEX "roulette_roulettebet_playerID_id_1efcaf20" ON "roulette_roulettebet" ("playerID_id");
---
```

