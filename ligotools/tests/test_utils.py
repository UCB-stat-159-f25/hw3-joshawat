import pytest
import numpy as np
import os
from ligotools.utils import whiten, write_wavfile, reqshift

def test_whiten_returns_array():
    """Test that whiten returns numpy array with correct shape"""
    dt = 1.0/4096
    strain = np.random.random(1024)  # Random test data
    simple_psd = lambda freqs: np.ones_like(freqs) * 1e-40
    
    result = whiten(strain, simple_psd, dt)
    assert isinstance(result, np.ndarray)
    assert result.shape == strain.shape

def test_write_wavfile_creates_file():
    """Test that write_wavfile creates a file"""
    fs = 44100
    data = np.random.random(44100)  # 1 second of random audio
    test_filename = "test_temp.wav"
    
    write_wavfile(test_filename, fs, data)
    assert os.path.exists(test_filename)
    
    # Clean up
    if os.path.exists(test_filename):
        os.remove(test_filename)

def test_reqshift_returns_array():
    """Test that reqshift returns numpy array with correct shape"""
    sample_rate = 4096
    data = np.random.random(4096)  # 1 second of random data
    fshift = 100
    
    result = reqshift(data, fshift=fshift, sample_rate=sample_rate)
    assert isinstance(result, np.ndarray)
    assert result.shape == data.shape