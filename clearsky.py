import os
import itertools
import matplotlib.pyplot as plt
import pandas as pd
import pvlib
from pvlib import clearsky, atmosphere, solarposition
from pvlib.location import Location
from pvlib.iotools import read_tmy3

tus = Location(34.6937378, 135.5021651, 'Asia/Tokyo', 100, 'Tokyo')
times = pd.DatetimeIndex(start='2019-07-01', end='2019-07-04', freq='1min', tz=tus.tz)
cs = tus.get_clearsky(times)
cs.plot()
plt.show()