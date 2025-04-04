create database if not exists rental;
create database if not exists price;
create database if not exists aptadditional;

use rental;
drop table if exists amenities_types;
drop table if exists amenities;
drop table if exists generalInfo;
drop table if exists propertyDetails;

use price;
drop table if exists payment;
drop table if exists pricing;

use aptadditional;
drop table if exists sources;
drop table if exists media;


-- Database 1
use rental;

create table generalInfo (
    id varchar(100) primary key,
    title text,
    cityname varchar(100),
    state varchar(100),
    latitude decimal(9, 6),
    longitude decimal(9, 6)
);

create table propertyDetails (
    id varchar(100),
    square_feet bigint,
    bedrooms decimal(2, 1),
    bathrooms decimal(2, 1),
    pets_allowed varchar(100),
    primary key (id),
    foreign key (id) references generalInfo(id) on delete cascade
);

create table amenities (
    amenity_id int auto_increment primary key,
    amenity_name varchar(100)
);

create table amenities_types (
    id varchar(100),
    amenity_id int,
    primary key (id, amenity_id),
    foreign key (id) references generalInfo(id) on delete cascade,
    foreign key (amenity_id) references amenities(amenity_id) on delete cascade
);

-- Database 2
use price;

create table pricing (
    id varchar(100) primary key,
    price int,
    currency varchar(100)
);

create table payment (
    id varchar(100),
    price_display varchar(100),
    price_type varchar(100),
    primary key (id),
    foreign key (id) references pricing(id) on delete cascade
);

-- Database 3
use aptadditional;

create table media (
    id varchar(100) primary key,
    has_photo varchar(100)
);

create table sources (
    id varchar(100),
    source varchar(100),
    time datetime,
    primary key (id),
    foreign key (id) references media(id) on delete cascade
);