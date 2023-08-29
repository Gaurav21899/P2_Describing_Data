import arcpy
import os

file_GDB_path = r"D:\Sem-3\Programming for GIS-3\P2_Describing_Data\Practical_2_ProProject\Practical_2_ProProject\02_Describing_Data.gdb"
majorAttractions_fc_name = "MajorAttractions"

majorAttraction_fc_full_path = os.path.join(file_GDB_path,majorAttractions_fc_name)
print(majorAttraction_fc_full_path)


majorAttractions_Feature_class_path = r"D:\Sem-3\Programming for GIS-3\P2_Describing_Data\Practical_2_ProProject\Practical_2_ProProject\02_Describing_Data.gdb\MajorAttractions"

# Creating a Describe object
majorAttraction_desc_obj = arcpy.Describe(majorAttractions_Feature_class_path)

# Printing the type of shape
print("The type of shape is{}".format(majorAttraction_desc_obj.shapeType))