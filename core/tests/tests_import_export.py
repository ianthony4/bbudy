# -*- coding: utf-8 -*-
import datetime
import importlib
import os
import tablib

from django.core.management import call_command
from django.test import TestCase

from core import admin, models


class ImportTestCase(TestCase):
    base_path = os.path.dirname(__file__) + "/import/"
    admin_module = importlib.import_module("core.admin")
    model_module = importlib.import_module("core.models")

    def setUp(self):
        call_command("migrate", verbosity=0)
        # The data to be imported uses 2020-02-10 as a basis and Child ID 1.
        birth_date = datetime.date(year=2020, month=2, day=10)
        models.Child.objects.create(
            first_name="Child", last_name="One", birth_date=birth_date
        ).save()

    def get_dataset(self, model_name):
        with open(self.base_path + model_name + ".csv", "r") as f:
            data = f.read()
        return tablib.Dataset().load(data)

    def import_data(self, model, count):
        dataset = self.get_dataset(model._meta.model_name)
        resource_class = getattr(
            self.admin_module, model.__name__ + "ImportExportResource"
        )
        resource = resource_class()
        result = resource.import_data(dataset, dry_run=False)
        self.assertFalse(result.has_validation_errors())
        self.assertFalse(result.has_errors())
        self.assertEqual(model.objects.count(), count)

    # Verifica la importación de datos del índice de masa corporal (BMI) desde un CSV.
    # Valida que se creen exactamente 5 registros en la base de datos sin errores.
    def test_bmi(self):
        self.import_data(models.BMI, 5)

    # Verifica la importación de perfiles de infantes (Child) desde un archivo CSV.
    # Valida que existan 2 registros finales exitosos en el sistema.
    def test_child(self):
        self.import_data(models.Child, 2)

    # Verifica el manejo de errores al intentar importar datos inconsistentes (infante inexistente).
    # Valida que el proceso sea bloqueado y retorne errores de validación.
    def test_child_invalid(self):
        dataset = self.get_dataset("diaperchange-invalid-child")
        resource = admin.DiaperChangeImportExportResource()
        result = resource.import_data(dataset, dry_run=False)
        self.assertTrue(result.has_validation_errors())

    # Verifica la importación masiva de registros de cambios de pañal.
    # Valida la inserción exitosa de 75 registros en la base de datos.
    def test_diaperchange(self):
        self.import_data(models.DiaperChange, 75)

    # Verifica la importación de registros de alimentación del infante.
    # Valida la creación de 40 registros continuos sin presentar errores.
    def test_feeding(self):
        self.import_data(models.Feeding, 40)

    # Verifica la importación de las mediciones de la circunferencia craneal.
    # Valida que se inserten 5 registros correspondientes correctamente.
    def test_headercircumference(self):
        self.import_data(models.HeadCircumference, 5)

    # Verifica la importación de los datos históricos de altura.
    # Valida la inserción de 5 registros correctos en la base de datos.
    def test_height(self):
        self.import_data(models.Height, 5)

    # Verifica la importación de notas o comentarios personalizados.
    # Valida que se procese e inserte 1 registro en el sistema.
    def test_note(self):
        self.import_data(models.Note, 1)

    # Verifica la importación de los registros de extracción de leche (Pumping).
    # Valida la creación masiva de 23 registros exitosos.
    def test_pumping(self):
        self.import_data(models.Pumping, 23)

    # Verifica la carga de datos sobre los periodos de sueño del infante.
    # Valida que se inserten 39 registros de descanso sin errores de validación.
    def test_sleep(self):
        self.import_data(models.Sleep, 39)

    # Verifica la importación individual de etiquetas (Tags) para agrupar datos.
    # Valida la creación exitosa de 10 etiquetas base.
    def test_tag(self):
        self.import_data(models.Tag, 10)

    # Verifica que las etiquetas importadas se asocien correctamente a los registros.
    # Valida comparando los tags de múltiples entradas de Temperatura contra listas esperadas.
    def test_tagged(self):
        self.import_data(models.Tag, 10)
        self.import_data(models.Temperature, 23)
        tests = [
            (65, ["ten", "method"]),
            (70, ["our", "you", "everybody", "ten", "military"]),
            (71, ["you", "treatment", "method"]),
            (75, ["everybody"]),
            (78, ["our", "treatment", "surface"]),
        ]
        for pk, tags in tests:
            entry = models.Temperature.objects.get(pk=pk)
            self.assertQuerySetEqual(entry.tags.names(), tags, ordered=False)

    # Verifica la importación de las tomas de temperatura del infante.
    # Valida la inserción de 23 registros continuos en la base de datos.
    def test_temperature(self):
        self.import_data(models.Temperature, 23)

    # Verifica la carga de las sesiones de tiempo boca abajo (Tummy Time).
    # Valida la creación exitosa de 36 registros en el sistema.
    def test_tummytime(self):
        self.import_data(models.TummyTime, 36)

    # Verifica la importación de los datos de seguimiento de peso.
    # Valida que se procesen e inserten 5 registros sin fallos.
    def test_weight(self):
        self.import_data(models.Weight, 5)