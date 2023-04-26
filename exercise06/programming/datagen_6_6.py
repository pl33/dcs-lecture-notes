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


T_START = 0.0
T_END = 4.0
N_SAMPLES = 1024


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


def main():
    """
    Entry point
    """
    np.random.seed(10000)
    
    t = np.linspace(T_START, T_END, N_SAMPLES)
    fft_bin_diff = 1 / (T_END - T_START)
    
    s1 = make_signal(t, 1500.0, fft_bin_diff * 2.0, 0)
    s2 = make_signal(t, 2000.0, fft_bin_diff * 48.0, np.pi / 2)
    noise = np.random.normal(0, 256.0, len(t))
    
    signal = (s1 + s2 + noise).astype(np.int16)
    data = signal.tobytes()
    with open("data_6_6.dat", "wb") as fh:
        fh.write(data)
    

if __name__ == "__main__":
    main()


