# pylint: disable=missing-function-docstring
"""Test comm.p2p.DistP2pContext."""
import os
import unittest
import torch
from edgepipe.comm.p2p import DistP2pContext

MASTER_ADDR = 'localhost'
MASTER_PORT = '29501'


def _cmd_cb(cmd, tensors):
    assert isinstance(cmd, int)
    assert isinstance(tensors, tuple)
    for tensor in tensors:
        assert isinstance(tensor, torch.Tensor)


class TestDistP2pContext(unittest.TestCase):
    """Test DistP2pContext."""

    @classmethod
    def setUpClass(cls):
        os.environ['MASTER_ADDR'] = MASTER_ADDR
        os.environ['MASTER_PORT'] = MASTER_PORT

    def test_lifecycle(self):
        # pylint: disable=no-self-use
        ctx = DistP2pContext(1, 0, _cmd_cb)
        ctx.init()
        ctx.shutdown()

    def test_context(self):
        # pylint: disable=no-self-use
        with DistP2pContext(1, 0, _cmd_cb):
            pass
