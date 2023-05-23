#!/usr/bin/env python3

class MyString:
  def __init__(self, value=None):
      self._value = None
      if value is not None:
          self.value = value

  @property
  def value(self):
      return self._value
  
  @value.setter
  def value(self, value):
      if not isinstance(value, str):
          print("The value must be a string.")
      else:
          self._value = value

  def is_sentence(self):
      return self._value.endswith('.')
  
  def is_question(self):
      return self._value.endswith("?")
  
  def is_exclamation(self):
      return self._value.endswith("!")
  
  def count_sentences(self):
      if self._value is None:
          return 0
      count = 0
      for char in self._value:
          if char in ['.', '?', '!']:
              count += 1
      return count
  

