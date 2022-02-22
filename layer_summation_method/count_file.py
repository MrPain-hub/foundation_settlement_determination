from CreateModels import *
from Methods import *

"""
Входные данные
"""
dict_ige = {"ige1": 0,
            "ige2": 0,
            "ige3": 0,
            }
dict_soil = {"soil0": "ige1",
             "soil1": "ige2",
             "soil2": "ige3",
             }
E = [6e6, 10e6, 15e6]
gamma = [16e3, 17e3, 18e3]
z_soils = [50, 30, 20, 0]
water_soils = [False, False, False]
P = 200e3
H_found = 0
f_length = 30
f_width = 5
"""
Создание материалов
"""
for i, ige in enumerate(dict_ige):
    dict_ige[ige] = CreateMaterial()
    dict_ige[ige].change = ("E", E[i])
    dict_ige[ige].change = ("gamma", gamma[i])
"""
Создание скважины
"""
Borehole_1 = CreateBorehole(0, 0)
"""
Создание слоев в скважине
"""
for i, soil in enumerate(dict_soil):
    Borehole_1.createSoil(bot=z_soils[i + 1],
                          water=water_soils[i],
                          material=dict_ige[dict_soil[soil]]
                          )
Borehole_1.change[0][0].change["Top"] = z_soils[0]
"""
Создание нагрузки и плиты
"""
load_1 = CreateLoad(Type="P", load=P)
plate_1 = CreatePlate(FL=z_soils[0]-H_found, length=f_length, width=f_width)
plate_1.change["Load"] = load_1
"""
Вычисление напряжений
"""
Mps = LayerSumMethod(Borehole_1, plate_1, load_1, type_found="ленточный")
Mps.calculation()
print(f"осадка {Mps.Output()[0]}")
print(f"Отметка {Mps.comparison()}")
