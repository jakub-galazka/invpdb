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
DROP TABLE workplace CASCADE CONSTRAINTS;
CREATE TABLE account (
  account_id number(7), 
  email      char(50) NOT NULL UNIQUE, 
  username   char(50) NOT NULL UNIQUE, 
  pass       char(10) NOT NULL, 
  last_login date NOT NULL, 
  PRIMARY KEY (account_id));
CREATE TABLE building (
  building_id   number(7), 
  building_name char(50) NOT NULL UNIQUE, 
  floors_number number(1) NOT NULL, 
  street        char(50), 
  street_number number(7), 
  postal_code   number(5), 
  city          char(50), 
  country       char(50), 
  PRIMARY KEY (building_id));
CREATE TABLE room (
  room_id     number(7), 
  room_number char(5) NOT NULL, 
  room_name   char(50) NOT NULL, 
  floor       number(1) NOT NULL, 
  building_id number(7) NOT NULL, 
  PRIMARY KEY (room_id));
CREATE TABLE computer (
  computer_id   number(7), 
  computer_name char(50) NOT NULL, 
  manufacturer  char(50) NOT NULL, 
  ssd_memory    number(5), 
  hdd_memory    number(5), 
  add_info      char(2000), 
  room_id       number(7) NOT NULL, 
  PRIMARY KEY (computer_id));
CREATE TABLE cpu (
  cpu_id          number(7), 
  cpu_name        char(50) NOT NULL, 
  manufacturer    char(50) NOT NULL, 
  cores_number    number(2) NOT NULL, 
  threads_number  number(2) NOT NULL, 
  min_clock_speed number(3, 2) NOT NULL, 
  max_clock_speed number(3, 2) NOT NULL, 
  memory          number(2) NOT NULL, 
  computer_id     number(7) NOT NULL, 
  PRIMARY KEY (cpu_id));
CREATE TABLE ram_stick (
  ram_stick_id   number(7), 
  memory         number(2) NOT NULL, 
  ram_stick_type char(4) NOT NULL, 
  clock_speed    number(4) NOT NULL, 
  computer_id    number(7) NOT NULL, 
  PRIMARY KEY (ram_stick_id));
CREATE TABLE gpu (
  gpu_id       number(7), 
  gpu_name     char(50) NOT NULL, 
  manufacturer char(50) NOT NULL, 
  memory       number(5) NOT NULL, 
  tgp          number(3), 
  computer_id  number(7) NOT NULL, 
  PRIMARY KEY (gpu_id));
CREATE TABLE software (
  software_id   number(7), 
  software_name char(50) NOT NULL, 
  publisher     char(50) NOT NULL, 
  license_key   char(15), 
  expire_date   date, 
  PRIMARY KEY (software_id));
CREATE TABLE account_building (
  account_id  number(7) NOT NULL, 
  building_id number(7) NOT NULL);
CREATE TABLE software_computer (
  software_id number(7) NOT NULL, 
  computer_id number(7) NOT NULL);
ALTER TABLE account_building ADD CONSTRAINT FKaccount_bu654416 FOREIGN KEY (account_id) REFERENCES account (account_id) ON DELETE CASCADE;
ALTER TABLE account_building ADD CONSTRAINT FKaccount_bu316095 FOREIGN KEY (building_id) REFERENCES building (building_id) ON DELETE CASCADE;
ALTER TABLE room ADD CONSTRAINT FKroom519804 FOREIGN KEY (building_id) REFERENCES building (building_id) ON DELETE CASCADE;
ALTER TABLE computer ADD CONSTRAINT FKcomputer840158 FOREIGN KEY (room_id) REFERENCES room (room_id) ON DELETE CASCADE;
ALTER TABLE cpu ADD CONSTRAINT FKcpu71334 FOREIGN KEY (computer_id) REFERENCES computer (computer_id) ON DELETE CASCADE;
ALTER TABLE gpu ADD CONSTRAINT FKgpu67490 FOREIGN KEY (computer_id) REFERENCES computer (computer_id) ON DELETE CASCADE;
ALTER TABLE ram_stick ADD CONSTRAINT FKram_stick452317 FOREIGN KEY (computer_id) REFERENCES computer (computer_id) ON DELETE CASCADE;
ALTER TABLE software_computer ADD CONSTRAINT FKsoftware_c454240 FOREIGN KEY (software_id) REFERENCES software (software_id) ON DELETE CASCADE;
ALTER TABLE software_computer ADD CONSTRAINT FKsoftware_c657235 FOREIGN KEY (computer_id) REFERENCES computer (computer_id) ON DELETE CASCADE;