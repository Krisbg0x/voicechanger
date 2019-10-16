import pyaudio
import time
import numpy as np
import struct

class Voicechanger():

    def __init__(self):
        self.WIDTH = 2
        self.CHANNELS = 2
        self.RATE = 44100
        self.INDEX = 1
        self.CHUNK = 1024*2
        self.OUTPUT_DEVICE = 5 #Discord = 5, PC-Speakers = 3
        self.delta = 0
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(self.WIDTH),
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=True,
                                  input_device_index = self.INDEX,
                                  output_device_index = self.OUTPUT_DEVICE,
                                  frames_per_buffer=self.CHUNK,
                                  stream_callback=self.callback)

    def setDelta(self, delta):
        # print("Delta has been set to",str(delta))
        self.delta = delta

    def __change_pitch(self,data,delta):
        size = len(data)/2
        format = "%dh"%(size)
        input = struct.unpack(format,data)
        f = np.fft.rfft(input)
        f = np.roll(f,delta)
        # f[0:100] = 0
        inversef = np.fft.irfft(f).astype(np.int16)
        # print([*inversef])
        return struct.pack(format, *inversef)

    def callback(self,in_data, frame_count, time_info, status):
        alt_audio = self.__change_pitch(in_data, self.delta)
        return (alt_audio, pyaudio.paContinue)

    def run(self):
        self.stream.start_stream()
    
        
    def close(self):
        self.stream.stop_stream()
        # self.stream.close()
        # self.p.terminate()