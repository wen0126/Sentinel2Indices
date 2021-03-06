import numpy as np

#https://www.indexdatabase.de/db/s-single.php?id=96

#class of an satellite index, created only with name
class SatelliteIndex:
    def __init__(self,name):
        self.name = name

idxs = {}



def build_simple_index(channel1, channel2):
    """Basic index function, which calculates (channel1 - channel2)/(channel1 + channel2)
        input: 2 x 2D-numpy array, output = 1 x 2D-numpy array"""
    # calculate index
    idx = channel1 - channel2
    idx = np.divide(idx, (channel1 + channel2))
    return idx


#Normalized Difference Vegetation Index
NDVI = SatelliteIndex('Normalized Difference Vegetation Index')
NDVI.abbreviation = 'NDVI'
NDVI.channels = ['B08', 'B04']
NDVI.function = build_simple_index
NDVI.use = 'Detection of vegetation'
NDVI.Source = 'https://www.sentinel-hub.com/eoproducts/ndvi-normalized-difference-vegetation-index'
idxs['NDVI'] = (NDVI)

#Normalized Difference Water Index
NDWI = SatelliteIndex('Normalized Difference Water Index')
NDWI.abbreviation = 'NDWI'
NDWI.channels = ['B08', 'B11']
NDWI.function = build_simple_index
NDWI.use = 'Detection of water'
NDWI.Source = 'https://www.sentinel-hub.com/develop/documentation/eo_products/Sentinel2EOproducts'
idxs['NDWI'] = NDWI

#Modified Normalized Difference Water Index
MNDWI = SatelliteIndex('Modified Normalized Difference Water Index')
MNDWI.abbreviation = 'MNDWI'
MNDWI.channels = ['B03', 'B11']
MNDWI.function = build_simple_index
MNDWI.use = 'Detection of water'
MNDWI.Source = 'https://www.mdpi.com/2072-4292/8/4/354'
idxs['MNDWI'] = MNDWI

#Normalized Burn Ratio
NBR = SatelliteIndex('Normalized Burn Ratio')
NBR.abbreviation = 'NBR'
NBR.channels = ['B08', 'B12']
NBR.function = build_simple_index
NBR.use = 'Detection of water'
NBR.Source = 'https://www.indexdatabase.de/db/si-single.php?sensor_id=96&rsindex_id=53r'
idxs['NBR'] = NBR





