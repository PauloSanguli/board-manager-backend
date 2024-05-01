"""create the models of entities database"""

from datetime import datetime

from sqlalchemy import (
    Column,
    TEXT,
    INTEGER,
    Table,
    MetaData,
    TIMESTAMP,
    VARCHAR,
    create_engine,
    FLOAT,
    ForeignKey,
    DATE,
    BOOLEAN,
    String,
    Time,
    BOOLEAN
)

from dotenv import load_dotenv

import os



load_dotenv()
engine = create_engine(os.getenv("DATABASE_URI"))
Base = MetaData()

admin = Table(
    'admin',
    Base,
    Column('name', TEXT, nullable=False),
    Column('password', TEXT, nullable=False),
    Column('email', TEXT, unique=True, nullable=False)
)

owner = Table(
    'owner',
    Base,
    Column('id', INTEGER, autoincrement=True, primary_key=True),
    Column('identity_card_id', INTEGER, ForeignKey('identity_card.id')),
    Column('driving_license_id', INTEGER, ForeignKey('driving_license.id'))
)

veichle = Table(
    'veichle',
    Base,
    Column('id', INTEGER, primary_key=True, autoincrement=True),
    Column('board', TEXT, nullable=False),
    Column('owner_id', INTEGER, ForeignKey('owner.id')),
    Column('blocket_id', INTEGER, ForeignKey('blocket.id')),
    Column('car_veichle_title_id', INTEGER, ForeignKey('car_veichle_title.id')),
    Column('license_id', INTEGER, ForeignKey('license.id')),
    Column('inspection_id', INTEGER, ForeignKey('inspection.id')),
    Column('secure_id', INTEGER, ForeignKey('secure.id')),
    Column('state', TEXT, default="stay at home")
)

identity_card = Table(
    'identity_card',
    Base,
    Column('id', INTEGER, primary_key=True, autoincrement=True),
    Column('name', TEXT, nullable=False),
    Column('membership', TEXT, nullable=True),
    Column('ticket_number', TEXT, nullable=False),
    Column('residence', TEXT, nullable=False),
    Column('naturalness', VARCHAR(50), nullable=False),
    Column('province', VARCHAR(50), nullable=False),
    Column('date_birth', DATE, nullable=False),
    Column('sex', VARCHAR(1), nullable=False),
    Column('marital_status', VARCHAR(20), nullable=False),
    Column('height', FLOAT, nullable=False),
    Column('expired', BOOLEAN, default=False),
    Column('issued_on', DATE, nullable=False),
    Column('valid_until', DATE, nullable=False)
)

driving_license = Table(
    'driving_license',
    Base,
    Column('id', INTEGER, primary_key=True, autoincrement=True),
    Column('name', TEXT, nullable=False)        ,
    Column('issue_date', DATE, nullable=False),
    Column('expiration_date', DATE, nullable=False),
    Column('category_veichle', VARCHAR(30), nullable=False),
    Column('restrictions', TEXT, nullable=True),
    Column('veichle_identification_number', INTEGER, nullable=False),
    Column('document_issuer_signature', TEXT, nullable=False),
    Column('expired', BOOLEAN, default=False)
)

blocket = Table(
    'blocket',
    Base,
    Column('id', INTEGER, primary_key=True, autoincrement=True),
    Column('board', TEXT, nullable=False),
    Column('chassis' , VARCHAR(50), nullable=False),
    Column('mark', VARCHAR(50), nullable=False),
    Column('model', VARCHAR(50), nullable=False),
    Column('category_veichle', VARCHAR(30), nullable=False),
    Column('number_places', INTEGER, nullable=False),
    Column('color', VARCHAR(20), nullable=False),
    Column('type_fuel', TEXT, nullable=False),
    Column('fiscal_power', TEXT, nullable=False),
    Column('issue_date_board', DATE, nullable=False),
    Column('veichle_purchase_date', DATE, nullable=False),
    Column('last_inspection_date', DATE, nullable=False),
    Column('enviroment_class_veichle', TEXT, nullable=False),
    Column('emissions_co2', FLOAT, nullable=False),
    Column('gross_weight', FLOAT, nullable=False),
    Column('obs', TEXT, nullable=True),
)

car_veichle_title = Table(
    'car_veichle_title',
    Base,
    Column('id', INTEGER, primary_key=True, autoincrement=True),
    Column('name_owner', TEXT, nullable=False),
    Column('home_adress_owner', TEXT, nullable=False),
    Column('board', TEXT, nullable=False),
    Column('chassis' , VARCHAR(50), nullable=False),
    Column('mark', VARCHAR(50), nullable=False),
    Column('model', VARCHAR(50), nullable=False),
    Column('color', VARCHAR(20), nullable=False),
    Column('type_fuel', TEXT, nullable=False),
    Column('number_places', INTEGER, nullable=False),
    Column('issue_date', DATE, nullable=False),
    Column('registration_date', DATE, nullable=False),
    Column('manufacture_date', DATE, nullable=False),
    Column('registration_number', INTEGER, nullable=False),
    Column('engine_power', TEXT, nullable=False),
)

traffic_agent = Table(
    'traffic_agent',
    Base,
    Column('id', INTEGER, primary_key=True, autoincrement=True),
    Column('username', TEXT, nullable=False),
    Column('email', VARCHAR(100), unique=True, nullable=False),
    Column('password', TEXT, nullable=False),
    Column('cellphone', VARCHAR(20), nullable=False)
)

license = Table(
    'license',
    Base,
    Column('id', INTEGER,primary_key=True,autoincrement=True),
    Column('expiration_date', DATE, nullable=False),
    Column('cod', String(40), nullable=False)
)

secure = Table(
    'secure',
    Base,
    Column('id', INTEGER, primary_key=True, autoincrement=True),
    Column('expiration_date', DATE, nullable=False),
    Column('cod', String(40), nullable=False)
)

inspection = Table(
    'inspection',
    Base,
    Column('id', INTEGER, primary_key=True, autoincrement=True),
    Column('expiration_date', DATE, nullable=False),
    Column('cod', String(40), nullable=False)
)

newspaper = Table(
    'newspaper',
    Base,
    Column('id', INTEGER, primary_key=True, autoincrement=True),
    Column('reference', VARCHAR(50), nullable=False, unique=True),
    Column('body', TEXT, nullable=False),
    Column('date_publish', TIMESTAMP, default=datetime.now),
    Column('updated_at', TIMESTAMP, default=datetime.now, onupdate=datetime.now),
)

infractions = Table(
    'infractions',
    Base,
    Column('id', INTEGER, primary_key=True, autoincrement=True),
    Column('identity_card_id', INTEGER, ForeignKey("identity_card.id")),
    Column('blocket_id', INTEGER, ForeignKey("blocket.id")),
    Column('num_carter_habilitacion', INTEGER, nullable=False),
    Column('obs', TEXT, nullable=False),
    Column('date', DATE, nullable=False),
    Column('local', TEXT, nullable=False),
    Column('time', Time, nullable=False),
    Column('type_infraction', TEXT, nullable=False),
    Column('value', FLOAT, nullable=False),
    Column('info_payment', TEXT, nullable=False),
    Column('paid', BOOLEAN, default=False),
)

Base.create_all(engine)
