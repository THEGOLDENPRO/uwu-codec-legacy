from .codec import UwUCodec

class UwUStreamWriter(UwUCodec): # Copy of codecs.StreamWriter but for the uwu codec.
    def __init__(self, stream, errors = "strict"):
        self.stream = stream
        self.errors = errors

    def write(self, object):
        """Writes the object's contents encoded to self.stream."""
        data, consumed = self.encode(object, self.errors)
        self.stream.write(data)

    def writelines(self, list):
        """Writes the concatenated list of strings to the stream using .write()."""
        self.write(''.join(list))

    def reset(self):
        """
        Flushes and resets the codec buffers used for keeping state.

        Calling this method should ensure that the data on the
        output is put into a clean state, that allows appending
        of new fresh data without having to rescan the whole
        stream to recover state.
        """
        pass

    def seek(self, offset, whence = 0):
        self.stream.seek(offset, whence)
        if whence == 0 and offset == 0:
            self.reset()

    def __getattr__(self, name, getattr=getattr):
        """Inherit all other methods from the underlying stream."""
        return getattr(self.stream, name)

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.stream.close()