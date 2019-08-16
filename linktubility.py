import calendar
import os
import matplotlib.pyplot as plt
import tables
import pvlib


pvlib_path = os.path.dirname(os.path.abspath(pvlib.clearsky.__file__))
filepath = os.path.join(pvlib_path, 'data', 'LinkeTurbidities.h5')


def plot_turbidity_map(month, vmin=1, vmax=100):
    plt.figure()
    with tables.open_file(filepath) as lt_h5_file:
        ltdata = lt_h5_file.root.LinkeTurbidity[:, :, month - 1]
    plt.imshow(ltdata, vmin=vmin, vmax=vmax)
    # data is in units of 20 x turbidity
    plt.title('Linke turbidity x 20, ' + calendar.month_name[month])
    plt.colorbar(shrink=0.5)
    plt.tight_layout()


plot_turbidity_map(1)
plot_turbidity_map(7)
plt.show()
