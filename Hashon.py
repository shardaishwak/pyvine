
class Encoder:
	def __init__(self, code, list_hashes):
		self.code = code
		self.list_hashes = list_hashes

	def encode(self):
		ap_code = [2,9]

	
		encode_s1 = []

		def_code = 0
		def_codes = {
			"a": 2,
			"b": 6244,
			"c": "429hjf&5637",
			"d": 333770,
			"e": 318,
			"f": 338264,
			"g": 6394,
			"h": 97,
			"i": "4838QRT9jf7259f$54",
			"j": 38838682,
			"k": "6fd$",
			"l": 17,
			"m": 975,
			"n": 4964,
			"o": "j03",
			"p": 286,
			"q": 44,
			"r": 106,
			"s": 84,
			"t": "fh40I07",
			"u": 87,
			"v": 398,
			"w": 24,
			"x": 47,
			"y": 3984,
			"z": 39,
			"0": "u73GY",
			"1": 75494,
			"2": "TB4o",
			"3": 8026,
			"4": "7BposG4",
			"5": "g9tjQ",
			"6": "zbt85",
			"7": 98664,
			"8": "ufh58",
			"9": "ql$6"
		}

		for i in self.code:
			for j in def_codes:
				lcl =def_codes[i]
				if type(lcl) is str:
					def_code = lcl
				else:
					def_code = lcl*ap_code[0]*ap_code[1]

			encode_s1.append(def_code)
		concatanation = ''.join(map(str, encode_s1))
		self.list_hashes.append({
			"code": self.code,
			"hash": concatanation
			})
		print(f"Hash§: {concatanation}")

