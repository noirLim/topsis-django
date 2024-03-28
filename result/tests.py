from django.test import TestCase
from .utils import *
import re

# Create your tests here.

data_alternative = [
    {'id': 2, 'value': 5.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 3, 'criteria__name': 'Dependents'}, 
    {'id': 3, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 4, 'criteria__name': 'GPA'}, 
    {'id': 4, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 5, 'criteria__name': 'Semester'},
    {'id': 5, 'value': 2.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 6, 'criteria__name': "Parents' income"},
    
    {'id': 6, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 3, 'criteria__name': 'Dependents'}, 
    {'id': 7, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 4, 'criteria__name': 'GPA'}, 
    {'id': 8, 'value': 3.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 5, 'criteria__name': 'Semester'}, 
    {'id': 9, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 6, 'criteria__name': "Parents' income"},
   
    {'id': 10, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 3, 'criteria__name': 'Dependents'},  
    {'id': 11, 'value': 2.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 4, 'criteria__name': 'GPA'},
    {'id': 12, 'value': 3.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 5, 'criteria__name': 'Semester'}, 
    {'id': 13, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 6, 'criteria__name': "Parents' income"},

    {'id': 14, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 3, 'criteria__name': 'Dependents'}, 
    {'id': 15, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 4, 'criteria__name': 'GPA'},
    {'id': 16, 'value': 1.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 5, 'criteria__name': 'Semester'},
    {'id': 17, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 6, 'criteria__name': "Parents' income"}, 
    
    {'id': 18, 'value': 4.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 3, 'criteria__name': 'Dependents'}, 
    {'id': 19, 'value': 5.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 4, 'criteria__name': 'GPA'}, 
    {'id': 20, 'value': 3.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 5, 'criteria__name': 'Semester'}, 
    {'id': 21, 'value': 2.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 6, 'criteria__name': "Parents' income"}
    ]

criteria_data = [
    {'id': 3, 'code': '0001', 'name': 'Dependents', 'attribute': 'benefit', 'weight': 3.0},
    {'id': 4, 'code': '0002', 'name': 'GPA', 'attribute': 'benefit', 'weight': 2.0}, 
    {'id': 5, 'code': '0003', 'name': 'Semester', 'attribute': 'benefit', 'weight': 2.0}, 
    {'id': 6, 'code': '0004', 'name': "Parents' income", 'attribute': 'cost', 'weight': 3.0}
]

students_data = [
    {'id': 4, 'name': 'Maria'}, 
    {'id': 5, 'name': 'Ana'}, 
    {'id': 6, 'name': 'Antonio'}, 
    {'id': 7, 'name': 'Thomas'}, 
    {'id': 8, 'name': 'Christina'}
]

def remove_whitespace(text):
    # Remove all whitespace characters (\s) using regular expression
    return re.sub(r'\s+', '', text)

class ResultTestCase(TestCase):
    # create array of alternative and map according id
    def test_get_students_by_id(self):
        expected = [
            {'id': 4, 'name': 'Maria',"alt":[
              {'id': 2, 'value': 5.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 3, 'criteria__name': 'Dependents'}, 
              {'id': 3, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 4, 'criteria__name': 'GPA'}, 
              {'id': 4, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 5, 'criteria__name': 'Semester'},
              {'id': 5, 'value': 2.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 6, 'criteria__name': "Parents' income"},
            ]}, 
            {'id': 5, 'name': 'Ana',"alt":[
             {'id': 6, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 3, 'criteria__name': 'Dependents'}, 
             {'id': 7, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 4, 'criteria__name': 'GPA'}, 
             {'id': 8, 'value': 3.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 5, 'criteria__name': 'Semester'}, 
             {'id': 9, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 6, 'criteria__name': "Parents' income"},
            ]}, 
            {'id': 6, 'name': 'Antonio',"alt":[
             {'id': 10, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 3, 'criteria__name': 'Dependents'},  
             {'id': 11, 'value': 2.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 4, 'criteria__name': 'GPA'},
             {'id': 12, 'value': 3.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 5, 'criteria__name': 'Semester'}, 
             {'id': 13, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 6, 'criteria__name': "Parents' income"},
            ]}, 
            {'id': 7, 'name': 'Thomas',"alt":[
             {'id': 14, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 3, 'criteria__name': 'Dependents'}, 
             {'id': 15, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 4, 'criteria__name': 'GPA'},
             {'id': 16, 'value': 1.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 5, 'criteria__name': 'Semester'},
             {'id': 17, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 6, 'criteria__name': "Parents' income"}, 
            ]}, 
            {'id': 8, 'name': 'Christina',"alt":[
             {'id': 18, 'value': 4.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 3, 'criteria__name': 'Dependents'}, 
             {'id': 19, 'value': 5.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 4, 'criteria__name': 'GPA'}, 
            {'id': 20, 'value': 3.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 5, 'criteria__name': 'Semester'}, 
            {'id': 21, 'value': 2.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 6, 'criteria__name': "Parents' income"}
            ]}
        ]

        actual = map_by_id(students_data,data_alternative)
        self.assertEqual(actual,expected)

    def test_normalize(self):
        matriks = [
            {'id': 4, 'name': 'Maria',"alt":[
              {'id': 2, 'value': 5.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 3, 'criteria__name': 'Dependents'}, 
              {'id': 3, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 4, 'criteria__name': 'GPA'}, 
              {'id': 4, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 5, 'criteria__name': 'Semester'},
              {'id': 5, 'value': 2.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 6, 'criteria__name': "Parents' income"},
            ]}, 
            {'id': 5, 'name': 'Ana',"alt":[
             {'id': 6, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 3, 'criteria__name': 'Dependents'}, 
             {'id': 7, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 4, 'criteria__name': 'GPA'}, 
             {'id': 8, 'value': 3.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 5, 'criteria__name': 'Semester'}, 
             {'id': 9, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 6, 'criteria__name': "Parents' income"},
            ]}, 
            {'id': 6, 'name': 'Antonio',"alt":[
             {'id': 10, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 3, 'criteria__name': 'Dependents'},  
             {'id': 11, 'value': 2.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 4, 'criteria__name': 'GPA'},
             {'id': 12, 'value': 3.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 5, 'criteria__name': 'Semester'}, 
             {'id': 13, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 6, 'criteria__name': "Parents' income"},
            ]}, 
            {'id': 7, 'name': 'Thomas',"alt":[
             {'id': 14, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 3, 'criteria__name': 'Dependents'}, 
             {'id': 15, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 4, 'criteria__name': 'GPA'},
             {'id': 16, 'value': 1.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 5, 'criteria__name': 'Semester'},
             {'id': 17, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 6, 'criteria__name': "Parents' income"}, 
            ]}, 
            {'id': 8, 'name': 'Christina',"alt":[
             {'id': 18, 'value': 4.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 3, 'criteria__name': 'Dependents'}, 
             {'id': 19, 'value': 5.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 4, 'criteria__name': 'GPA'}, 
            {'id': 20, 'value': 3.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 5, 'criteria__name': 'Semester'}, 
            {'id': 21, 'value': 2.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 6, 'criteria__name': "Parents' income"}
            ]}
        ]

        expected =[
            {'id': 4, 'name': 'Maria', 'alt': [
                {'id': 2, 'value': 5.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.5735393346764044}, 
                {'id': 3, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.3535533905932738}, 
                {'id': 4, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719}, 
                {'id': 5, 'value': 2.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.30499714066520933}
                ]}, 
            {'id': 5, 'name': 'Ana', 'alt': [
                {'id': 6, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.5735393346764044}, 
                {'id': 7, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.5892556509887896},
                {'id': 8, 'value': 3.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719}, 
                {'id': 9, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.7624928516630234}
                ]}, 
            {'id': 6, 'name': 'Antonio', 'alt': [{'id': 10, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.11470786693528087}, 
            {'id': 11, 'value': 2.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.23570226039551587}, 
            {'id': 12, 'value': 3.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719}, 
            {'id': 13, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.15249857033260467}
            ]}, 
            {'id': 7, 'name': 'Thomas', 'alt': [
                {'id': 14, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.3441236008058426}, 
                {'id': 15, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.3535533905932738}, 
                {'id': 16, 'value': 1.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.1643989873053573},
                {'id': 17, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.457495710997814}
            ]}, 
                {'id': 8, 'name': 'Christina', 'alt': [
               {'id': 18, 'value': 4.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.4588314677411235}, 
               {'id': 19, 'value': 5.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.5892556509887896}, 
               {'id': 20, 'value': 3.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719}, 
               {'id': 21, 'value': 2.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.30499714066520933}]}]
        actual = normalize(criteria_data,data_alternative,matriks)
        self.assertEqual(actual,expected)

    def test_weighted_normalization(self):
        data = [
            {'id': 4, 'name': 'Maria', 'alt': [
                {'id': 2, 'value': 5.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.5735393346764044}, 
                {'id': 3, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.3535533905932738}, 
                {'id': 4, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719}, 
                {'id': 5, 'value': 2.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.30499714066520933}
                ]}, 
            {'id': 5, 'name': 'Ana', 'alt': [
                {'id': 6, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.5735393346764044}, 
                {'id': 7, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.5892556509887896},
                {'id': 8, 'value': 3.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719}, 
                {'id': 9, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.7624928516630234}
                ]}, 
            {'id': 6, 'name': 'Antonio', 'alt': [{'id': 10, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.11470786693528087}, 
            {'id': 11, 'value': 2.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.23570226039551587}, 
            {'id': 12, 'value': 3.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719}, 
            {'id': 13, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.15249857033260467}
            ]}, 
            {'id': 7, 'name': 'Thomas', 'alt': [
                {'id': 14, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.3441236008058426}, 
                {'id': 15, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.3535533905932738}, 
                {'id': 16, 'value': 1.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.1643989873053573},
                {'id': 17, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.457495710997814}
            ]}, 
                {'id': 8, 'name': 'Christina', 'alt': [
               {'id': 18, 'value': 4.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.4588314677411235}, 
               {'id': 19, 'value': 5.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.5892556509887896}, 
               {'id': 20, 'value': 3.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719}, 
               {'id': 21, 'value': 2.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.30499714066520933}]}]
        
        expected = [
            {'id': 4, 'name': 'Maria', 'alt': [
                {'id': 2, 'value': 5.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.5735393346764044, 'new_weight': 0.17206180040292132}, 
                {'id': 3, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.3535533905932738, 'new_weight': 0.07071067811865477}, 
                {'id': 4, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719, 'new_weight': 0.09863939238321438}, 
                {'id': 5, 'value': 2.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.30499714066520933, 'new_weight': 0.0914991421995628}]}, 
            {'id': 5, 'name': 'Ana', 'alt': [
                {'id': 6, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.5735393346764044, 'new_weight': 0.17206180040292132}, 
                {'id': 7, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.5892556509887896, 'new_weight': 0.11785113019775793},
                {'id': 8, 'value': 3.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719, 'new_weight': 0.09863939238321438}, 
                {'id': 9, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.7624928516630234, 'new_weight': 0.228747855498907}]}, 
            {'id': 6, 'name': 'Antonio', 'alt': [
                {'id': 10, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.11470786693528087, 'new_weight': 0.03441236008058426}, 
                {'id': 11, 'value': 2.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.23570226039551587, 'new_weight': 0.047140452079103175},
                {'id': 12, 'value': 3.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719, 'new_weight': 0.09863939238321438}, 
                {'id': 13, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.15249857033260467, 'new_weight': 0.0457495710997814}]}, 
            {'id': 7, 'name': 'Thomas', 'alt': [
                {'id': 14, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.3441236008058426, 'new_weight': 0.10323708024175278}, 
                {'id': 15, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.3535533905932738, 'new_weight': 0.07071067811865477}, 
                {'id': 16, 'value': 1.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.1643989873053573, 'new_weight': 0.03287979746107146}, 
                
                {'id': 17, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.457495710997814, 'new_weight': 0.13724871329934418}]}, 
            {'id': 8, 'name': 'Christina', 'alt': [{'id': 18, 'value': 4.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.4588314677411235, 'new_weight': 0.13764944032233703}, 
                {'id': 19, 'value': 5.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.5892556509887896, 'new_weight': 0.11785113019775793}, 
                {'id': 20, 'value': 3.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719, 'new_weight': 0.09863939238321438}, 
                {'id': 21, 'value': 2.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.30499714066520933, 'new_weight': 0.0914991421995628}]}]
        actual = calc_weighted(data,criteria_data)
        self.assertEqual(actual,expected)

    def test_ideal_solution(self):
        data = [
            {'id': 4, 'name': 'Maria', 'alt': [
                {'id': 2, 'value': 5.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.5735393346764044, 'new_weight': 0.17206180040292132}, 
                {'id': 3, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.3535533905932738, 'new_weight': 0.07071067811865477}, 
                {'id': 4, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719, 'new_weight': 0.09863939238321438}, 
                {'id': 5, 'value': 2.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.30499714066520933, 'new_weight': 0.0914991421995628}]}, 
            {'id': 5, 'name': 'Ana', 'alt': [
                {'id': 6, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.5735393346764044, 'new_weight': 0.17206180040292132}, 
                {'id': 7, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.5892556509887896, 'new_weight': 0.11785113019775793},
                {'id': 8, 'value': 3.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719, 'new_weight': 0.09863939238321438}, 
                {'id': 9, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.7624928516630234, 'new_weight': 0.228747855498907}]}, 
            {'id': 6, 'name': 'Antonio', 'alt': [
                {'id': 10, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.11470786693528087, 'new_weight': 0.03441236008058426}, 
                {'id': 11, 'value': 2.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.23570226039551587, 'new_weight': 0.047140452079103175},
                {'id': 12, 'value': 3.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719, 'new_weight': 0.09863939238321438}, 
                {'id': 13, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.15249857033260467, 'new_weight': 0.0457495710997814}]}, 
            {'id': 7, 'name': 'Thomas', 'alt': [
                {'id': 14, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.3441236008058426, 'new_weight': 0.10323708024175278}, 
                {'id': 15, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.3535533905932738, 'new_weight': 0.07071067811865477}, 
                {'id': 16, 'value': 1.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.1643989873053573, 'new_weight': 0.03287979746107146}, 
                
                {'id': 17, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.457495710997814, 'new_weight': 0.13724871329934418}]}, 
            {'id': 8, 'name': 'Christina', 'alt': [{'id': 18, 'value': 4.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.4588314677411235, 'new_weight': 0.13764944032233703}, 
                {'id': 19, 'value': 5.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.5892556509887896, 'new_weight': 0.11785113019775793}, 
                {'id': 20, 'value': 3.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719, 'new_weight': 0.09863939238321438}, 
                {'id': 21, 'value': 2.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.30499714066520933, 'new_weight': 0.0914991421995628}]}]
        
        actual = find_ideal_solution(criteria_data,data)
        expected = [
            {'id': 3, 'code': '0001', 'name': 'Dependents', 'attribute': 'benefit', 'weight': 3.0, 'positive': 0.17206180040292132, 'negative': 0.03441236008058426}, 
            {'id': 4, 'code': '0002', 'name': 'GPA', 'attribute': 'benefit', 'weight': 2.0, 'positive': 0.11785113019775793, 'negative': 0.047140452079103175},
            {'id': 5, 'code': '0003', 'name': 'Semester', 'attribute': 'benefit', 'weight': 2.0, 'positive': 0.09863939238321438, 'negative': 0.03287979746107146}, 
            {'id': 6, 'code': '0004', 'name': "Parents' income", 'attribute': 'cost', 'weight': 3.0, 'positive': 0.0457495710997814, 'negative': 0.228747855498907}]
        self.assertEqual(actual,expected)

    def test_ideal_solution_dis(self):
          data = [
            {'id': 4, 'name': 'Maria', 'alt': [
                {'id': 2, 'value': 5.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.5735393346764044, 'new_weight': 0.17206180040292132}, 
                {'id': 3, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.3535533905932738, 'new_weight': 0.07071067811865477}, 
                {'id': 4, 'value': 3.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719, 'new_weight': 0.09863939238321438}, 
                {'id': 5, 'value': 2.0, 'student__id': 4, 'student__name': 'Maria', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.30499714066520933, 'new_weight': 0.0914991421995628}]}, 
            {'id': 5, 'name': 'Ana', 'alt': [
                {'id': 6, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.5735393346764044, 'new_weight': 0.17206180040292132}, 
                {'id': 7, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.5892556509887896, 'new_weight': 0.11785113019775793},
                {'id': 8, 'value': 3.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719, 'new_weight': 0.09863939238321438}, 
                {'id': 9, 'value': 5.0, 'student__id': 5, 'student__name': 'Ana', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.7624928516630234, 'new_weight': 0.228747855498907}]}, 
            {'id': 6, 'name': 'Antonio', 'alt': [
                {'id': 10, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.11470786693528087, 'new_weight': 0.03441236008058426}, 
                {'id': 11, 'value': 2.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.23570226039551587, 'new_weight': 0.047140452079103175},
                {'id': 12, 'value': 3.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719, 'new_weight': 0.09863939238321438}, 
                {'id': 13, 'value': 1.0, 'student__id': 6, 'student__name': 'Antonio', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.15249857033260467, 'new_weight': 0.0457495710997814}]}, 
            {'id': 7, 'name': 'Thomas', 'alt': [
                {'id': 14, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.3441236008058426, 'new_weight': 0.10323708024175278}, 
                {'id': 15, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.3535533905932738, 'new_weight': 0.07071067811865477}, 
                {'id': 16, 'value': 1.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.1643989873053573, 'new_weight': 0.03287979746107146}, 
                
                {'id': 17, 'value': 3.0, 'student__id': 7, 'student__name': 'Thomas', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.457495710997814, 'new_weight': 0.13724871329934418}]}, 
            {'id': 8, 'name': 'Christina', 'alt': [{'id': 18, 'value': 4.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 3, 'criteria__name': 'Dependents', 'pow': 0.4588314677411235, 'new_weight': 0.13764944032233703}, 
                {'id': 19, 'value': 5.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 4, 'criteria__name': 'GPA', 'pow': 0.5892556509887896, 'new_weight': 0.11785113019775793}, 
                {'id': 20, 'value': 3.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 5, 'criteria__name': 'Semester', 'pow': 0.4931969619160719, 'new_weight': 0.09863939238321438}, 
                {'id': 21, 'value': 2.0, 'student__id': 8, 'student__name': 'Christina', 'criteria__id': 6, 'criteria__name': "Parents' income", 'pow': 0.30499714066520933, 'new_weight': 0.0914991421995628}]}]
          
          new_criteria = [
            {'id': 3, 'code': '0001', 'name': 'Dependents', 'attribute': 'benefit', 'weight': 3.0, 'positive': 0.17206180040292132, 'negative': 0.03441236008058426}, 
            {'id': 4, 'code': '0002', 'name': 'GPA', 'attribute': 'benefit', 'weight': 2.0, 'positive': 0.11785113019775793, 'negative': 0.047140452079103175},
            {'id': 5, 'code': '0003', 'name': 'Semester', 'attribute': 'benefit', 'weight': 2.0, 'positive': 0.09863939238321438, 'negative': 0.03287979746107146}, 
            {'id': 6, 'code': '0004', 'name': "Parents' income", 'attribute': 'cost', 'weight': 3.0, 'positive': 0.0457495710997814, 'negative': 0.228747855498907}]
          
          actual = find_ideal_dis(data,new_criteria)
          expected = [
              {'id': 4, 'name': 'Maria', 'positive': 0.06569052806939654, 'negative': 0.20655376443739312}, 
              {'id': 5, 'name': 'Ana', 'positive': 0.1829982843991256, 'negative': 0.168141882781706}, 
              {'id': 6, 'name': 'Antonio', 'positive': 0.15474937292620164, 'negative': 0.19445486987305713}, 
              {'id': 7, 'name': 'Thomas', 'positive': 0.14019800881276995, 'negative': 0.1168952124086976}, 
              {'id': 8, 'name': 'Christina', 'positive': 0.05724712902958318, 'negative': 0.19702646614983482}]
          self.assertEqual(actual,expected)

    def test_preference_val(self):
        data = [
              {'id': 4, 'name': 'Maria', 'positive': 0.06569052806939654, 'negative': 0.20655376443739312}, 
              {'id': 5, 'name': 'Ana', 'positive': 0.1829982843991256, 'negative': 0.168141882781706}, 
              {'id': 6, 'name': 'Antonio', 'positive': 0.15474937292620164, 'negative': 0.19445486987305713}, 
              {'id': 7, 'name': 'Thomas', 'positive': 0.14019800881276995, 'negative': 0.1168952124086976}, 
              {'id': 8, 'name': 'Christina', 'positive': 0.05724712902958318, 'negative': 0.19702646614983482}]
        expected = [
            {'student_id': 8, 'value': 0.774860110861338}, 
            {'student_id': 4, 'value': 0.7587074187505392}, 
            {'student_id': 6, 'value': 0.5568513953733379}, 
            {'student_id': 5, 'value': 0.4788454825081734}, 
            {'student_id': 7, 'value': 0.45468025898668357}]
        actual = calc_preference(data)
        self.assertEqual(actual,expected)

    def test_topsis_func(self):
        expected = [
            {'student_id': 8, 'value': 0.774860110861338}, 
            {'student_id': 4, 'value': 0.7587074187505392}, 
            {'student_id': 6, 'value': 0.5568513953733379}, 
            {'student_id': 5, 'value': 0.4788454825081734}, 
            {'student_id': 7, 'value': 0.45468025898668357}]
        
        actual = calc_topsis(data_alternative,criteria_data,students_data)
        self.assertEqual(actual,expected)

    def create_excel_report(self):
        data = {"custom_labels":{
            "rank":"Rank",
            'student':"Student",
            'value':"Value"
            },"data":[
                {'id': 1, 'value': 0.774860110861338, 'student__id': 8, 'student__name': 'Christina'}, 
                {'id': 2, 'value': 0.7587074187505392, 'student__id': 4, 'student__name': 'Maria'}, 
                {'id': 3, 'value': 0.5568513953733379, 'student__id': 6, 'student__name': 'Antonio'}, 
                {'id': 4, 'value': 0.4788454825081734, 'student__id': 5, 'student__name': 'Ana'}, 
                {'id': 5, 'value': 0.45468025898668357, 'student__id': 7, 'student__name': 'Thomas'}]
            }
        actual = create_html_excel(data)
        expected = """
        <table>
        <tr>
        <th>Rank</th>
        <th>Student</th>
        <th>Value</th>
        <tr/>
        <tr>
        <td>1</td>
        <td>Christina</td>
        <td>0.774860110861338</td>
        </tr>
        <tr>
        <td>2</td>
        <td>Maria</td>
        <td>0.7587074187505392</td>
        </tr>
        <tr>
        <td>3</td>
        <td>Antonio</td>
        <td>0.5568513953733379</td>
        </tr>
        <tr>
        <td>4</td>
        <td>Ana</td>
        <td>0.4788454825081734</td>
        </tr>
        <tr>
        <td>5</td>
        <td>Thomas</td>
        <td>0.45468025898668357</td>
        </tr>
        </table>
        """
        self.assertEqual(remove_whitespace(actual),remove_whitespace(expected))
        
      