from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech


def quickstart_v2(
    project_id: str,
    audio_file: str,
) -> cloud_speech.RecognizeResponse:
    """Transcribe an audio file."""
    # Instantiates a client
    client = SpeechClient()

    # Reads a file as bytes
    with open(audio_file, "rb") as f:
        content = f.read()

    config = cloud_speech.RecognitionConfig(
        auto_decoding_config={}, language_codes=["en-US"], model="latest_long"
    )

    request = cloud_speech.RecognizeRequest(
        recognizer=f"projects/{project_id}/locations/global/recognizers/_",
        config=config,
        content=content,
    )

    # Transcribes the audio into text
    response = client.recognize(request=request)

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

    return response


my_project_id = "adroit-metric-384510"
my_audio_file = "myAudio.mp3"

responseFromGoogle = quickstart_v2(my_project_id, my_audio_file)

audioTranscript = ''.join(result.alternatives[0].transcript
                          for result in responseFromGoogle.results)
print(audioTranscript)