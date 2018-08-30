node = hou.pwd()
geo = node.geometry()

vol_res = 100
vol_geo = geo.createVolume(vol_res, vol_res, vol_res)

voxelData = [] # float

for i in range(0, vol_res * vol_res * vol_res):
    voxelData.append(0.000001 * i)

vol_geo.setAllVoxels(voxelData)

for i in range(0, vol_res):
    vol_geo.setVoxel((i,i,i), 100.0)