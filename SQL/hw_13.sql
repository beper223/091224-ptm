CREATE TABLE IF NOT EXISTS Clients (
    id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_number VARCHAR(13),
    address VARCHAR(255),
    reg_date DATE
);

CREATE TABLE IF NOT EXISTS Autos (
    id INT PRIMARY KEY,
    model_name VARCHAR(255),
    production_year VARCHAR(4),
    color VARCHAR(255),
    country VARCHAR(255),
    class VARCHAR(4)
);

CREATE TABLE IF NOT EXISTS Drivers (
    id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    license_number VARCHAR(20),
    issue_licese_date DATE
);

CREATE TABLE IF NOT EXISTS Schedules (
    id INT PRIMARY KEY,
    driver_id int,
    auto_id int,
    begin_dt DATETIME,
    end_dt DATETIME,
    FOREIGN KEY (driver_id) REFERENCES Drivers(id),
	FOREIGN KEY (auto_id) REFERENCES Autos(id)
    );

CREATE TABLE IF NOT EXISTS Orders (
    id INT PRIMARY KEY,
    create_dt DATETIME,
    status INT,
    client_id INT,
    schedule_id INT,
    departure VARCHAR(255),
    arrival VARCHAR(255),
    FOREIGN KEY (client_id) REFERENCES Clients(id),
	FOREIGN KEY (schedule_id) REFERENCES Schedules(id)
    );