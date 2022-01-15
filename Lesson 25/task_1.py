from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import math

owm = OWM('616b19f855025f498b47f3069a1594a6')
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Moscow')
w = observation.weather

print('Текущая температура в Москве:', math.floor(w.temperature('celsius')['temp']))
