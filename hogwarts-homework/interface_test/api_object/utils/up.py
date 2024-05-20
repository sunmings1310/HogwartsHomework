#!/usr/bin/env python
# -*- coding: utf-8 -*-
from genson import SchemaBuilder

build = SchemaBuilder()
build.add_object({"a": 1, "b": "aaaa", "c": "", "d": None})
build.add_object({"a": "1", "b": "bbb", "c": 1})
print(build.to_json(indent=2))