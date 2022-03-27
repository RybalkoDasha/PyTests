import unittest
from secretary_documents import get_doc_shelf, get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf, add_new_doc, \
    documents, directories, delete_doc


class TestDocFunctions(unittest.TestCase):
    def test_add_doc_normal_flow(self):
        # По скольку функция добавления возврращает номер полки, то сравнение ведется с ним
        self.assertEqual(add_new_doc(), '3')

    def test_get_shelf(self):
        # Проверка наличия документа на полке
        self.assertEqual(get_doc_shelf(), '1')

    def test_get_owner(self):
        # Проверка вывода имени владельца документа
        self.assertEqual(get_doc_owner_name(), 'Геннадий Покемонов')

    def test_get_all(self):
        # Проверка всех имен владельцев документов
        self.assertEqual(get_all_doc_owners_names(), {'Аристарх Павлов', 'Геннадий Покемонов', 'Oleg', 'Василий Гупкин'})


    def test_remove_doc(self):
        # Проверка удаления документа по его номеру, функция в прриложении возвращает номер удаленного элемента
        self.assertEqual(delete_doc(), '11-2')