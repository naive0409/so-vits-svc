from pydub import AudioSegment
from pydub.silence import split_on_silence

names = [34,35,39,41,42,43,44,46,47,48]
directory = 'datasets_raw/speaker0/'

def split(directory,filename):
    print('*'*10 + directory + filename + ".wav" + "*"*10)

    sound = AudioSegment.from_mp3(directory + filename + ".wav")
    loudness = sound.dBFS
    #print(loudness)

    chunks = split_on_silence(sound,
        # 连续沉默时间，毫秒
        min_silence_len=400,
        # 阈值dBFS
        silence_thresh=-45,
        # 插入断句时长，毫秒
        keep_silence=100
    )
    print('总分段：', len(chunks))

    # 放弃
    for i in list(range(len(chunks)))[::-1]:
        if len(chunks[i]) <= 2000 or len(chunks[i]) >= 15000:
            chunks.pop(i)
    print('取有效分段(大于2s小于15s):', len(chunks))

    for i, chunk in enumerate(chunks):
        chunk.export((directory + "splitted/{0}_{1}.wav").format(filename,i), format="wav")
        #print(i)

if __name__ == "__main__":
    for name in names:
        try:
            split(directory,str(name))
        except:
            print("skipped {}.wav".format(name))
