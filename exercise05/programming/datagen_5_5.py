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


N_SAMPLES = 64      # Number of samples per symbol
SYMBOL_RATE = 2     # Symbols per second
CARRIER_AMPLITUDE = 1.0
CARRIER_FREQUENCY = 5
CARRIER_PHASE_DEG = 0


def make_psk_signal(t, phase_rad):
    """
    Make PSK-modulated signal
    
    :param t: Vector of time points
    :param phase_rad: Signal fed into the PSK phase rotator (length must be length of t)
    :return: Vector of signal points corresponding to the time points in t
    """
    signal = CARRIER_AMPLITUDE * np.cos((2 * np.pi * CARRIER_FREQUENCY * t) + CARRIER_PHASE_DEG + phase_rad)
    return signal


def make_symbol_signal(t, symbols):
    """
    Make symbol signal
    
    Effectivly extend each symbol to occupy its complete timespan in the output vector
    
    :param t: Vector of time points
    :param symbols: Vector of symbols
    :return: Vector of symbol points corresponding to the time points in t
    """
    signal = np.zeros((len(t), ))
    for index, sym in enumerate(symbols):
        t_start = (1 / SYMBOL_RATE) * index
        t_end = (1 / SYMBOL_RATE) * (index + 1)
        mask = np.logical_and(t_start <= t, t < t_end)
        signal[mask] = sym
    return signal


def save(fname, symbols, n):
    """
    Save PSK signal to file
    
    :param fname: File name
    :param symbols: Vector of symbols
    :param n: Number of PSK steps in the n-PSK (2 = BPSK, 4 = QPSK, ...)
    """
    t = np.linspace(0, len(symbols) / SYMBOL_RATE, N_SAMPLES * len(symbols))
    
    symbol_signal = make_symbol_signal(t, symbols)
    
    phase_step = 2 * np.pi / n
    phase_signal = symbol_signal * phase_step
    
    psk_signal = make_psk_signal(t, phase_signal)
    
    data = np.array([t, psk_signal]).astype(np.float64).tobytes()
    with open(fname, "wb") as fh:
        fh.write(data)


def main():
    """
    Entry point
    """
    save("qpsk.dat", [0, 1, 3, 2], 4)
    

if __name__ == "__main__":
    main()


