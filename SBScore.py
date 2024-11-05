import numpy as np
import warnings
from scipy.io import wavfile
warnings.filterwarnings('ignore')
precision = 0

from discrete_speech_metrics import SpeechBERTScore

for i in range(5):
    # Load the .wav file
    sample_rate, ref_wav= wavfile.read('.\\discrete_speech_metrics\\evaluation\\TARGET\\wav ('+str(i+1)+').wav')
    sample_rate, gen_wav= wavfile.read('.\\discrete_speech_metrics\\evaluation\\GENERATED\\wav ('+str(i+1)+').wav')

    metrics = SpeechBERTScore(
        sr=16000,
        model_type="wavlm-large",
        layer=14,
        use_gpu=True)
    prec, _, _ = metrics.score(ref_wav, gen_wav)
    precision += prec

print(f"SpeechBERTScore: {precision/5}")