import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recepts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recept",
            name="category",
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="recept",
            name="time",
            field=models.TimeField(default=0.0),
        ),
    ]