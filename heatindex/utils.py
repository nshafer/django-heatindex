from __future__ import unicode_literals, print_function, division

import math


def calculate_heat(score, seconds, score_base, decay_time):
    """
    calculate_heat: The special sauce

    This function will return the `seconds` + an adjustment such that things with more "heat" will have a higher
    heat index than things that are either scored lower or are older. The algorithm is such that an object that has
    a score equal to `score_base` will be devoid of "heat", plus or minus, at exactly `decay_time`, and just return
    `seconds` with no adjustment. Anything with a higher score will still retain heat beyond `decay_time` and
    anything with a lower score will lose all heat before `decay_time` has passed. Negative scores will cause the
    adjustment to be negative immediately and will always return something less than `seconds`.
    """

    # Store the sign for later use
    sign = math.copysign(1, score)

    # Calculate the inverse exponential power of the score so that scores above `score_base` will lose
    # effectiveness and prevent this object from never losing heat, and becoming perpetual. Due to the use of
    # logarithm, scores of 1, 0 and -1 are effectively the same.
    score_power = sign * math.log(max(abs(score), 1), score_base)

    # Multiply by the `decay_time` so that this object will lose "heat" as it gets older and closer to the
    # target `decay_time`
    heat_adjustment = score_power * decay_time

    # Add the adjustment to the timestamp of this object so we can sort or filter by it
    return seconds + heat_adjustment


def update_heat_column_migration_factory(app_label, model_name, *fields):
    """
    function factory that returns a function compatible with django.db.migrations.RunPython to recalculate heat columns
    """
    def migration_function(apps, schema_editor):
        model = apps.get_model(app_label, model_name)
        # TODO: do this in batches?  Perhaps custom UPDATE SQL queries?
        for object in model._default_manager.all():
            object.save(update_fields=fields)
    return migration_function


