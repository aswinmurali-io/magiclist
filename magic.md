magic module[¶](#module-magic "Permalink to this headline")
===========================================================

 *class*`magic.`{.sig-prename .descclassname}`Magic`{.sig-name .descname}(*name: str*)[¶](#magic.Magic "Permalink to this definition")
:   Bases: `object`{.xref .py .py-class .docutils .literal .notranslate}

     `append`{.sig-name .descname}(*key: str*, *item: any*) → None[¶](#magic.Magic.append "Permalink to this definition")
    :   The append(…) function can be used to append a new element into
        the magic list.

        Args:
        :   key (str): The key used for accessing the data. item (any):
            The content to store in the magic list with that above key
            as reference.

     `append_parallel`{.sig-name .descname}(*items: dict*) → None[¶](#magic.Magic.append_parallel "Permalink to this definition")
    :   The append\_parallel(…) function can be used to batch append
        elements to the list.

        Args:
        :   items (dict): The dict of data to be added to the magiclist.

     `get`{.sig-name .descname}(*key: str*) → any[¶](#magic.Magic.get "Permalink to this definition")
    :   The get(…) function is used to get an element from the magiclist
        via the key.

        Args:
        :   key (str): The key used for accessing the data.

        Returns:
        :   any: Get the element asked for via the key.

     `gets`{.sig-name .descname}(*keys: iter*) → list[¶](#magic.Magic.gets "Permalink to this definition")
    :   The gets(…) function is used to batch get elements w.r.t to all
        the keys specified

        Args:
        :   keys (iter): The keys used for accessing the datas.

        Returns:
        :   list: Get all the elements asked for via the keys.

     `load`{.sig-name .descname}() → bool[¶](#magic.Magic.load "Permalink to this definition")
    :   The load() function can be used to load the previous data state
        from the storage device.

        Returns:
        :   bool: If loaded successfully or not

     `purge`{.sig-name .descname}()[¶](#magic.Magic.purge "Permalink to this definition")
    :   The purge() function will release less used elements from memory
        reducing the memory size of the list.

     `sync`{.sig-name .descname}(*key: str*, *item: any*, *access\_count: int*, *trend\_ratio: int*) → None[¶](#magic.Magic.sync "Permalink to this definition")
    :   The sync function can be used to sync the data changes given in
        the function args to the in-memory magic list and to the
        storge-based (async) magiclist.

        Args:
        :   key (str): The key used for accessing the data. item (any):
            The content to store in the magic list with that above key
            as reference. access\_count (int): The number of times the
            elements is been accessed. trend\_ratio (int): The
            access\_count w.r.t. to a specific time interval.

[magiclist](../index.html) {.logo}
==========================

### Navigation

### Related Topics

-   [Documentation overview](../index.html)

### Quick search {#searchlabel}

©2020, Aswin Murali, Abhinav Basil Shinow, Kashinadh S Nair. | Powered
by [Sphinx 3.2.1](http://sphinx-doc.org/) & [Alabaster
0.7.12](https://github.com/bitprophet/alabaster) | [Page
source](../_sources/docs/magic.rst.txt)
