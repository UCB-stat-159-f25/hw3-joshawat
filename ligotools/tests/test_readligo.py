import pytest
import numpy as np
from ligotools import readligo

def test_dq_channel_to_seglist_basic():
    """Test dq_channel_to_seglist with simple input - should find data segments"""
    # Create a DQ channel: 1=good data, 0=bad data
    # This represents: good data at [0-2] and [4-6], bad data at [2-4]
    dq_channel = np.array([1, 1, 0, 0, 1, 1])
    
    segments = readligo.dq_channel_to_seglist(dq_channel, fs=1)
    
    # Should return list of slices where data is good
    assert isinstance(segments, list)
    assert len(segments) == 2  # Two segments of good data
    
    # Check the slices point to the correct ranges
    assert segments[0].start == 0  # First segment starts at index 0
    assert segments[0].stop == 2   # First segment ends at index 2
    assert segments[1].start == 4  # Second segment starts at index 4  
    assert segments[1].stop == 6   # Second segment ends at index 6

def test_dq_channel_to_seglist_empty():
    """Test dq_channel_to_seglist with all bad data - should return no segments"""
    # All zeros means no good data anywhere
    dq_channel = np.array([0, 0, 0, 0])
    
    segments = readligo.dq_channel_to_seglist(dq_channel, fs=1)
    
    # Should return empty list when no good data segments
    assert isinstance(segments, list)
    assert len(segments) == 0  # No segments found