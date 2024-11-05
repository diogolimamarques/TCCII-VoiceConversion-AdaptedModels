from discrete_speech_metrics.mcd import MCD
from scipy.io import wavfile

scorer = MCD()
score = 0

for i in range(5):

    sample_rate, ref_wav= wavfile.read('.\\discrete_speech_metrics\\evaluation\\TARGET\\wav ('+str(i+1)+').wav')
    sample_rate, gen_wav= wavfile.read('.\\discrete_speech_metrics\\evaluation\\GENERATED\\wav ('+str(i+1)+').wav')

    score += scorer.score(ref_wav, gen_wav)


print("A pontuação MCD foi: "+str(score/5))