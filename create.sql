CREATE TABLE "Circuits" (
  "id" int PRIMARY KEY,
  "name" varchar
);

CREATE TABLE "Athlete" (
  "id" int PRIMARY KEY,
  "name" varchar,
  "birthday" datetime,
  "country" varchar
);

CREATE TABLE "Judges" (
  "id" int PRIMARY KEY,
  "name" varchar,
  "country" varchar
);

CREATE TABLE "Countries" (
  "name" varchar PRIMARY KEY
);

CREATE TABLE "IndividualSkate" (
  "id" int PRIMARY KEY,
  "competition" int,
  "athlete" varchar,
  "rank" int,
  "type" boolean,
  "score" int
);

CREATE TABLE "Competitions" (
  "id" int PRIMARY KEY,
  "level" int,
  "host_country" varchar,
  "start_time" datetime,
  "end_time" datetime
);

CREATE TABLE "TechnicalElements" (
  "id" int PRIMARY KEY,
  "skate_id" int,
  "type" varchar,
  "base_score" int,
  "sequence_number" int,
  "is_second_half" boolean,
  "downgraded" boolean,
  "edge_call" boolean,
  "is_rep" boolean,
  "failed_requirements" boolean,
  "edge_warning" boolean,
  "GOE" int
);

CREATE TABLE "PerformanceElement" (
  "id" int PRIMARY KEY,
  "skate_id" int,
  "type" varchar,
  "multiplier" int
);

CREATE TABLE "TechnicalElementReference" (
  "name" varchar PRIMARY KEY,
  "base_score" int,
  "is_jump" boolean
);

CREATE TABLE "JudgesTechnical" (
  "judge" int,
  "technical_element" int,
  "score" int,
  "dropped" boolean
);

CREATE TABLE "JudgesPerformance" (
  "judge" int,
  "perfromance_element" int,
  "score" int
);

CREATE TABLE "Deductions" (
  "skate" int,
  "reason" varchar,
  "points_off" int
);

ALTER TABLE "IndividualSkate" ADD FOREIGN KEY ("competition") REFERENCES "Competitions" ("id");

ALTER TABLE "Competitions" ADD FOREIGN KEY ("host_country") REFERENCES "Countries" ("name");

ALTER TABLE "TechnicalElements" ADD FOREIGN KEY ("skate_id") REFERENCES "IndividualSkate" ("id");

ALTER TABLE "PerformanceElement" ADD FOREIGN KEY ("skate_id") REFERENCES "IndividualSkate" ("id");

ALTER TABLE "JudgesTechnical" ADD FOREIGN KEY ("judge") REFERENCES "Judges" ("id");

ALTER TABLE "JudgesTechnical" ADD FOREIGN KEY ("technical_element") REFERENCES "TechnicalElements" ("id");

ALTER TABLE "JudgesPerformance" ADD FOREIGN KEY ("judge") REFERENCES "Judges" ("id");

ALTER TABLE "JudgesPerformance" ADD FOREIGN KEY ("perfromance_element") REFERENCES "PerformanceElement" ("id");

ALTER TABLE "Deductions" ADD FOREIGN KEY ("skate") REFERENCES "IndividualSkate" ("id");

ALTER TABLE "Athlete" ADD FOREIGN KEY ("country") REFERENCES "Countries" ("name");

ALTER TABLE "Judges" ADD FOREIGN KEY ("country") REFERENCES "Countries" ("name");

ALTER TABLE "IndividualSkate" ADD FOREIGN KEY ("athlete") REFERENCES "Athlete" ("id");
