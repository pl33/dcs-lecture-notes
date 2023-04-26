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
import matplotlib.pyplot as plt


N_SAMPLES = 64      # Number of samples per symbol
SYMBOL_RATE = 2     # Symbols per second
CARRIER_AMPLITUDE = 1.0
CARRIER_FREQUENCY = 6
CARRIER_PHASE_DEG = 0


def make_psk_signal(t, phase_rad):
    """
    Make PSK-modulated signal
    
    :param t: Vector of time points
    :param phase_rad: Signal fed into the PSK phase rotator (length must be length of t)
    :return: Vector of signal points corresponding to the time points in t
    """
    signal = #TODO
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


def plot(title, symbols, n):
    """
    Make plot for PSK signal
    
    :param title: Plot title
    :param symbols: Vector of symbols
    :param n: Number of PSK steps in the n-PSK (2 = BPSK, 4 = QPSK, ...)
    """
    t = np.linspace(0, len(symbols) / SYMBOL_RATE, N_SAMPLES * len(symbols))
    
    # Create a signal from the data symbols
    symbol_signal = make_symbol_signal(t, symbols)
    
    # Get the phase spacing between two symbols in the PSK constellation
    phase_step = # TODO
    # Convert the symbol signal into the signal containing the desired phase shift of the carrier
    phase_signal = symbol_signal * phase_step
    
    # PSK modulation happens now
    psk_signal = make_psk_signal(t, phase_signal)
    
    # Plot everything
    fig, (ax1, ax2) = plt.subplots(2, 1, num=title)
    ax1.set_title("Symbols")
    ax1.plot(t, symbol_signal)
    ax2.set_title("PSK")
    ax2.plot(t, psk_signal)


def main():
    """
    Entry point
    """
    plot("BPSK", [0, 0, 1, 0, 1, 1, 0, 1], 2)
    plot("QPSK", [0, 1, 3, 2], 4)
    plt.show()
    

if __name__ == "__main__":
    main()


