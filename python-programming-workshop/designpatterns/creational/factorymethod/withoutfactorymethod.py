# Python Code for Object
# Oriented Concepts without
# using Factory method

class FrenchTranslator:

	""" it simply returns the french version """

	def __init__(self):

		self.translations = {"car": "voiture", "bike": "bicyclette",
							"cycle":"cyclette"}

	def translate(self, message):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class SpanishTranslator:
	"""it simply returns the spanish version"""

	def __init__(self):

		self.translations = {"car": "coche", "bike": "bicicleta",
							"cycle":"ciclo"}

	def translate(self, msg):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class EnglishTranslator:
	"""Simply return the same message"""

	def translate(self, msg):
		return msg

if __name__ == "__main__":

	# main method to call others
	f = FrenchTranslator()
	e = EnglishTranslator()
	s = SpanishTranslator()

	# list of strings
	message = ["car", "bike", "cycle"]

	for msg in message:
		print(f.translate(msg))
		print(e.translate(msg))
		print(s.translate(msg))
