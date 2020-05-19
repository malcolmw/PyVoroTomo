import numpy as np

EARTH_RADIUS              = 6371.
ROOT_RANK                 = 0
DISPATCH_REQUEST_TAG      = 100
DISPATCH_TRANSMISSION_TAG = 101
DTYPE_INT                 = np.int64
DTYPE_REAL                = np.float64

EVENT_DTYPES = dict(
    event_id=DTYPE_INT,
    latitude=DTYPE_REAL,
    longitude=DTYPE_REAL,
    depth=DTYPE_REAL,
    time=DTYPE_REAL,
    residual=DTYPE_REAL
)
EVENT_FIELDS = [
    "event_id",
    "latitude",
    "longitude",
    "depth",
    "time",
    "residual"
]

ARRIVAL_DTYPES = dict(
    event_id=DTYPE_INT,
    network=str,
    station=str,
    phase=str,
    time=DTYPE_REAL,
    residual=DTYPE_REAL
)
ARRIVAL_FIELDS = [
    "event_id",
    "network",
    "station",
    "phase",
    "time",
    "residual"
]
try:

    import h5py
    import mpi4py.MPI as MPI
    import os

    COMM = MPI.COMM_WORLD

    filename = ".MbCZm61Z3M"
    f5 = h5py.File(filename, 'w', driver='mpio', comm=COMM)
    f5.close()

    if COMM.Get_rank() == ROOT_RANK:
        os.remove(filename)

    HDF5_PARALLEL_ENABLED = True

except AttributeError:

    HDF5_PARALLEL_ENABLED = False
