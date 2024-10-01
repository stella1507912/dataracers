-- query to find a team's kits (in this case the team with the ID 1234).
SELECT *
FROM Team_Table
    JOIN Team_Kit ON Team_Table.TeamID = Team_Kit.TeamID
WHERE Team_Table.TeamID = 1234;

-- find the teams at a certain race event (race 57)
SELECT TeamName
FROM Team_Table
    JOIN Race_Event ON Team_Table.RaceID = Race_Event.RaceID
WHERE RaceID = 57;


-- find a container information for a race event and container
SELECT RaceID
FROM Race_Event
	JOIN Shipment ON Race_Event.RaceID = Shipment.RaceID
    JOIN Container ON Shipment.ShipmentID = Container.ShipmentID
WHERE ConID = 12 AND RaceID = 57;

-- Query to find all team kits that are part of a specific container
-- in this case, container 10
SELECT Team_Kit.*, Team_Table.TeamName
FROM Container_contains_TeamKits
    JOIN Team_Kit ON Container_contains_TeamKits.KitID = Team_Kit.KitID
    JOIN Team_Table ON Team_Kit.TeamID = Team_Table.TeamID
WHERE ConID = 10;

-- Query to find the number of containers per shipment
SELECT Shipment.ShipmentID, COUNT(Container.ConID) AS ContainerCount
FROM Shipment
    JOIN Container ON Shipment.ShipmentID = Container.ShipmentID
GROUP BY Shipment.ShipmentID;

