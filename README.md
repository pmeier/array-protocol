# Array protocol playground

This repository provides a playground for a vendorable protocol for array objects that can be used to statically as well as at runtime check for adherence to the [Array API](https://github.com/data-apis/array-api). You can find a discussion in [this thread](https://github.com/data-apis/array-api/issues/229).

`consumer.py` implements a "vendored" version of the proposed protocol and `provider` implements a dummy array object adhering to it. 

- The static checks can be run by `mypy static_checks.py`
- The runtime checks can be run by `python runtime_checks.py`