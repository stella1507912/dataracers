"""Queries for database views."""

from . import db_connect

def critical_dates(race_year):
    with db_connect() as con:
        with con.cursor() as cur:
            cur.execute("""SELECT
	    re."RaceID",
	    re."Location",
	    re."Date",
	    s."ShipmentID",
	    s."Status" AS "Shipment Status",
	    c."ConID" AS "Critical ContainerID"
	FROM "Race_Event" re
	JOIN "Shipment" s ON re."RaceID" = s."RaceID"
	JOIN "Container" c ON s."ShipmentID" = c."ShipmentID"
	WHERE re."Date" BETWEEN %s AND %s
	    AND s."Status" = 'Not Left'                      
	    AND c."CriticalContainer" = TRUE;""", (f"{race_year}-01-01", f"{race_year}-12-31"))
            return cur.fetchall()
        
def race_team_shipment(team_name: str) -> list:
    query = """
        SELECT re."RaceID", t."TeamName", s."ShipmentID", s."Status"
        FROM "Race_Event" re
        JOIN "Team" t ON re."RaceID" = t."RaceID"
        JOIN "Shipment" s ON re."RaceID" = s."RaceID"
        WHERE t."TeamName" = %s;
    """
    with db_connect() as con:
        with con.cursor() as cur:
            # cur.execute('SELECT * FROM "RaceTeamShipmentView" WHERE "TeamName" = %s', (team_name,))
            # return cur.fetchall()
            cur.execute(query, (team_name,))
            return cur.fetchall()