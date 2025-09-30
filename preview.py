import bpy

bpy.ops.wm.open_mainfile(filepath="./project.blend")

bpy.context.scene.render.resolution_x = 256
bpy.context.scene.render.resolution_y = 256
bpy.context.scene.render.resolution_percentage = 100

bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = "./thumbnail.png"

bpy.ops.render.render(write_still=True)