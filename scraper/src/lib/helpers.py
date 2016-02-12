import unicodedata
def collection_to_str(var, delimiter = ',', item_num = 1, clean = True ):
	result = ()
	#return delimiter.join(result)

	if isinstance(var, dict):
		var = var.items()

	if isinstance(var, list):
		if var[0] and isinstance(var[0], tuple):
			var = tuple_to_str_list(var, item_num, clean)

		result += tuple(filter(None, var)) if clean else tuple(var) 
	elif isinstance(var, tuple):
		result += var

	else:
		if clean and var:
			result += (var,)

	return delimiter.join(result)

def tuple_to_str_list(lst, item_num = 0, clean = True):
	result = []
	for item in lst:
		if clean:
			if item[item_num]:
				result.append(item[item_num])
		else:
			item_value = item[item_num] if item[item_num] else ''
			result.append(item_value)

	return result

def no_space_lower(str_):
	return str(str_).replace(' ', '').lower()

def str_to_float(str_, default = 0):
	try:
		return float(no_space_lower( str_.replace('$', '').replace(',', '') ))
	except:
		return default

def str_to_int(str_, default = 0):
	try:
		return int(str_to_float(str_, default))
	except:
		return default

def str_decode(string):
	if isinstance(string, unicode):
		string = unicodedata.normalize('NFKD', string).encode('ascii','ignore')
	string = str(string)
	return string
	