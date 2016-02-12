

def cell_is_highlighted(cell_meta):
	if cell_background(cell_meta) == 'none':
		return False
	else:
		return True

def get_color_name(rgb):
	colors = {
			'blue' 		: [(204, 204, 255)],
			'red'		: [(255, 0, 0)],
			'vivid_red'	: [(221, 8, 6)],
			'green_tone': [(31, 183, 20)],

			'yellow'	: [(255,255,0)],
			'white'		: [(255,255,255)],
			'orange'	:[(255, 102, 0)],
			'orange_four'	:[(254, 167, 70)],
			'shades_yellow':[(252, 243, 5)],
			'green'		: [(0, 255, 0)],
			'gray_tone'		: [(128, 128, 128)],
			'grey'		: [(221, 221, 221)]
			}
	if rgb == None:
		return None
	else:
		for color, rgbs in colors.items():
			if rgb in rgbs:
				return color
		return rgb
