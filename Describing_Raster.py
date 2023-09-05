import arcpy

raster_path = r"D:\Sem-3\Programming for GIS-3\RASTER_DATA\ASTGTMV003_N27E077_dem.tif"

desc_obj = arcpy.Describe(raster_path)

dataset_type = desc_obj.datasetType

print(dataset_type)

# The Number of band in the raster dataset
print(desc_obj.bandCount)

# Raster dataset format. Possible value are Grid, ERDAS IMAGINE, TIFF
print(desc_obj.format)

# Raster band pixel type. Value indicate signed and unsigned pixel types in 1 bit through 32 bit
print(desc_obj.pixelType)

#