from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('mysql+pymysql://easyque:Easyque@2022@localhost:3306/easyque', echo = True)
meta = MetaData()
conn = engine.connect()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('password', String(255))
)


owners = Table(
    'owners', meta,
    Column('id', Integer, primary_key=True),
    Column('contact', String(255)),
    Column('auth_token', String(255)),
    Column('fcm_token', String(255)),
    Column('active', Integer()),
)


property = Table(
    'property', meta,
    Column('id', Integer, primary_key=True),
    Column('uid', Integer()),
    Column('property_name', String(255)),
    Column('images', String(255)),
    Column('latitude', String(255)),
    Column('longtitude', String(255)),
    Column('landmark_1', String(255)),
    Column('landmark_2', String(255)),
    Column('landmark_3', String(255)),
    Column('rent', String(255)),
    Column('city', String(255)),
    Column('state', String(255)),
    Column('country', String(255)),
    Column('gender', String(255)),
    Column('type', String(255)),
    Column('is_verified', Integer()),
    Column('avg_rating', String(255)),
    Column('hygiene_rating', String(255)),
    Column('food_quality_rating', String(255)),
    Column('power_backup', String(255)),
    Column('wifi', String(255)),
    Column('security_deposit', String(255)),
    Column('security_deposit_amount', String(255)),
    Column('notice_period', String(255)),
    Column('furnished_level', String(255)),
    Column('laundry_facility', String(255)),
    Column('ac', String(255)),
    Column('total_floors', String(255)),
    Column('attach_lat_bath', String(255)),
    Column('maintainace_charge', String(255)),
)


# ins = students.insert().values(name = 'Ravi', email = 'Kapoor', password='sdfsffsdfsfs')
# result = conn.execute(ins)

meta.create_all(engine)
