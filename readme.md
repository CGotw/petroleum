```SQL
CREATE TABLE `area_table` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `management_area_code` varchar(256) NOT NULL,
  `date` date NOT NULL,
  `power_consumption` double DEFAULT NULL,
  `daily_liquid_production` double DEFAULT NULL,
  `daily_carbon_dioxide_production` double DEFAULT NULL,
  `productive_time` double DEFAULT NULL,
  `theoretical_discharge_capacity` double DEFAULT NULL,
  `daily_oil_production` double DEFAULT NULL,
  `daily_water_production` double DEFAULT NULL,
  `daily_gas` double DEFAULT NULL,
  `plant_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

```

```SQL
CREATE TABLE `plant_table` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `oil_production_plant_number` varchar(256) NOT NULL,
  `date` date NOT NULL,
  `power_consumption` double DEFAULT NULL,
  `daily_liquid_production` double DEFAULT NULL,
  `daily_carbon_dioxide_production` double DEFAULT NULL,
  `productive_time` double DEFAULT NULL,
  `theoretical_discharge_capacity` double DEFAULT NULL,
  `daily_oil_production` double DEFAULT NULL,
  `daily_water_production` double DEFAULT NULL,
  `daily_gas` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

```SQL
CREATE TABLE `station_table` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `injection_and_extraction_station_number` varchar(256) NOT NULL,
  `date` date NOT NULL,
  `power_consumption` double DEFAULT NULL,
  `daily_liquid_production` double DEFAULT NULL,
  `daily_carbon_dioxide_production` double DEFAULT NULL,
  `productive_time` double DEFAULT NULL,
  `theoretical_discharge_capacity` double DEFAULT NULL,
  `daily_oil_production` double DEFAULT NULL,
  `daily_water_production` double DEFAULT NULL,
  `daily_gas` double DEFAULT NULL,
  `area_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1
```

```SQL
CREATE TABLE `well_table` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `oil _well` varchar(256) NOT NULL,
  `date` date NOT NULL,
  `oil_pressure` double DEFAULT NULL,
  `casing _pressure` double DEFAULT NULL,
  `gauge _pressure` double DEFAULT NULL,
  `back_pressure` double DEFAULT NULL,
  `wellhead _temperature` double DEFAULT NULL,
  `daily_liquid_production` double DEFAULT NULL,
  `Daily_carbon_dioxide_production` double DEFAULT NULL,
  `voltage` double DEFAULT NULL,
  `current` double DEFAULT NULL,
  `upward _curren` double DEFAULT NULL,
  `descending_current` double DEFAULT NULL,
  `power_consumption` double DEFAULT NULL,
  `output_liquid_concentration` double DEFAULT NULL,
  `jig_frequency` double DEFAULT NULL,
  `stroke` double DEFAULT NULL,
  `opening_time` double DEFAULT NULL,
  `speed` int(11) DEFAULT NULL,
  `productive_time` double DEFAULT NULL,
  `pump_diameter` double DEFAULT NULL,
  `theoretical_discharge_capacity` double DEFAULT NULL,
  `daily_oil_production` double DEFAULT NULL,
  `daily_water_production` double DEFAULT NULL,
  `daily_gas` double DEFAULT NULL,
  `gas-oil_ratio` double DEFAULT NULL,
  `containing_water` double DEFAULT NULL,
  `Water_content_added` double DEFAULT NULL,
  `pump_depth` double DEFAULT NULL,
  `balance_degree` double DEFAULT NULL,
  `pump_efficiency` double DEFAULT NULL,
  `station_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```