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

# Original data for later checking
ORIGINAL_DATA = np.array(
    [
        [+1, +1, -1, -1, +1, -1, +1, -1],
        [-1, +1, -1, -1, +1, +1, -1, -1],
        [+1, -1, -1, +1, +1, -1, -1, +1],
        [-1, -1, -1, -1, +1, +1, +1, +1],
    ]
)
    
# Number of OFDM carriers
NOF_CARRIERS = 16
    
# Number of training/synchronization OFDM carriers
NOF_SYNC = 8

# Decision boundaries. When the output of the accumulator is evaluated (at decoder),
# everything above is considered a logical HIGH (1) and everything
# below is considered a logical LOW (0).
DECISION_BOUNDARY = 0


def decode(carrier):
    """
    BPSK decoder
    
    :param carrier: Carrier of FFT
    :return: Decoded data
    """
    if np.real(carrier) >= DECISION_BOUNDARY:
        return +1
    else:
        return -1


def main():
    """
    Entry point
    """
    # Load received signal.
    # - The signal is OFDM modulated
    # - Each carrier is BPSK modulated
    # - It is noise-free
    # - Carriers 0, 1, 2, 3, -1, -2, -3, -4 are training/synchronization carriers. They are always +1 at transmission
    # - Carrier-to-data mapping:
    #     Carrier 4  -> Bit 0
    #     Carrier 5  -> Bit 1
    #     Carrier 6  -> Bit 2
    #     Carrier 7  -> Bit 3
    #     Carrier 11 -> Bit 4
    #     Carrier 10 -> Bit 5
    #     Carrier 9  -> Bit 6
    #     Carrier 8  -> Bit 7
    with open("data_7_6_ofdm.dat", "rb") as fh:
        adc = np.frombuffer(fh.read(), dtype=np.int16).reshape((-1, 2))
        # Real and imaginary part are stored as two integers. Combine them to a complex number.
        signal = adc[:, 0] + (1.j * adc[:, 1])
        
    # Number of frames
    nof_frames = int(signal.shape[0] / NOF_CARRIERS)
    
    # Allocate memory for FFT / carriers per frame
    carriers = np.zeros((nof_frames, NOF_CARRIERS), dtype=np.complex128)
    
    # FFT of all frames
    for frame_index in range(nof_frames):
        # Windowing with rectangular window
        extract = signal[(frame_index * NOF_CARRIERS):((frame_index + 1) * NOF_CARRIERS)]
        
        # FFT
        carriers[frame_index, :] = np.fft.fft(extract)
        
    # TODO: Is something missing here? -> Carrier synchronization
    # Get phase offset from synchronization carriers
    phase_offset = np.angle(
        np.average(
            np.concatenate(
                [carriers[0:4], carriers[12:16]]
            )
        )
    )
    print(f"The phase offset is {phase_offset} rad / {180 * phase_offset / np.pi} deg")
    # Phase correction
    carriers *= np.exp(-1j * phase_offset)
    
    # Data decoding
    data = np.zeros((nof_frames, (NOF_CARRIERS - NOF_SYNC)), dtype=np.int32)
    for frame_index in range(nof_frames):
        # Do reverse mapping
        data[frame_index, 0] = decode(carriers[frame_index, 4])
        data[frame_index, 1] = decode(carriers[frame_index, 5])
        data[frame_index, 2] = decode(carriers[frame_index, 6])
        data[frame_index, 3] = decode(carriers[frame_index, 7])
        data[frame_index, 4] = decode(carriers[frame_index, 11])
        data[frame_index, 5] = decode(carriers[frame_index, 10])
        data[frame_index, 6] = decode(carriers[frame_index, 9])
        data[frame_index, 7] = decode(carriers[frame_index, 8])
    
    # Check data
    if (data == ORIGINAL_DATA).all():
        print("Your solution is correct")
    else:
        raise AssertionError(f"Data mismatch: {data} != {ORIGINAL_DATA}")


if __name__ == "__main__":
    main()
