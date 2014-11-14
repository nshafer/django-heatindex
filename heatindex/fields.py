from __future__ import unicode_literals, print_function, division
from datetime import datetime, time
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils import timezone
import math

DEFAULT_DECAY_TIME = 86400
DEFAULT_SCORE_BASE = 10


class HeatIndexField(models.FloatField):
    def __init__(self, score_field, timestamp_field=None, decay_time=DEFAULT_DECAY_TIME, score_base=DEFAULT_SCORE_BASE,
                 *args, **kwargs):
        self.score_field = score_field
        self.timestamp_field = timestamp_field
        self.decay_time = decay_time
        self.score_base = score_base
        kwargs['default'] = 1
        if 'db_index' not in kwargs:
            kwargs['db_index'] = True
        super(HeatIndexField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(HeatIndexField, self).deconstruct()
        kwargs['score_field'] = self.score_field
        kwargs['timestamp_field'] = self.timestamp_field
        if self.decay_time != DEFAULT_DECAY_TIME:
            kwargs['decay_time'] = self.decay_time
        if self.score_base != DEFAULT_SCORE_BASE:
            kwargs['score_base'] = self.score_base
        return name, path, args, kwargs

    @staticmethod
    def get_field_or_callable(field, model_instance, add):
        if callable(field):
            return field(model_instance, add)
        try:
            return getattr(model_instance, field)
        except AttributeError:
            raise ImproperlyConfigured("Invalid field {}".format(field))

    def get_score(self, model_instance, add):
        if isinstance(self.score_field, (list, tuple)) and len(self.score_field) == 2:
            positive = self.get_field_or_callable(self.score_field[0], model_instance, add)
            negative = self.get_field_or_callable(self.score_field[1], model_instance, add)
            return positive - negative
        else:
            return self.get_field_or_callable(self.score_field, model_instance, add)

    def get_timestamp(self, model_instance, add):
        return self.get_field_or_callable(self.timestamp_field, model_instance, add)

    def calculate_heat(self, score, seconds):
        """ The secret sauce """
        return seconds + math.copysign(1, score) * math.log(max(abs(score), 1), self.score_base) * self.decay_time

    def pre_save(self, model_instance, add):
        timestamp = self.get_timestamp(model_instance, add)
        score = self.get_score(model_instance, add)
        try:
            seconds = timestamp.timestamp()
        except AttributeError:
            # Must not be python>=3.3
            try:
                seconds = (timestamp - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()
            except AttributeError:
                # Must not be python>=2.7
                seconds = time.mktime(timestamp.timetuple())
        value = self.calculate_heat(score, seconds)
        setattr(model_instance, self.attname, value)
        return super(HeatIndexField, self).pre_save(model_instance, add)

