#!/usr/bin/env python3

# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright 2023 Philipp Le
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.

import numpy as np
import scipy.signal
import matplotlib.pyplot as plt


T_START = 0.0
T_END = 4.0
N_SAMPLES = 512
LOCAL_OSCILLATOR_FREQUENCY = 5
LPF_CUT_OFF = 7


def make_signal(t, amplitude, frequency, phase_rad):
    """
    Make signal
    
    :param t: Vector of time points
    :param amplitude: Amplitude of the signal
    :param frequency: Frequency of the signal
    :param phase_rad: Phase shift of the signal in rad
    :return: Vector of signal points corresponding to the time points in t
    """
    y = amplitude * np.cos((2 * np.pi * frequency * t) + phase_rad)
    return y


def low_pass_filter(signal):
    """
    Low-pass filter a signal
    
    :param signal: Signal points
    :return: Points of the low-pass filtered signal
    """
    b, a = scipy.signal.butter(9, LPF_CUT_OFF, btype='low', fs=len(signal))
    zi = scipy.signal.lfilter_zi(b, a)
    z, _ = scipy.signal.lfilter(b, a, signal, zi=zi*signal[0]*0.2)
    return z


def plot(title, t, signal, lo_phase_rad):
    """
    Make plot for given situation
    
    :param title: Plot title
    :param t: Vector of time points
    :param signal: Signal points
    :param lo_phase_rad: Local osciallator phase offset in rad
    """
    # Create local osciallator (LO) signal of I and Q branch
    lo_i = make_signal(t, 1.0, LOCAL_OSCILLATOR_FREQUENCY, lo_phase_rad)
    lo_q = make_signal(t, 1.0, LOCAL_OSCILLATOR_FREQUENCY, lo_phase_rad + (np.pi / 2))
    
    # Calculate the baseband signal which is the low-pass filtered product of signal and corresponding LO branch
    base_i = low_pass_filter(signal * lo_i)
    base_q = low_pass_filter(signal * lo_q)
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, num=f"Sub-task {title}")
    ax1.plot(t, signal, label="Signal")
    ax2.plot(t, lo_i, label="LO In-phase")
    ax2.plot(t, lo_q, label="LO Quadarature")
    ax3.plot(t, base_i, label="Baseband In-phase")
    ax3.plot(t, base_q, label="Baseband Quadarature")


def main():
    """
    Entry point
    """
    t = np.linspace(T_START, T_END, N_SAMPLES)
    plot("1", t, make_signal(t, 2.0, 6.0, 0), 0)
    plot("2", t, make_signal(t, 2.0, 4.0, 0), 0)
    plot("3", t, make_signal(t, 2.0, 5.0, 0), 0)
    plot("4", t, make_signal(t, 2.0, 5.0, np.pi / 2), 0)
    
    # Load ADC data with QPSK signal from file
    with open("qpsk.dat", "rb") as fh:
        data = np.frombuffer(fh.read(), dtype=np.float64).reshape((2, -1))
        # Extract time points
        t_psk = data[0]
        # Extract ADC Values
        signal_psk = data[1]
    plot("5", t_psk, signal_psk, 0)
    plot("6", t_psk, signal_psk, np.pi / 2)
    
    plt.show()
    

if __name__ == "__main__":
    main()


