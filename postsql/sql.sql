CREATE TABLE Doctor (
    Doctor_Id SERIAL PRIMARY KEY,
    Doctor_Name VARCHAR NOT NULL,
    Hospital_Id INTEGER NOT NULL,
    Joining_Date DATE NOT NULL,
    Speciality VARCHAR NOT NULL,
    Salary INTEGER NOT NULL,
    Experience SMALLINT,
    FOREIGN KEY (Hospital_Id) REFERENCES hospital (Id) ON DELETE CASCADE
);
