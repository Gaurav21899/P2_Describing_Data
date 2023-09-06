import arcpy
import os
gdb_path = r"D:\Sem-3\Programming for GIS-3\P2_Describing_Data\Practical_2_ProProject\02_Describing_Data.gdb"
fc_name_list = ["MajorAttractions", "Freeways"]

for fc in fc_name_list:
    fc_path = os.path.join(gdb_path, fc)
    desc_obj = arcpy.Describe(fc_path)

    # The type of Geometry, some possible values: Point, Polyline, Polygon, Multipoint and MultiPatch
    shape_type = desc_obj.shapeType
    print("The geometry type of feature class : {} is {}".format(fc, shape_type))

    # User assigned name
    fc_name = desc_obj.name
    # print(fc_name)

    # The type of the dataset. Some possible value: FeatureClass,RasterDataset, Table
    dataset_type = desc_obj.datasetType
    # print(dataset_type)
    print("The name of {} is {} and the type is {}".format(dataset_type, fc_name, shape_type))

    sr_obj = desc_obj.spatialReference
    print(sr_obj.name)
    print(sr_obj.type)

    field_list = desc_obj.fields
    for field in field_list:
        # print(field.name)
        # print(field.type)
        print("The field name is {} and the type is {}".format(field.name, field.type))
