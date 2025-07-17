from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import logging
logger = logging.getLogger(__name__)

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        try:
            user_message = json.loads(request.body).get("message")
            logger.info(f"Received message: {user_message}")  # Check if the message is received correctly
            
            if user_message is None:
                return JsonResponse({"response": "No message provided."}, status=400)
            
           
            responses = {
                "hello": "Hi there! How can I assist you today?",
                "how are you?": "I'm just a bot, but thanks for asking!",
                "bye": "Goodbye! Have a great day!",
                "exercise": "Here are some exercises you can do today: Push-ups, Squats, and Crunches.",
                "bmi": "To calculate your BMI, please provide your weight and height.",
                "what is your name?": "I am FitnessBot, here to help you with fitness and health-related queries!",
                
                }

            bot_message = responses.get(user_message.lower(), "Sorry, I don't understand :( ")

            logger.info(f"Bot response: {bot_message}")  # Log the bot response
            return JsonResponse({"response": bot_message})
        
        except json.JSONDecodeError:
            return JsonResponse({"response": "Invalid JSON."}, status=400)
    
    return JsonResponse({"response": "Invalid request."}, status=400)


# Index view for rendering the chatbot interface
def index(request):
    return render(request, 'chatbot/index.html')  # Ensure you have this template in your templates folder
