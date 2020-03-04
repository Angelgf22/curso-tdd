from enum import Enum

IssueState = Enum('IssueState', 'Open Closed')

class Issue:

    def __init__(self):
        self.state = IssueState.Open