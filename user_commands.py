import omni.kit.commands
from pxr import Usd, Gf, Sdf
import random


for i in range(10):
	prim_type = "Cube"
	prim_path = ""
	if prim_type == "Cube":
		prim_path = "/World/Cube"
	elif prim_type == "Cone":
		prim_path = "/World/Cone"

	omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
		prim_type=prim_type)

	suffix = ""
	if i > 0:
		suffix = f"_0{i}"

	omni.kit.commands.execute('TransformPrimSRT',
		path=Sdf.Path(f'{prim_path}{suffix}'),
		new_translation=Gf.Vec3d(random.uniform(-300, 300), random.uniform(-300, 300), random.uniform(-300, 300)),
		new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
		new_rotation_order=Gf.Vec3i(0, 1, 2),
		new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
		old_translation=Gf.Vec3d(0.0, 0.0, 0.0),
		old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
		old_rotation_order=Gf.Vec3i(0, 1, 2),
		old_scale=Gf.Vec3d(1.0, 1.0, 1.0))




