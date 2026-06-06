# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.utils import timezone, formats

from core.models import Child, Timer
from core.templatetags import bootstrap, datetime, duration, timers


class MockUserRequest:
    def __init__(self, user):
        self.user = user


class TemplateTagsTestCase(TestCase):
    # Verifica la renderización de iconos booleanos de Bootstrap.
    # Valida que retorne el HTML correcto (clases de CSS) para valores True y False.
    def test_bootstrap_bool_icon(self):
        self.assertEqual(
            bootstrap.bool_icon(True),
            '<i class="icon-true text-success" aria-hidden="true"></i>',
        )
        self.assertEqual(
            bootstrap.bool_icon(False),
            '<i class="icon-false text-danger" aria-hidden="true"></i>',
        )

    # def test_child_age_string(self):
    #     self.assertEqual(
    #         "6\xa0hours",
    #         duration.child_age_string(
    #             timezone.localtime() - timezone.timedelta(days=0, hours=6)
    #         ),
    #     )
    #     self.assertEqual(
    #         "1\xa0day",
    #         duration.child_age_string(
    #             timezone.localdate() - timezone.timedelta(days=1, hours=6)
    #         ),
    #     )
    #     self.assertEqual(
    #         "1\xa0month",
    #         duration.child_age_string(
    #             timezone.localdate() - timezone.timedelta(days=45)
    #         ),
    #     )
    #     self.assertEqual(
    #         "3\xa0months",
    #         duration.child_age_string(
    #             timezone.localdate() - timezone.timedelta(days=95)
    #         ),
    #     )
    #     self.assertEqual("", duration.child_age_string(None))
    #     self.assertEqual("", duration.child_age_string("not a date!!"))

    # Verifica la conversión de un objeto timedelta a una cadena de duración legible.
    # Valida formatos completos, formatos recortados ('m', 'h') y el manejo de excepciones TypeError.
    def test_duration_duration_string(self):
        delta = timezone.timedelta(hours=1, minutes=30, seconds=15)
        self.assertEqual(
            duration.duration_string(delta), "1 hour, 30 minutes, 15 seconds"
        )
        self.assertEqual(duration.duration_string(delta, "m"), "1 hour, 30 minutes")
        self.assertEqual(duration.duration_string(delta, "h"), "1 hour")

        self.assertEqual(duration.duration_string(""), "")
        self.assertRaises(TypeError, duration.duration_string("not a delta"))

    # Verifica la extracción precisa de la cantidad de horas a partir de un timedelta.
    # Valida el retorno en enteros y el manejo de errores de tipo.
    def test_duration_hours(self):
        delta = timezone.timedelta(hours=1)
        self.assertEqual(duration.hours(delta), 1)
        self.assertEqual(duration.hours(""), 0)
        self.assertRaises(TypeError, duration.hours("not a delta"))

    # Verifica la extracción de la cantidad de minutos desde un objeto timedelta.
    # Valida que devuelva los minutos exactos y que lance una excepción ante datos inválidos.
    def test_duration_minutes(self):
        delta = timezone.timedelta(minutes=45)
        self.assertEqual(duration.minutes(delta), 45)
        self.assertEqual(duration.minutes(""), 0)
        self.assertRaises(TypeError, duration.minutes("not a delta"))

    # Verifica la extracción de segundos desde un objeto timedelta.
    # Valida el cálculo numérico y la validación de excepciones al enviar cadenas de texto.
    def test_duration_seconds(self):
        delta = timezone.timedelta(seconds=20)
        self.assertEqual(duration.seconds(delta), 20)
        self.assertEqual(duration.seconds(""), 0)
        self.assertRaises(TypeError, duration.seconds("not a delta"))

    # Verifica el cálculo descriptivo de los días transcurridos respecto a una fecha límite.
    # Valida múltiples escenarios devolviendo textos como "today", "yesterday" o "X days ago".
    def test_duration_dayssince(self):
        # test with a few different dates that could be pathological
        dates = [
            timezone.datetime(2022, 1, 1, 0, 0, 1).date(),  # new year
            timezone.datetime(2021, 12, 31, 23, 59, 59).date(),  # almost new year
            timezone.datetime(
                1969, 2, 1, 23, 59, 59
            ).date(),  # old but middle of the year
        ]
        for d in dates:
            self.assertEqual(duration.dayssince(d, today=d), "today")
            self.assertEqual(
                duration.dayssince((d - timezone.timedelta(hours=5)), today=d), "today"
            )
            self.assertEqual(
                duration.dayssince((d - timezone.timedelta(hours=24)), today=d),
                "yesterday",
            )
            self.assertEqual(
                duration.dayssince((d - timezone.timedelta(hours=24 * 2)), today=d),
                "2 days ago",
            )
            self.assertEqual(
                duration.dayssince((d - timezone.timedelta(hours=24 * 10)), today=d),
                "10 days ago",
            )
            self.assertEqual(
                duration.dayssince((d - timezone.timedelta(hours=24 * 60)), today=d),
                "60 days ago",
            )

    # Verifica el cálculo exacto del tiempo transcurrido entre dos objetos datetime.
    # Valida que la diferencia generada corresponda al timedelta esperado en varios escenarios.
    def test_duration_deltasince(self):
        datetimes = [
            (
                timezone.datetime(2022, 1, 1, 0, 0, 1),
                timezone.timedelta(seconds=1),
            ),  # new year
            (
                timezone.datetime(2021, 12, 31, 23, 59, 59),
                timezone.timedelta(seconds=3),
            ),  # almost new year
            (
                timezone.datetime(1969, 2, 1, 23, 59, 59),
                timezone.timedelta(days=19326, seconds=3),
            ),  # old but middle of the year
        ]
        now = timezone.datetime(2022, 1, 1, 0, 0, 2)
        for d, expected_delta in datetimes:
            with self.subTest():
                self.assertEqual(duration.deltasince(d, now), expected_delta)

    # [PRUEBA DE INTEGRACIÓN]
    # No es unitaria porque inserta objetos Child y Timer en la Base de Datos.
    def test_instance_add_url(self):
        child = Child.objects.create(
            first_name="Test", last_name="Child", birth_date=timezone.localdate()
        )
        user = get_user_model().objects.create_user(username="timer")
        timer = Timer.objects.create(user=user)

        url = timers.instance_add_url({"timer": timer}, "core:sleep-add")
        self.assertEqual(url, "/sleep/add/?timer={}".format(timer.id))

        timer = Timer.objects.create(user=user, child=child)
        url = timers.instance_add_url({"timer": timer}, "core:sleep-add")
        self.assertEqual(
            url, "/sleep/add/?timer={}&child={}".format(timer.id, child.slug)
        )

    # Verifica el formateo de fechas hacia representaciones de texto más cortas.
    # Valida el uso de "Today" para la fecha actual y formatos de "mes corto" para previas.
    def test_datetime_short(self):
        date = timezone.localtime()
        self.assertEqual(
            datetime.datetime_short(date),
            "Today, {}".format(formats.date_format(date, format="TIME_FORMAT")),
        )

        date = timezone.localtime() - timezone.timedelta(days=1, hours=6)
        self.assertEqual(
            datetime.datetime_short(date),
            "{}, {}".format(
                formats.date_format(date, format="SHORT_MONTH_DAY_FORMAT"),
                formats.date_format(date, format="TIME_FORMAT"),
            ),
        )
