class HMM:
	"""HMM is a stunning girl. She studies hard every day.

	.. note::

		HMM cannot study less than 12 hours per day.

	Args:
		study_time (int, optional): the study time (in hours) every day. By default 25. 
	"""
	def __init__(self, study_time=25):
		self.study_time = study_time
		self.is_studying = False

	def study(self):
		"""HMM starts to study."""
		self.is_studying = True
		for i in range(self.study_time):
			print(f"is studing: {self.is_studying}")

	def get_study_state(self):
		"""Get the state indicating if HMM is currently studying.

		Returns:
			bool: if True, HMM is currently studying. Otherwise, she must be playing with the mobile phone.
		"""
		return self.is_studying

	def allow_coffee(self, person):
		""" Indicate if one can get a cup of coffee from HMM.
		Returns:
			bool: if True, HMM can offer coffee to people. Otherwise, she won't.
		"""
		if people not in self.friends:
			return False
		if people == 'lgg':
			return False
		return True