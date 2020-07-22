"""
SQL Queries to assist with:
- Dropping existing database tables
- Creating tables
- Inserting data into the database
- Reading data from the database
"""

table_names = ["trail_popularity", "top_elevation_gain_parks", "medium_trails_in_arizona"]

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
create_arizona_trails_table_query = """
    CREATE TABLE IF NOT EXISTS medium_trails_in_arizona
    (name TEXT, area_name TEXT, state_name TEXT, 
    difficulty_rating FLOAT, 
    PRIMARY KEY ((state_name), difficulty_rating));
    """
create_table_queries = [create_popularity_table_query, create_top_elevation_gain_table_query, create_arizona_trails_table_query]

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

load_queries = {"popularity": load_popularity_query, "elevation_gain": load_elevation_query, "arizona_trails": load_med_arizona_trails_query}

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
read_queries = [read_popularity_query, read_elevation_query, read_med_arizona_trails_query]