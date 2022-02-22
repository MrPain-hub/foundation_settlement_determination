Language: Python 3.6+\
OS: Windows\
RU
##О Проекте
Данный проект будет полезен инженеру-проектировщику, так как экономит время на
определение сжимаемой толщи грунта и осадки под фундаментом.\
**Вычисления производятся в соответсвии с СП-83 и СП-2017**

##Абревиатуры
ИГЭ - инжинерно геологический элемент, слой грунта.\
ГСТ - глубина сжимаемой толщи грунта.\
МПС - метод послойного суммирования.

##Описание пакета `layer_summation_method`
Пакет содержит модули для моделирования геологического разреза, 
плиты фундамента и определения осадки.\
####`CreateModels.py` - _используется для создания моделей._
 Включает в себя следующие классы:\
` CreateMaterial` - _создание материала_\
`Soil` - _создание ИГЭ(геологический слой)_\
`CreateBorehole` - _создание геологической скважины_\
`CreateLoad` - _создание нагрузки_\
`CreatePlate` - _создание плиты фундамента_

####`Methods.py` - _содержит метод и способы определения осадки фундамента_
На данный момент включает в себя только один метод определения:\
`LayerSumMethod` - _класс определяет ГСТ и осадку фундамента с помощью МПС_ 
