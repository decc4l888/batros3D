import trimesh

# STL'yi yükle
mesh = trimesh.load_mesh("iha.stl")

# Hacim (mm³ -> cm³)
volume_cm3 = mesh.volume / 1000

# ASA yoğunluğu
density = 1.07  # g/cm³

# Hedef toplam ağırlık (örneğin 300 gram altında kalmak istiyoruz)
target_weight = 1025
# Gereken doluluk oranını hesapla
required_infill = target_weight / (volume_cm3 * density)

# Oran %100'ü geçiyorsa bu tasarımı hafifletmen gerekir
if required_infill > 1:
    print("Tasarım çok ağır, yeniden tasarlaman gerekebilir.")
else:
    print(f"Bu ağırlıkla kalmak için gereken doluluk oranı: %{required_infill * 100:.1f}")
