from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.contrib.auth.models import User, Permission
from django.urls import reverse

from .models import Facultad, Carrera, Materia, Malla


# ==========================================================
# TESTS AUTOMÁTICOS - MATERIAS
# ==========================================================

class MateriaTests(TestCase):

    def test_mat_001_crear_materia_valida(self):
        """
        Verifica que se pueda crear una materia con datos válidos.
        """
        materia = Materia.objects.create(
            codigo="QA101",
            nombre="Fundamentos de Testing"
        )

        self.assertEqual(materia.codigo, "QA101")
        self.assertEqual(materia.nombre, "Fundamentos de Testing")

        self.assertTrue(
            Materia.objects.filter(codigo="QA101").exists()
        )


    def test_mat_002_codigo_duplicado_no_permitido(self):
        """
        Verifica que no se puedan registrar dos materias
        utilizando el mismo código.
        """

        Materia.objects.create(
            codigo="QA101",
            nombre="Fundamentos de Testing"
        )

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Materia.objects.create(
                    codigo="QA101",
                    nombre="Testing de Software II"
                )


    def test_mat_005_codigo_superior_a_20_caracteres(self):
        """
        Verifica que la validación del modelo rechace
        códigos superiores a 20 caracteres.
        """

        materia = Materia(
            codigo="A" * 21,
            nombre="Prueba de límite"
        )

        with self.assertRaises(ValidationError):
            materia.full_clean()


# ==========================================================
# TEST AUTOMÁTICO - INTEGRIDAD REFERENCIAL
# ==========================================================

class IntegridadReferencialTests(TestCase):

    def test_fac_001_eliminacion_en_cascada(self):
        """
        Verifica que al eliminar una Facultad:
        - desaparezca su Carrera
        - desaparezca su Malla
        - la Materia continúe existiendo
        """

        facultad = Facultad.objects.create(
            nombre="Facultad Test QA"
        )

        carrera = Carrera.objects.create(
            nombre="Carrera Test QA",
            facultad=facultad
        )

        materia = Materia.objects.create(
            codigo="QA999",
            nombre="Materia Superviviente"
        )

        malla = Malla.objects.create(
            carrera=carrera,
            anio=2026
        )

        malla.materias.add(materia)

        # Guardamos los IDs para consultarlos después de eliminar.
        facultad_id = facultad.id
        carrera_id = carrera.id
        malla_id = malla.id
        materia_id = materia.id

        facultad.delete()

        # Facultad eliminada
        self.assertFalse(
            Facultad.objects.filter(id=facultad_id).exists()
        )

        # Carrera eliminada por CASCADE
        self.assertFalse(
            Carrera.objects.filter(id=carrera_id).exists()
        )

        # Malla eliminada por CASCADE
        self.assertFalse(
            Malla.objects.filter(id=malla_id).exists()
        )

        # La Materia DEBE seguir existiendo
        self.assertTrue(
            Materia.objects.filter(id=materia_id).exists()
        )


# ==========================================================
# TEST AUTOMÁTICO - PERMISOS
# ==========================================================

class PermisosMateriaTests(TestCase):

    def setUp(self):
        """
        Prepara el usuario y la materia antes de ejecutar
        la prueba de permisos.
        """

        self.usuario = User.objects.create_user(
            username="qa_tester",
            password="qa_test_123"
        )

        self.usuario.is_staff = True
        self.usuario.save()

        permisos = Permission.objects.filter(
            content_type__app_label="academico",
            codename__in=[
                "view_materia",
                "add_materia",
                "change_materia",
            ]
        )

        self.usuario.user_permissions.set(permisos)

        self.materia = Materia.objects.create(
            codigo="QA200",
            nombre="Prueba de Permisos"
        )

        self.client.login(
            username="qa_tester",
            password="qa_test_123"
        )


    def test_usr_001_usuario_sin_permiso_no_puede_eliminar(self):
        """
        Verifica que un usuario staff sin permiso delete_materia
        no pueda acceder a la eliminación de una materia.
        """

        url_eliminar = reverse(
            "admin:academico_materia_delete",
            args=[self.materia.id]
        )

        response = self.client.get(url_eliminar)

        self.assertEqual(response.status_code, 403)

        self.assertTrue(
            Materia.objects.filter(id=self.materia.id).exists()
        )