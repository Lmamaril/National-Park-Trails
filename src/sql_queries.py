"""
SQL Queries to assist with:
- Dropping existing database tables
- Creating tables
- Inserting data into the database
- Reading data from the database
"""

tables_names = ["trail_popularity", "top_elevation_gain_parks", "medium_trails_in_arizona"]

# DROP TABLES
def drop_table(table_name):
    drop_table_query = "DROP TABLE IF EXISTS {}".format(table_name)
    try:
        session.execute(drop_table_query)
    except Exception as er:
        print(er)

# CREATE TABLES
create_popularity_table_query = """
    CREATE TABLE IF NOT EXISTS trail_popularity 
    (name TEXT, area_name TEXT, popularity FLOAT, 
    PRIMARY KEY(name, popularity)) 
    WITH CLUSTERING ORDER BY (popularity DESC);
    """
create_top_elevation_gain_table_query = """
    CREATE TABLE IF NOT EXISTS top_elevation_gain_parks 
    (area_name TEXT, elevation_gain FLOAT, 
    PRIMARY KEY(area_name, elevation_gain));
    """
create_table_query = """
    CREATE TABLE IF NOT EXISTS medium_trails_in_arizona
    (name TEXT, area_name TEXT, state_name TEXT, 
    difficulty_rating FLOAT, 
    PRIMARY KEY ((state_name), difficulty_rating));
    """

# INSERT DATA
load_popularity_query = """
    INSERT INTO trail_popularity (name, area_name, popularity) 
    VALUES (%s, %s, %s);
    """
load_elevation_query = """
    INSERT INTO top_elevation_gain_parks (area_name, elevation_gain) 
    VALUES (%s, %s);
    """
load_med_arizona_trails_query = """
    INSERT INTO medium_trails_in_arizona (name, area_name, state_name, difficulty_rating) 
    VALUES (%s, %s, %s, %s);
    """

# READ DATA
read_popularity_query = "SELECT * FROM trail_popularity LIMIT 2;"
read_elevation_query = """
    SELECT area_name, MAX(elevation_gain) AS max
    FROM top_elevation_gain_parks 
    GROUP BY area_name;
    """
read_med_arizona_trails_query = """
    SELECT name, area_name FROM medium_trails_in_arizona
    WHERE state_name = 'Arizona' AND difficulty_rating = 3;
    """