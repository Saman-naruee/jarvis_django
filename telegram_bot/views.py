from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.http import require_http_methods
import json
import logging
from .webhook import TelegramBot

logger = logging.getLogger(__name__)

@csrf_exempt
@require_http_methods(["POST"])
def webhook(request):
    try:
        bot = TelegramBot.get_instance()
        update = json.loads(request.body.decode('utf-8'))
        update = bot.bot.bot.update(update)
        bot.process_update(update)
        return JsonResponse({"status": "ok"})
    except Exception as e:
        logger.error(f"Error processing update: {e}")
        return JsonResponse({"status": "error"}, status=500)