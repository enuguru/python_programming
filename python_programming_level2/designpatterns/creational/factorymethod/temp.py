
# Python Code for factory method under creational design pattern

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

def Factory(language ="English"):

	"""Factory Method"""
	translators = {
		"French": FrenchTranslator,
		"English": EnglishTranslator,
		"Spanish": SpanishTranslator,
	}

	return translators[language]()

#if __name__ == "__main__":

#	f = Factory("French")
#	e = Factory("English")
#	s = Factory("Spanish")

message = ["car", "bike", "cycle"]

for msg in message:
	print(Factory("French").translate(msg))
	print(Factory("English").translate(msg))
	print(Factory("Spanish").translate(msg))
	#print(e.translate(msg))
	#print(s.translate(msg))
