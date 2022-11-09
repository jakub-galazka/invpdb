DROP TABLE account CASCADE CONSTRAINTS;
DROP TABLE building CASCADE CONSTRAINTS;
DROP TABLE room CASCADE CONSTRAINTS;
DROP TABLE computer CASCADE CONSTRAINTS;
DROP TABLE cpu CASCADE CONSTRAINTS;
DROP TABLE ram_stick CASCADE CONSTRAINTS;
DROP TABLE gpu CASCADE CONSTRAINTS;
DROP TABLE software CASCADE CONSTRAINTS;
DROP TABLE account_building CASCADE CONSTRAINTS;
DROP TABLE software_computer CASCADE CONSTRAINTS;
CREATE TABLE account (
  account_id number(38) NOT NULL, 
  email      char(255) NOT NULL UNIQUE, 
  username   char(255) NOT NULL UNIQUE, 
  pass       char(255) NOT NULL, 
  last_login date NOT NULL, 
  PRIMARY KEY (account_id));
CREATE TABLE building (
  building_id   number(38) NOT NULL, 
  building_name char(255) NOT NULL UNIQUE, 
  floors_number number(3) NOT NULL, 
  street        char(255), 
  street_number char(255), 
  postal_code   char(255), 
  city          char(255), 
  country       char(255), 
  PRIMARY KEY (building_id));
CREATE TABLE room (
  room_id     number(38) NOT NULL, 
  room_number char(255) NOT NULL, 
  room_name   char(255) NOT NULL, 
  floor       number(3) NOT NULL, 
  building_id number(38) NOT NULL, 
  PRIMARY KEY (room_id));
CREATE TABLE computer (
  computer_id   number(38) NOT NULL, 
  computer_name char(255) NOT NULL, 
  manufacturer  char(255) NOT NULL, 
  ssd_memory    number(5), 
  hdd_memory    number(5), 
  add_info      char(2000), 
  room_id       number(38) NOT NULL, 
  PRIMARY KEY (computer_id));
CREATE TABLE cpu (
  cpu_id          number(38) NOT NULL, 
  cpu_name        char(255) NOT NULL, 
  manufacturer    char(255) NOT NULL, 
  cores_number    number(2) NOT NULL, 
  threads_number  number(2) NOT NULL, 
  min_clock_speed number(3, 2) NOT NULL, 
  max_clock_speed number(3, 2) NOT NULL, 
  memory          number(3) NOT NULL, 
  computer_id     number(38) NOT NULL, 
  PRIMARY KEY (cpu_id));
CREATE TABLE ram_stick (
  ram_stick_id   number(38) NOT NULL, 
  memory         number(3) NOT NULL, 
  ram_stick_type char(255) NOT NULL, 
  clock_speed    number(4) NOT NULL, 
  computer_id    number(38) NOT NULL, 
  PRIMARY KEY (ram_stick_id));
CREATE TABLE gpu (
  gpu_id       number(38) NOT NULL, 
  gpu_name     char(255) NOT NULL, 
  manufacturer char(255) NOT NULL, 
  memory       number(5) NOT NULL, 
  tgp          number(3), 
  computer_id  number(38) NOT NULL, 
  PRIMARY KEY (gpu_id));
CREATE TABLE software (
  software_id   number(38) NOT NULL, 
  software_name char(255) NOT NULL, 
  publisher     char(255) NOT NULL, 
  license_key   char(255), 
  expire_date   date, 
  PRIMARY KEY (software_id));
CREATE TABLE account_building (
  account_id  number(38) NOT NULL, 
  building_id number(38) NOT NULL);
CREATE TABLE software_computer (
  software_id number(38) NOT NULL, 
  computer_id number(38) NOT NULL);
ALTER TABLE account_building ADD CONSTRAINT FKaccount_bu654416 FOREIGN KEY (account_id) REFERENCES account (account_id);
ALTER TABLE account_building ADD CONSTRAINT FKaccount_bu316095 FOREIGN KEY (building_id) REFERENCES building (building_id);
ALTER TABLE room ADD CONSTRAINT FKroom519804 FOREIGN KEY (building_id) REFERENCES building (building_id);
ALTER TABLE computer ADD CONSTRAINT FKcomputer840158 FOREIGN KEY (room_id) REFERENCES room (room_id);
ALTER TABLE cpu ADD CONSTRAINT FKcpu71334 FOREIGN KEY (computer_id) REFERENCES computer (computer_id);
ALTER TABLE gpu ADD CONSTRAINT FKgpu67490 FOREIGN KEY (computer_id) REFERENCES computer (computer_id);
ALTER TABLE ram_stick ADD CONSTRAINT FKram_stick452317 FOREIGN KEY (computer_id) REFERENCES computer (computer_id);
ALTER TABLE software_computer ADD CONSTRAINT FKsoftware_c454240 FOREIGN KEY (software_id) REFERENCES software (software_id);
ALTER TABLE software_computer ADD CONSTRAINT FKsoftware_c657235 FOREIGN KEY (computer_id) REFERENCES computer (computer_id);
