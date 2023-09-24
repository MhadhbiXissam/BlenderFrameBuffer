import bpy , json , os




output_path = bpy.context.blend_data.filepath + ".png"
shared_data = os.path.join(os.path.dirname(output_path),"shared_data.json")
print(json.dumps({"img" : output_path }) , file = open(shared_data,"w"))



def my_timer_callback():
	# Set the render resolution to match the current view
	bpy.context.scene.render.resolution_x = 800
	bpy.context.scene.render.resolution_y = 800

	# Set the output file format and path
	bpy.context.scene.render.image_settings.file_format = 'PNG'
	bpy.context.scene.render.filepath = output_path

	# Render the image
	bpy.ops.render.opengl(write_still=True)
	return 1 # Set the interval for the next callback in seconds

# Register the timer callback
bpy.app.timers.register(my_timer_callback)