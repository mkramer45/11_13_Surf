-- GOOD --
CREATE TABLE SurfMaster2 AS
select SurfReport.ID, SurfReport.SwellSizeFt, SurfReport.SwellIntervalSec, WindInfo.WindMPH, WindDirection.WindDescription, SurfReport.AirTemp
from SurfReport
inner join WindInfo on SurfReport.ID = WindInfo.ID
inner join WindDirection on WindInfo.ID = WindDirection.ID

--Adds Beachname column
ALTER TABLE SurfMaster2
  ADD beach_name TEXT;

-- Updates Beachname Column with Appropriate value
--Narragansett
UPDATE SurfMaster2
SET beach_name = 'Narragansett'
WHERE
 ID BETWEEN 1 AND 56;

--2nd Beach
 UPDATE SurfMaster2
SET beach_name = '2nd Beach'
WHERE
 ID BETWEEN 57 AND 112;

--Nahant
UPDATE SurfMaster2
SET beach_name = 'Nahant'
WHERE
 ID BETWEEN 113 AND 168;

 --Nantasket
UPDATE SurfMaster2
SET beach_name = 'Nantasket'
WHERE
 ID BETWEEN 169 AND 224;

--Scituate
UPDATE SurfMaster2
SET beach_name = 'Scituate'
WHERE
 ID BETWEEN 225 AND 280;

--Cape Cod
UPDATE SurfMaster2
SET beach_name = 'Cape Cod'
WHERE
 ID BETWEEN 281 AND 336;

--NH Seacoast
UPDATE SurfMaster2
SET beach_name = 'NH Seacoast'
WHERE
 ID BETWEEN 337 AND 392;

--Green Harbor 
UPDATE SurfMaster2
SET beach_name = 'Green Harbor'
WHERE
 ID BETWEEN 393 AND 448;

--Cape Ann
UPDATE SurfMaster2
SET beach_name = 'Cape Ann'
WHERE
 ID BETWEEN 449 AND 504;

--Myrtle Beach (NC)
UPDATE SurfMaster2
SET beach_name = 'Myrtle Beach'
WHERE
 ID BETWEEN 505 AND 560;

--Cocoa Beach FL
UPDATE SurfMaster2
SET beach_name = 'Cocoa Beach'
WHERE
 ID BETWEEN 561 AND 616;
 
 --Adds Date column
ALTER TABLE SurfMaster2
  ADD date_ TEXT;

 --First 8 records are for (current_day)
	-- and so on and so fourth ... ie second 8 records are for getdate(+1)
UPDATE SurfMaster2
SET date_ = date('now')
WHERE
 Time_ID BETWEEN 1 AND 8;

-- 2nd set of 8 records ... getdate(+1)
UPDATE SurfMaster2
SET date_ = date('now','+1 day')
WHERE
 Time_ID BETWEEN 9 AND 16;

-- 2nd set of 8 records ... getdate(+2)
UPDATE SurfMaster2
SET date_ = date('now','+2 day')
WHERE
 Time_ID BETWEEN 17 AND 24;
 
-- 3rd set of 8 records ... getdate(+3)
UPDATE SurfMaster2
SET date_ = date('now','+3 day')
WHERE
 Time_ID BETWEEN 25 AND 32;

-- 4th set of 8 records ... getdate(+4)
UPDATE SurfMaster2
SET date_ = date('now','+4 day')
WHERE
 Time_ID BETWEEN 33 AND 40;
 
-- 5th set of 8 records ... getdate(+5)
UPDATE SurfMaster2
SET date_ = date('now','+5 day')
WHERE
 Time_ID BETWEEN 41 AND 48;

 -- 6th set of 8 records ... getdate(+6)
UPDATE SurfMaster2
SET date_ = date('now','+6 day')
WHERE
 Time_ID BETWEEN 49 AND 56;

 -- Adds Time column
 ALTER TABLE SurfMaster2
  ADD time_ TEXT;

  --Time = 12am
UPDATE SurfMaster2
SET time_ = '12am'
WHERE
 Time_ID in (1,9,17,25,33,41,49)

  --Time = 3am
UPDATE SurfMaster2
SET time_ = '3am'
WHERE
 Time_ID in (2,10,18,26,34,42,50)
 
  --Time = 6am
UPDATE SurfMaster2
SET time_ = '6am'
WHERE
 Time_ID in (3,11,19,27,35,43,51)
 
  --Time = 9am
UPDATE SurfMaster2
SET time_ = '9am'
WHERE
 Time_ID in (4,12,20,28,36,44,52)
 
  --Time = 12pm
UPDATE SurfMaster2
SET time_ = '12pm'
WHERE
 Time_ID in (5,13,21,29,37,45,53)
 
   --Time = 3pm
UPDATE SurfMaster2
SET time_ = '3pm'
WHERE
 Time_ID in (6,14,22,30,38,46,54)

   --Time = 6pm
UPDATE SurfMaster2
SET time_ = '6pm'
WHERE
 Time_ID in (7,15,23,31,39,47,55)
 
    --Time = 9pm
UPDATE SurfMaster2
SET time_ = '9pm'
WHERE
 Time_ID in (8,16,24,32,40,48,56)
 
--Add new column for TimeID 
ALTER TABLE SurfMaster2
  ADD Time_ID TEXT;



