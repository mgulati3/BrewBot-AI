from agents import (GuardAgent,
                    ClassificationAgent, 
                    DetailsAgent,
                    AgentProtocol, 
                    RecommendationAgent,
                    OrderTakingAgent
                )
from typing import Dict
import os
import pathlib
folder_path = pathlib.Path(__file__).parent.resolve()

class AgentController():
    def __init__(self):
        self.guard_agent = GuardAgent()
        self.classification_agent = ClassificationAgent()
        self.recommendation_agent = RecommendationAgent('recommendation_objects/apriori_recommendations.json',
                                                    'recommendation_objects/popularity_recommendation.csv'
                                                    )
        self.agent_dict: dict[str, AgentProtocol] = {
            "details_agent": DetailsAgent(),
            "recommendation_agent": self.recommendation_agent,
            "order_taking_agent": OrderTakingAgent(self.recommendation_agent)
        }
    
    def get_response(self, input):

        # Extract user input
        job_input = input["input"]
        messages = job_input["messages"]

        # Get guard agent response
        guard_agent_response = self.guard_agent.get_response(messages)
        if guard_agent_response["memory"]["guard_decision"] == "not allowed":
            messages.append(guard_agent_response)
            return guard_agent_response

        # Get Claasification Agent's response
        classification_agent_response = self.classification_agent.get_response(messages)
        chosen_agent = classification_agent_response["memory"]["classification_decision"]

        # Get the chosen agent's response
        agent = self.agent_dict[chosen_agent]
        response = agent.get_response(messages)

        return response

