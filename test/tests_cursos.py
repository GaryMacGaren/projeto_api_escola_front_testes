from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Cursos-list') #nome baseado no basename de urls.py
        self.curso_1 = Curso.objects.create(
            codigo_curso='CT1', descricao='Curso Teste 1', nivel='B',
        )
        self.curso_2 = Curso.objects.create(
        codigo_curso = 'CT2', descricao = 'Curso Teste 2', nivel = 'A',
        )

    # def test_falha(self):
    #     self.fail('Teste falhou, não se preocupar!')

    def test_requisicao_get_listar_cursos(self):
        """Teste para verificar a requisicao get para listar cursos"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_requisicao_post_criar_curso(self):
        """Teste para fazer post em cursos"""

        data = {
            "codigo_curso": "CT1",
            "descricao": "Curso Teste 1",
            "nivel": "B",
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_requisicao_deletar_curso(self):
        """Teste para testar deletar um curso"""
        response = self.client.delete('/cursos/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_requisicao_put_atualizar_curso(self):
        """Teste para verificar requisicao put cursos"""
        data = {
            "codigo_curso": "CT3",
            "descricao": "Curso Teste 3",
            "nivel": "A",
        }
        response = self.client.put('/cursos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)