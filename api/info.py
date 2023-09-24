from fastapi import APIRouter

info_router = APIRouter()


@info_router.get("/info/plants", summary='所有工厂 id 和 name')
async def plants():
    pass


@info_router.get("/info/areas", summary='该工厂 id 下的所有的管理区 id 和 name')
async def areas(plantId: int):
    pass


@info_router.get("/info/stations", summary='该管理区 id 下的所有的注采站 id 和 name')
async def stations(areaId: int):
    pass


@info_router.get("/info/wells", summary='该注采站 id 下的所有的油井 id 和 name')
async def wells(stationId: int):
    pass


@info_router.get("/info/wells", summary='返回指定工厂，管理区，注采站，油井，日期下的数据')
async def wells(plantId: int, areaId: int, stationId: int, wellId: int, date: str):
    pass


    return {
        'plant':{

        },
        'area':{

        },
        'station':{

        },
        'well':{

        }
    }
