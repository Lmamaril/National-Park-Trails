import pandas as pd
import cassandra
from cassandra.cluster import Cluster
from sql_queries import table_names, create_table_queries, load_queries, read_queries

def connect_database():
    """ Connects to the cassandra db
        
        Params:
            None
        Returns:
            cluster a cassandra cluster object
            session a cassandra session object
    """
    # create the cluster to connect to the Cassandra instance
    cluster = Cluster(['127.0.0.1'])

    # create the connection
    session = cluster.connect()
    
    # create the keyspace
    create_keyspace = """
        CREATE KEYSPACE IF NOT EXISTS np_trails
        WITH replication = 
        {'class' : 'SimpleStrategy', 'replication_factor' : 1}
        """

    try:
        session.execute(create_keyspace)
    except Exception as er:
        print(er)
    
    # set the keyspace
    session.set_keyspace('np_trails')
    
    return cluster, session
    
def drop_table(session, table_name):
    """ Drops all existing tables
    """
    drop_table_query = "DROP TABLE IF EXISTS {}".format(table_name)
    try:
        session.execute(drop_table_query)
    except Exception as er:
        print(er)

def main():
    
    # connect to the database
    cluster, session = connect_database()
    
    # drop the tables
    for table in table_names:
        drop_table(session, table)
    
    # create the tables
    for create_table in create_table_queries:
        try:
            session.execute(create_table)
        except Exception as er:
            print(er)
    
    # read the data
    df = pd.read_csv("../data/alltrails-nationalpark.csv")
    
    # insert the values

    for idx, row in df.iterrows():
        load_query = """
            INSERT INTO trail_popularity (name, area_name, popularity) 
            VALUES (%s, %s, %s);
            """
        popularity_row = (row['name'], row['area_name'], row.popularity)
        session.execute(load_queries['popularity'], popularity_row) 
        
        elevation_gain_row = (row['area_name'], row['elevation_gain'])
        session.execute(load_queries['elevation_gain'], elevation_gain_row)
        
        arizona_trails_row = (row['name'], row['area_name'], row['state_name'], row['difficulty_rating'])
        session.execute(load_queries['arizona_trails'], arizona_trails_row)
        
        cluster.shutdown()
    
    
    # read from the database
if __name__ == "__main__":
    main()