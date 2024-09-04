#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = ["Knowledge1", "Knowledge2"]  # Sample knowledge list

    def teach(self):
        # Returns a piece of knowledge from the list
        return self.knowledge[0] if self.knowledge else None
