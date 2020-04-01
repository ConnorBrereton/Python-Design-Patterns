#!/usr/bin/env python
#
# This is an example of chain of responsibility.

class ContentFilter(object):
    def __init__(self, filter):
        self._filters = filter
        if _filters is not None:
            self._filters += filter

    def filter(self, content):
        for filter in self._filters:
            content = filter(content)
        return content

filter = ContentFilter([
                pi_filter,
                ads_filter,
                graphic_filter])

filtered_content = filter.filter(content)