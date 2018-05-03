"""
 * By Alejandro G (Jano)
 * 03/05/2018
 * github.com/imthejano
 * facebook.com/imthejano
 * twitter.com/imthejano
"""

import pyaudio
import wave
import sys

class WavePack:
    def __init__(self,frames,packPath,packName,nWavs):
        self.packName=packName
        self.packPath=packPath
        self.frames=frames
        self.nWavs=nWavs
        self.wavs=[]
        print("Pack name: "+packName+"\nPath: "+packPath+"\nn Wavs: "+str(nWavs))
        
    def loadPack(self):
         for i in range(0, self.nWavs):
             self.wavs.append("")
             self.wavs[i]=Wave(self.packPath,str(i)+".wav",self.frames)
             print("Loading pack...\n " +str(i)+".wav"+"pack: "+self.packName)
             
    def play (self,index):
        self.wavs[index].play()
        
    def isPlaying (self,index):
        return self.wavs[index].isPlaying

class Wave:
    
    def load(self):
        try:
            self.wav=wave.open(self.filePath,'rb')
        except:
            print("Unexpected error: "+sys.exc_info()[0])
            raise
    
    def read(self):
        return self.wav.readframes(self.frames)
    
    def start(self):
        try:
            self.pyAud = pyaudio.PyAudio()
            self.strm = (self.pyAud.open(format=self.pyAud.get_format_from_width(self.wav.getsampwidth()),
                    channels=self.wav.getnchannels(),
                    rate=self.wav.getframerate(),
                    output=True))
        except:
            print("Unexpected error:",sys.exc_info()[0])
            raise

    def play(self):
        if self.f!='':
            self.start()
            self.isPlaying=1
            self.strm.write(self.f)
            self.isPlaying=0
        self.isPlaying=0
        
    def close(self):
        self.strm.stop_stream()
        self.strm.close()
        self.pyAud.terminate()
        
    def __init__(self, path, waveFile, frames):
        self.path = path
        self.waveFile = waveFile
        self.frames = frames
        self.filePath = self.path+'/'+self.waveFile
        self.load()
        self.start()
        self.f = self.read()
