import arcpy
import os

file_GDB_path = r"D:\Sem-3\Programming for GIS-3\P2_Describing_Data\Practical_2_ProProject\Practical_2_ProProject\02_Describing_Data.gdb"

# Feature class names
majorAttractions_fc_name = "MajorAttractions"
freeways_fc_name = "Freeways"

# Joining the path
majorAttraction_fc_full_path = os.path.join(file_GDB_path,majorAttractions_fc_name)
print(majorAttraction_fc_full_path)
freeways_fc_full_path = os.path.join(file_GDB_path,freeways_fc_name)

majorAttractions_Feature_class_path = r"D:\Sem-3\Programming for GIS-3\P2_Describing_Data\Practical_2_ProProject\Practical_2_ProProject\02_Describing_Data.gdb\MajorAttractions"
freeways_desc_obj = arcpy.Describe(freeways_fc_full_path)

# Creating a Describe object
majorAttraction_desc_obj = arcpy.Describe(majorAttractions_Feature_class_path)
freeways_desc_obj = arcpy.Describe(freeways_fc_full_path)

# Printing the type of shape
print("The type of shape is{}".format(majorAttraction_desc_obj.shapeType))
print(freeways_desc_obj.shapeType)