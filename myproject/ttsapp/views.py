from django.shortcuts import render
from django.http import HttpResponse
from gtts import gTTS
import os

def text_to_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            tts = gTTS(text=text, lang='en')
            audio_file = 'output.mp3'
            tts.save(audio_file)

            # Serve the audio file
            with open(audio_file, 'rb') as audio:
                response = HttpResponse(audio.read(), content_type='audio/mpeg')
                response['Content-Disposition'] = 'attachment; filename="output.mp3"'
                return response

    return render(request, 'ttsapp/index.html')
