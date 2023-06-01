from .codec import UwUCodec

class UwUStreamReader(UwUCodec): # Code hijacked from codecs.StreamReader but instead inheriting from the uwu codec.
    charbuffertype = str

    def __init__(self, stream, errors = "strict"):
        """
        Creates a StreamReader instance.

            stream must be a file-like object open for reading.

            The StreamReader may use different error handling
            schemes by providing the errors keyword argument. These
            parameters are predefined:

                'strict' - raise a ValueError (or a subclass)
                'ignore' - ignore the character and continue with the next
                'replace'- replace with a suitable replacement character
                'backslashreplace' - Replace with backslashed escape sequences;

            The set of allowed parameter values can be extended via
            register_error.
        """
        self.stream = stream
        self.errors = errors
        self.bytebuffer = b""
        self._empty_charbuffer = self.charbuffertype()
        self.charbuffer = self._empty_charbuffer
        self.linebuffer = None

    def read(self, size = -1, chars = -1, firstline = False):
        """
        Decodes data from the stream self.stream and returns the
        resulting object.

        chars indicates the number of decoded code points or bytes to
        return. read() will never return more data than requested,
        but it might return less, if there is not enough available.

        size indicates the approximate maximum number of decoded
        bytes or code points to read for decoding. The decoder
        can modify this setting as appropriate. The default value
        -1 indicates to read and decode as much as possible.  size
        is intended to prevent having to decode huge files in one
        step.

        If firstline is true, and a UnicodeDecodeError happens
        after the first line terminator in the input only the first line
        will be returned, the rest of the input will be kept until the
        next call to read().

        The method should use a greedy read strategy, meaning that
        it should read as much data as is allowed within the
        definition of the encoding and the given size, e.g.  if
        optional encoding endings or state markers are available
        on the stream, these should be read too.
        """

        # If we have lines cached, first merge them back into characters
        if self.linebuffer:
            self.charbuffer = self._empty_charbuffer.join(self.linebuffer)
            self.linebuffer = None

        if chars < 0:
            # For compatibility with other read() methods that take a
            # single argument
            chars = size

        # read until we get the required number of characters (if available)
        while True:
            # can the request be satisfied from the character buffer?
            if chars >= 0:
                if len(self.charbuffer) >= chars:
                    break
            # we need more data
            if size < 0:
                newdata = self.stream.read()
            else:
                newdata = self.stream.read(size)
            # decode bytes (those remaining from the last call included)
            data = self.bytebuffer + newdata
            if not data:
                break
            try:
                newchars, decodedbytes = self.decode(data, self.errors)
            except UnicodeDecodeError as exc:
                if firstline:
                    newchars, decodedbytes = \
                        self.decode(data[:exc.start], self.errors)
                    lines = newchars.splitlines(keepends=True)
                    if len(lines)<=1:
                        raise
                else:
                    raise
            # keep undecoded bytes until the next call
            self.bytebuffer = data[decodedbytes:]
            # put new characters in the character buffer
            self.charbuffer += newchars
            # there was no data available
            if not newdata:
                break
        if chars < 0:
            # Return everything we've got
            result = self.charbuffer
            self.charbuffer = self._empty_charbuffer
        else:
            # Return the first chars characters
            result = self.charbuffer[:chars]
            self.charbuffer = self.charbuffer[chars:]
        return result

    def readline(self, size = None, keepends = True):
        """
        Read one line from the input stream and return the
        decoded data.

        size, if given, is passed as size argument to the
        read() method.
        """
        # If we have lines cached from an earlier read, return
        # them unconditionally
        if self.linebuffer:
            line = self.linebuffer[0]
            del self.linebuffer[0]
            if len(self.linebuffer) == 1:
                # revert to charbuffer mode; we might need more data
                # next time
                self.charbuffer = self.linebuffer[0]
                self.linebuffer = None
            if not keepends:
                line = line.splitlines(keepends=False)[0]
            return line

        readsize = size or 72
        line = self._empty_charbuffer
        # If size is given, we call read() only once
        while True:
            data = self.read(readsize, firstline=True)
            if data:
                # If we're at a "\r" read one extra character (which might
                # be a "\n") to get a proper line ending. If the stream is
                # temporarily exhausted we return the wrong line ending.
                if (isinstance(data, str) and data.endswith("\r")) or \
                   (isinstance(data, bytes) and data.endswith(b"\r")):
                    data += self.read(size=1, chars=1)

            line += data
            lines = line.splitlines(keepends=True)
            if lines:
                if len(lines) > 1:
                    # More than one line result; the first line is a full line
                    # to return
                    line = lines[0]
                    del lines[0]
                    if len(lines) > 1:
                        # cache the remaining lines
                        lines[-1] += self.charbuffer
                        self.linebuffer = lines
                        self.charbuffer = None
                    else:
                        # only one remaining line, put it back into charbuffer
                        self.charbuffer = lines[0] + self.charbuffer
                    if not keepends:
                        line = line.splitlines(keepends=False)[0]
                    break
                line0withend = lines[0]
                line0withoutend = lines[0].splitlines(keepends=False)[0]
                if line0withend != line0withoutend: # We really have a line end
                    # Put the rest back together and keep it until the next call
                    self.charbuffer = self._empty_charbuffer.join(lines[1:]) + \
                                      self.charbuffer
                    if keepends:
                        line = line0withend
                    else:
                        line = line0withoutend
                    break
            # we didn't get anything or this was our only try
            if not data or size is not None:
                if line and not keepends:
                    line = line.splitlines(keepends=False)[0]
                break
            if readsize < 8000:
                readsize *= 2
        return line

    def readlines(self, sizehint = None, keepends = True):
        """
        Read all lines available on the input stream
        and return them as a list.

        Line breaks are implemented using the codec's decoder
        method and are included in the list entries.

        sizehint, if given, is ignored since there is no efficient
        way to finding the true end-of-line.
        """
        data = self.read()
        return data.splitlines(keepends)

    def reset(self):
        """
        Resets the codec buffers used for keeping state.

        Note that no stream repositioning should take place.
        This method is primarily intended to be able to recover
        from decoding errors.
        """
        self.bytebuffer = b""
        self.charbuffer = self._empty_charbuffer
        self.linebuffer = None

    def seek(self, offset, whence = 0):
        """
        Set the input stream's current position.

        Resets the codec buffers used for keeping state.
        """
        self.stream.seek(offset, whence)
        self.reset()

    def __next__(self):
        """
        Return the next decoded line from the input stream.
        """
        line = self.readline()
        if line:
            return line
        raise StopIteration

    def __iter__(self):
        return self

    def __getattr__(self, name, getattr = getattr):
        """Inherit all other methods from the underlying stream."""
        return getattr(self.stream, name)

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.stream.close()