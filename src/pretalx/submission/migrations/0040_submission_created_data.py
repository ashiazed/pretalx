# Generated by Django 2.2.1 on 2019-05-01 20:36

from django.db import migrations
from django_scopes import scopes_disabled


def fill_created(apps, schema_editor):
    with scopes_disabled():
        Submission = apps.get_model('submission', 'Submission')
        for submission_id in Submission.objects.all().values_list('pk', flat=True):
            submission = Submission.objects.get(pk=submission_id)
            submission.created = getattr(
                submission.logged_actions().order_by('timestamp').first(), 'timestamp', None
            )
            if submission.created:
                submission.save(update_fields=['created'])


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0039_submission_created'),
    ]

    operations = [
        migrations.RunPython(fill_created, migrations.RunPython.noop),
    ]
