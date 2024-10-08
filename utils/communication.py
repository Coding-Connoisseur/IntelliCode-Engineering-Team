# collaborative_ai_team/utils/communication.py

class CommunicationChannel:
    def __init__(self):
        # Stores subscriptions where keys are agent names, and values are lists of callback functions
        self.subscriptions = {}

    def subscribe(self, agent_name, callback):
        """
        Subscribe to updates from a specific agent.
        """
        if agent_name not in self.subscriptions:
            self.subscriptions[agent_name] = []
        self.subscriptions[agent_name].append(callback)

    def publish(self, agent_name, message):
        """
        Publish a message to all subscribers of a specific agent.
        """
        if agent_name in self.subscriptions:
            for callback in self.subscriptions[agent_name]:
                callback(message)
