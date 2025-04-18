import trimesh

# STL dosyasını yükle
mesh =trimesh.load_mesh('govde.stl')

# Hacim mm³ cinsinden gelir, cm³'e çevirelim
volume_cm3 = mesh.volume / 1000

# ASA yoğunluğu (g/cm³)
density = 1.07

# Doluluk oranı (örnek: %20)
infill_ratio = 0.60

# Ağırlık = hacim × yoğunluk × doluluk oranı
weight = volume_cm3 * density * infill_ratio

print(f"ASA ile tahmini ağırlık (infill %{int(infill_ratio*100)}): {weight:.2f} gram")
