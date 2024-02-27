from Models import Goal


class GoalRepository:

    def __init__(self):
        self.goals: list[Goal] = []

    def GetAll(self):
        return self.goals

    def GetById(self, goal_id):
        return next(goal for goal in self.goals if goal["goal_id"] == goal_id)

    def AddUser(self, goal: Goal):
        self.goals.append(goal)

    def DeleteUserById(self, goal_id):
        self.goals.remove(self.GetById(goal_id))

    def Update(self, goal_id, new_goals: Goal):
        for goal in self.goals:
            if goal["goal_id"] == goal_id:
                new_goals.id = goal_id
                goal.update(new_goals)
