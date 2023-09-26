import uvicorn
from fastapi import FastAPI,APIRouter
from numpy.compat import long
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

info_router = APIRouter()

@info_router.get("/info/plants", summary='所有工厂 id 和 name')
async def plants():
    db = SessionLocal()
    items = db.query(plant_table).all()
    data = [{"id": plant_table.id, "name": plant_table.oil_production_plant_number} for item in items]
    return data

DATABASE_URL = "mysql://root:123456@localhost:3306/petroleum"

# 创建数据库引擎和会话
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建数据模型
Base = declarative_base()


class Area(Base):
    __tablename__ = "area_table"
    id = Column(Integer, primary_key=True, index=True)
    management_area_code = Column(String(50))
    date = Column(String(50))
    power_consumption = Column(String(50))
    daily_liquid_production = Column(String(50))
    daily_carbon_dioxide_production = Column(String(50))
    productive_time = Column(String(50))
    theoretical_discharge_capacity = Column(String(50))
    daily_oil_production = Column(String(50))
    daily_water_production = Column(String(50))
    daily_gas = Column(String(50))
    plant_id = Column(Integer)


class Plant(Base):
    __tablename__ = "plant_table"
    id = Column(Integer, primary_key=True, index=True)
    oil_production_plant_number = Column(String(50))
    date = Column(String(50))
    power_consumption = Column(String(50))
    daily_liquid_production = Column(String(50))
    daily_carbon_dioxide_production = Column(String(50))
    productive_time = Column(String(50))
    theoretical_discharge_capacity = Column(String(50))
    daily_oil_production = Column(String(50))
    daily_water_production = Column(String(50))
    daily_gas = Column(String(50))


class Station(Base):
    __tablename__ = "station_table"
    id = Column(Integer, primary_key=True, index=True)
    injection_and_extraction_station_number = Column(String(50))
    date = Column(String(50))
    power_consumption = Column(String(50))
    daily_liquid_production = Column(String(50))
    daily_carbon_dioxide_production = Column(String(50))
    productive_time = Column(String(50))
    theoretical_discharge_capacity = Column(String(50))
    daily_oil_production = Column(String(50))
    daily_water_production = Column(String(50))
    daily_gas = Column(String(50))
    area_id = Column(Integer)


class Well(Base):
    __tablename__ = "well_table"
    id = Column(Integer, primary_key=True, index=True)
    oil_well = Column(String(50))
    date = Column(String(50))
    oil_pressure = Column(String(50))
    casing_pressure = Column(String(50))
    gauge_pressure = Column(String(50))
    back_pressure = Column(String(50))
    wellhead_temperature = Column(String(50))
    daily_liquid_production = Column(String(50))
    daily_carbon_dioxide_production = Column(String(50))
    voltage = Column(String(50))
    current = Column(String(50))
    upward_curren = Column(String(50))
    descending_current = Column(String(50))
    power_consumption = Column(String(50))
    output_liquid_concentration = Column(String(50))
    jig_frequency = Column(String(50))
    stroke = Column(String(50))
    opening_time = Column(String(50))
    speed = Column(String(50))
    productive_time = Column(String(50))
    pump_diameter = Column(String(50))
    theoretical_discharge_capacity = Column(String(50))
    daily_oil_production = Column(String(50))
    daily_water_production = Column(String(50))
    daily_gas = Column(String(50))
    gas_oil_ratio = Column(String(50))
    containing_water = Column(String(50))
    water_content_added = Column(String(50))
    pump_depth = Column(String(50))
    balance_degree = Column(String(50))
    pump_efficiency = Column(String(50))
    station_id = Column(String(50))


@info_router.get("/info/plants", summary='所有工厂 id 和 name')
async def plants():
    db = SessionLocal()
    items = db.query(Plant).all()
    data = [{'id':item.id, 'name':item.oil_production_plant_number} for item in items]
    return {
        "data":data
    }


@info_router.get("/info/areas", summary='该工厂 id 下的所有的管理区 id 和 name')
async def areas(plantId: int):
    db = SessionLocal()
    items = db.query(Area).filter(Area.plant_id == plantId).all()
    res = []
    for item in items:
        res.append({
            'id': item.id,
            'name': item.management_area_code
        })
    return {"data": res}


@info_router.get("/info/stations", summary='该管理区 id 下的所有的注采站 id 和 name')
async def stations(areaId: int):
    db = SessionLocal()
    items = db.query(Station).filter(Station.area_id == areaId).all()
    res = []
    for item in items:
        res.append({
            'id': item.id,
            'name': item.injection_and_extraction_station_number
        })
    return {"data": res}


@info_router.get("/info/wells", summary='该注采站 id 下的所有的油井 id 和 name')
async def wells(stationId: int):
    db = SessionLocal()
    items = db.query(Well).filter(Well.station_id == stationId).all()
    res = []
    for item in items:
        res.append({
            'id': item.id,
            'name': item.oil_well
        })
    return {"data": res}

@info_router.get("/info/wells_information", summary='返回指定工厂，管理区，注采站，油井，日期下的数据')
async def wells(plantId: int, areaId: int, stationId: int, wellId: int, date: str):
    db = SessionLocal()
    # 去油井表里找油井号和日期对应的数据
    well = db.query(Well).filter(Well.id == wellId,Well.date==date).first()
    # 去注采站里找注采站号和日期对应的数据
    station = db.query(Station).filter(Station.id == stationId,Station.date==date).first()
    # 去管理区里找和日期对应的数据
    area = db.query(Area).filter(Area.id == areaId,Area.date==date).first()
    # 去采油厂里找管理区和日期对应的数据
    plant = db.query(Plant).filter(Plant.id == plantId, Plant.date == date).first()
    data={
        "date":date,
        "well": well,
        "station": station,
        "area" : area,
        "plant": plant
    }
    return data


# 运行FastAPI应用
if __name__ == '__main__':
    uvicorn.run('main:app')
