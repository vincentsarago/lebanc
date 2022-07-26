"""Benchmark items."""

import os

import pytest
import morecantile
from rio_tiler.io import COGReader
import rasterio


cog_path = os.path.join(os.path.dirname(__file__), "fixtures", "world.tif")


@pytest.mark.parametrize(
    "tile",
    [
        morecantile.Tile(x=23, y=13, z=5),
        morecantile.Tile(x=1, y=2, z=3),
        morecantile.Tile(x=18, y=25, z=5),
        morecantile.Tile(x=1, y=3, z=2),
    ],
)
def test_benchmark_tile(benchmark, tile):
    """Benchmark tile."""

    def read_tile(t):
        with rasterio.Env(GDAL_CACHEMAX=0, NUM_THREADS="all"):
            with COGReader(cog_path, minzoom=0, maxzoom=8) as cog:
                return cog.tile(*t)

    response = benchmark(read_tile, tile)

