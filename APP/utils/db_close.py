
from sqlalchemy import create_engine
from APP.utils.profiles import select_profile


async def close_db_connection():
    profile = select_profile()
    from sqlalchemy import create_engine

    # Create the SQLAlchemy engine
    engine = create_engine(f"{profile.db_string}")

    # Get a raw connection from the engine
    raw_connection = engine.raw_connection()

    # Execute pragma command to unlock the database
    raw_connection.execute('pragma wal_checkpoint(TRUNCATE)')

    # Close the raw connection
    raw_connection.close()