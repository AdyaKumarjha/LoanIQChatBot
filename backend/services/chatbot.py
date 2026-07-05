from services.agent import agent


class LoanChatbot:

    def reply(self, message: str):
        return agent.execute(message)


chatbot = LoanChatbot()