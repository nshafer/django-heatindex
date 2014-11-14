from __future__ import unicode_literals, print_function, division


def update_heat_column_migration_factory(app_label, model_name, *fields):
    def migration_function(apps, schema_editor):
        model = apps.get_model(app_label, model_name)
        # TODO: do this in batches?  Perhaps custom UPDATE SQL queries?
        for object in model._default_manager.all():
            object.save(update_fields=fields)
    return migration_function


