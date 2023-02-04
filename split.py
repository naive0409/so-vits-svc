from pydub import AudioSegment
from pydub.silence import split_on_silence

names = [34,35,39,41,42,43,44,46,47,48]

def split(filename):
    print('*'*10+filename+".wav"+"*"*10)

    sound = AudioSegment.from_mp3(filename+".wav")
    loudness = sound.dBFS
    #print(loudness)


    chunks = split_on_silence(sound,
        # must be silent for at least half a second,沉默半秒
        min_silence_len=400,

        # consider it silent if quieter than -16 dBFS
        silence_thresh=-45,
        keep_silence=100

    )
    print('总分段：', len(chunks))

    # 放弃长度小于2秒的录音片段
    for i in list(range(len(chunks)))[::-1]:
        if len(chunks[i]) <= 2000 or len(chunks[i]) >= 15000:
            chunks.pop(i)
    print('取有效分段(大于2s小于15s):', len(chunks))

    '''
    for x in range(0,int(len(sound)/1000)):
        print(x,sound[x*1000:(x+1)*1000].max_dBFS)
    '''

    for i, chunk in enumerate(chunks):
        chunk.export("splitted/{0}_{1}.wav".format(filename,i), format="wav")
        #print(i)


for name in names:
    try:
        split(str(name))
    except:
        print("skipped {}.wav".format(name))
