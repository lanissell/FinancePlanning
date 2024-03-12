from FinancePlanning.Models.Goal import Goal


class GoalRepository:

    def __init__(self):
        self.goals: list[Goal] = []

    def GetAll(self):
        return self.goals

    def GetById(self, goal_id):
        return next(goal for goal in self.goals if goal["goal_id"] == goal_id)

    def Add(self, goal: Goal):
        self.goals.append(goal)

    def DeleteById(self, goal_id):
        self.goals.remove(self.GetById(goal_id))

    def Update(self, goal_id, new_goal: Goal):
        index = 0

        for goal in self.goals:
            if goal.goal_id == goal_id:
                self.goals[index] = Goal(index, new_goal.goal_id, new_goal.name, new_goal.price, new_goal.closed)
