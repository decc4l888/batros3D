import trimesh
mesh = trimesh.load_mesh("iha.stl")
volume_cm3 = mesh.volume / 1000
density = 1.07  
target_weight = 1025
required_infill = target_weight / (volume_cm3 * density)
if required_infill > 1:
    print("tasarım çok ağır")
else:
    print("gereken doluluk oranı: %{required_infill * 100:.1f}")
