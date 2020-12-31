"""Call Center

Design simple Call Center with 3 employee.
Method dispatch_call() - assign new upcoming call
to the first free employee based on priority
Respondent -> Manager -> Director

classes: CallCenter, Respondent, Manager, Director

Instruction:

  while operation from 9am to 5pm:
      while waiting for call:
          Coming call # as input()
          while someone didn't picked the call up:
              if Respondent is not free:
                  move call to Manager
                  if Manager is not free
                      move call to Director
                      if Director is not free:
                          wait until someone becomes free:
                            # in appropeiate sequence 
                      else:
                          Director takes call
                  else:
                      Manager takes call
              else:
                  Responder takes call
           Call was picked up by first free employee

"""

import random


class CallCenter:

    def __init__(self):
        respondent = Respondent()
        manager = Manager()
        director = Director()
        self.team = [respondent, manager, director]
        self.current_calls = 0
        self.calls_at_moment = len(self.team)

    # class CallActionData:
    #     def __init__(self):
    #         self.data = []

    def dispatch_call(self):
        while self.current_calls == self.calls_at_moment:
            for team_member in self.team:
                if not team_member.is_free:
                    if not team_member.is_on_call():
                        self.update_calls_and_employee("End Call", team_member)
                        print("Call was finished by ", team_member.name, ". Current calls ", self.current_calls)

        free_employee = self.get_free_employee()
        self.update_calls_and_employee("Start Call", free_employee)
        print("Call is taken by ", free_employee.name, ". Current calls ", self.current_calls)

    def update_calls_and_employee(self, call_action, person):
        if call_action == "Start Call":
            person.take_call()
            call = 1
        elif call_action == "End Call":
            person.end_call()
            call = -1
        else:
            call = 0
        self.current_calls += call

    def get_free_employee(self):
        team_member = -1
        for team_member in self.team:
            if team_member.is_free:
                break
        return team_member


class Respondent:

    def __init__(self):
        self.is_free = True
        self.name = "Respondent"
        self.random_coefficient = 4

    def take_call(self):
        self.is_free = False

    def end_call(self):
        self.is_free = True

    def is_on_call(self):
        if self.is_call_finished():
            self.end_call()
            return False
        return True

    def is_call_finished(self):
        threshold_parameter = random.randint(0, 100)
        threshold_level = 100 // self.random_coefficient
        if threshold_parameter >= threshold_level:
            return True
        else:
            return False


class Manager:

    def __init__(self):
        self.is_free = True
        self.name = "Manager"
        self.random_coefficient = 6

    def take_call(self):
        self.is_free = False

    def end_call(self):
        self.is_free = True

    def is_on_call(self):
        if self.is_call_finished():
            self.end_call()
            return False
        return True

    def is_call_finished(self):
        threshold_parameter = random.randint(0, 100)
        threshold_level = 100 // self.random_coefficient
        if threshold_parameter >= threshold_level:
            return True
        else:
            return False


class Director:

    def __init__(self):
        self.is_free = True
        self.name = "Director"
        self.random_coefficient = 8

    def take_call(self):
        self.is_free = False

    def end_call(self):
        self.is_free = True

    def is_on_call(self):
        if self.is_call_finished():
            self.end_call()
            return False
        return True

    def is_call_finished(self):
        threshold_parameter = random.randint(0, 100)
        threshold_level = 100 // self.random_coefficient
        if threshold_parameter >= threshold_level:
            return True
        else:
            return False


if __name__ == '__main__':

    call_center = CallCenter()
    while True:
        new_call = type(str) == input()
        call_center.dispatch_call()
